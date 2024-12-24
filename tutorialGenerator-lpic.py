from openai import OpenAI
import os
import re

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Exam Objectives
exam_objectives_file = 'exam-lpic3virt.txt'

# Output
output_folder = '~/projects/b0x68.github.io/content/docs/lpic/lpic3-virtual/objectives/'

os.makedirs(output_folder, exist_ok=True)

# Generate a blog page using OpenAI API
def generate_blog_page(exam_objective):
    messages = [
        {"role": "system", "content": "You are a subject matter expert in Linux the domain. Generate a tutorial for a technical blog that covers the following exam objective. Please include robust, thoroughly detailed real world code examples and lots of them:"},
        {"role": "user", "content": f"""

        # Tech Tutorial: {exam_objective['title']}

        **Exam Objective:** {exam_objective['description']}

        **Key Knowledge Areas:**
        {exam_objective['key_areas']}

        **Utilities:**
        {exam_objective['utilities']}

        You are a subject matter expert in the following technical domain. Generate a tutorial for a technical blog that covers the following exam objectiv    e. Please include robust, thoroughly detailed real world examples. Use the FULL list of commands in each exam objective section, not partial list. Include sections such as Introduction, Step-by-Step Guide, Detailed Code Examples for every single command in the topic; lots of code examples, and Conclusion. Use markdown formatting.
        """}
    ]

    response = client.chat.completions.create(model="gpt-4-turbo",
    messages=messages,
    max_tokens=1500,
    temperature=0.7)

    # Prepare the blog content
    blog_content = response.choices[0].message.content.strip()

    # Add the required header to the blog content
    header = f"""
    ---
    title: "{exam_objective['title']}"
    #bookCollapseSection: true
    ---
    """

    # Combine the header with the blog content
    full_content = header + "\n" + blog_content

    return full_content

# Function to parse the objectives from the file
def parse_exam_objectives(file_content):
    objectives = []
    current_objective = {}
    key_areas = []
    utilities = []
    description = ""
    state = 'WAITING_FOR_HEADER'

    for line in file_content:
        line = line.strip()

        match = re.match(r'(\d+\.\d+) (.*) \(weight: (\d+)\)', line)
        if match:
            if current_objective:
                current_objective['key_areas'] = '\n'.join(key_areas)
                current_objective['utilities'] = '\n'.join(utilities)
                objectives.append(current_objective)

            current_objective = {
                'objective_number': match.group(1).strip(),    
                'title': match.group(0).strip(),
                #'weight': match.group(3).strip(),
                'description': '',
                'key_areas': '',
                'utilities': ''
            }
            key_areas = []
            utilities = []
            description = ""
            state = 'WAITING_FOR_DESCRIPTION'

        elif state == 'WAITING_FOR_DESCRIPTION' and line.startswith("Description"):
            state = 'READING_DESCRIPTION'
            continue

        elif state == 'READING_DESCRIPTION':
            if line.startswith("Key Knowledge Areas:"):
                current_objective['description'] = description.strip()
                state = 'WAITING_FOR_KEY_AREAS'
                description = ""
                continue
            description += line + " "

        elif state == 'WAITING_FOR_KEY_AREAS' and line.startswith("Key Knowledge Areas:"):
            state = 'READING_KEY_AREAS'
            continue

        elif state == 'READING_KEY_AREAS':
            if line.startswith("The following is a partial list of the used files, terms and utilities:"):
                current_objective['key_areas'] = '\n'.join(key_areas)
                state = 'WAITING_FOR_UTILITIES'
                continue
            key_areas.append(line.strip())

        elif state == 'WAITING_FOR_UTILITIES' and line.startswith("The following is a partial list of the used files, terms and utilities:"):
            state = 'READING_UTILITIES'
            continue

        elif state == 'READING_UTILITIES':
            if line.strip() == "":
                continue
            utilities.append(line.strip())

    if current_objective:
        current_objective['key_areas'] = '\n'.join(key_areas)
        current_objective['utilities'] = '\n'.join(utilities)
        objectives.append(current_objective)

    return objectives

# Read the file and parse the objectives
with open(exam_objectives_file, 'r') as file:
    file_content = file.readlines()
    exam_objectives = parse_exam_objectives(file_content)

# Generate and save markdown files for each objective
for i, objective in enumerate(exam_objectives, start=1):
    blog_content = generate_blog_page(objective)
    formatted_objective_number = objective['objective_number'].replace('.', '-')
    output_path = os.path.join(output_folder, f"{formatted_objective_number}.md")
    with open(output_path, 'w') as output_file:
        output_file.write(blog_content)
    print(f'Saved: {output_path}')

print('All tutorials have been generated.')

