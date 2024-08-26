# Tech Tutorial: Create Simple Shell Scripts Using Looping Constructs

## Introduction
In this tutorial, we are going to delve into the world of shell scripting with a focus on using looping constructs such as `for` loops to process files and command line inputs. Shell scripting is a powerful tool for automating repetitive tasks, simplifying complex operations, and managing system functionalities efficiently.

## Prerequisites
To follow this tutorial, you should have:
- A basic understanding of command line interface (CLI).
- Access to a Unix-like operating system (Linux, macOS), or a Windows machine with a Bash emulation environment (like Git Bash).
- A text editor for writing scripts (e.g., Vim, Nano, or VS Code).

## Step-by-Step Guide

### Step 1: Understanding the Basics of `for` Loops
A `for` loop in shell scripting is used to iterate over a list of items and perform actions on each item. The syntax of a `for` loop in Bash is as follows:

```bash
for item in [list]
do
    [actions]
done
```

### Step 2: Setting Up Your Script
1. Open your terminal.
2. Create a new file named `process_files.sh` using a text editor, for example:
   ```bash
   nano process_files.sh
   ```
3. Start the script with the shebang line to specify the script uses Bash:
   ```bash
   #!/bin/bash
   ```

### Step 3: Loop Through Files in a Directory
Let’s write a script that will loop through all files in a specified directory and display their names.

Add the following code to `process_files.sh`:
```bash
#!/bin/bash

# Directory to loop through
directory=$1

# Check if the directory exists
if [ -d "$directory" ]; then
    # Loop through each file in the directory
    for file in "$directory"/*
    do
        echo "Processing $file"
        # You can add more commands here to process each file
    done
else
    echo "Directory does not exist."
fi
```
Usage:
```bash
bash process_files.sh /path/to/directory
```

### Step 4: Processing Command Line Input
Modify the script to accept filenames directly from the command line and process them.

Update `process_files.sh` with this code:
```bash
#!/bin/bash

# Loop through each command line argument
for file in "$@"
do
    if [ -f "$file" ]; then
        echo "Processing $file"
        # Insert file processing commands here
    else
        echo "Error: $file does not exist."
    fi
done
```
Usage:
```bash
bash process_files.sh file1.txt file2.txt file3.txt
```

### Step 5: Advanced Example: Count Words in Text Files
Let’s create a script that counts the words in text files in a directory.

Add this to a new script `count_words.sh`:
```bash
#!/bin/bash

directory=$1

if [ -d "$directory" ]; then
    for file in "$directory"/*.txt
    do
        word_count=$(wc -w < "$file")
        echo "$file has $word_count words."
    done
else
    echo "Directory does not exist."
fi
```
Usage:
```bash
bash count_words.sh /path/to/directory
```

## Conclusion
In this tutorial, you have learned how to use `for` loops in shell scripts to process files and handle command line arguments. These skills are fundamental for automating tasks and can be applied to a variety of scenarios in system administration, software development, and data processing tasks. Practice by modifying the scripts to handle different file types or perform different types of processing to deepen your understanding.

Happy scripting!