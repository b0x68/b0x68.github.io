import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

output_folder = '~/projects/b0x68.github.io/content/docs/rhcsa/objectives'
os.makedirs(output_folder, exist_ok=True)

# Parsing function of exam objectives
def parse_new_exam_objectives(file_content):
    objectives = []
    current_section = None

    for line in file_content:
        line = line.strip()

        if line.startswith('-'):
            current_section = line.lstrip('-').strip()
        elif line:
            objectives.append({
                'section': current_section,
                'objective': line
            })

    return objectives

# Function to generate a blog page
def generate_blog_page(section, objective):
    messages = [
        {"role": "system", "content": "You are a subject matter expert in the following technical domain. Generate an in depth code and example heavy focused tutorial for a technical blog that covers the following exam objective. Please include robust, thoroughly detailed real world examples:"},
        {"role": "user", "content": f"""
        # Tech Tutorial: {section}

        **Exam Objective:** {objective}

        Write a detailed tech tutorial based on the above exam objective for the Red Hat Certified Systems Administrator exam( this means DO NOT use commands for other distros. Never give examples using commands outside the RHEL distro for this RHCSA tutorial. So only applicable commands and content related. Include sections such as Introduction, Step-by-Step Guide, Detailed Code Examples, and Conclusion. Use markdown formatting.
        """}
    ]

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens=4096,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Read and parse the file
exam_objectives_file = 'rhcsa.txt'

with open(exam_objectives_file, 'r') as file:
    file_content = file.readlines()
    exam_objectives = parse_new_exam_objectives(file_content)

# Generate and save markdown files for each objective
for i, objective in enumerate(exam_objectives, start=1):
    blog_content = generate_blog_page(objective['section'], objective['objective'])
    filename = f"""{i:03d}-{objective['objective'].replace(' ', '-').replace(',', '').replace("'", '').replace("/", '-')}.md"""
    #filename = f"{i:03d}-{objective['objective'].replace(' ', '-')}.md"
    output_path = os.path.join(output_folder, filename)
    
    with open(output_path, 'w') as output_file:
        output_file.write(blog_content)
    
    print(f'Saved: {output_path}')

print('All tutorials have been generated.')

