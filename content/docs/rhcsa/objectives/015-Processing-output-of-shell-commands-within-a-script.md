# Tech Tutorial: Create Simple Shell Scripts

## Introduction

In this tutorial, we will delve into how to process the output of shell commands within a script. Shell scripting is a powerful tool for automating repetitive tasks, managing systems, and more. Understanding how to manipulate and utilize command outputs can significantly enhance your scripts' capability and functionality.

## Prerequisites

Before starting, you should have:
- A basic understanding of shell commands and environments (Bash, sh, etc.).
- Access to a Linux or Unix-like operating system.
- Basic knowledge of programming concepts.

## Step-by-Step Guide

### Step 1: Understanding Command Execution in Scripts

Shell scripts execute commands in a sequence, similar to how you would in a terminal. The key to processing output is capturing this output for further use. Here’s a simple example:

```bash
#!/bin/bash
output=$(ls)
echo "The contents of the directory are: $output"
```

This script captures the output of `ls` (which lists directory contents) into the variable `output`, then prints it.

### Step 2: Processing Command Output

You can process the output of a command in many ways, like filtering, looping over it, or passing it as an argument to another command.

#### Example: Filtering Output

Suppose you want a list of all txt files in a directory:

```bash
#!/bin/bash
output=$(ls *.txt)
echo "TXT files in the directory: $output"
```

#### Example: Looping Over Output

If you want to process files individually, loop over them:

```bash
#!/bin/bash
for file in $(ls *.txt)
do
  echo "Processing $file"
  # Add more processing commands here
done
```

#### Example: Using Output in Commands

You can use the output of one command as input to another. For example, to count the number of lines in all txt files:

```bash
#!/bin/bash
for file in $(ls *.txt)
do
  lines=$(wc -l $file | awk '{print $1}')
  echo "The file $file has $lines lines."
done
```

### Step 3: Advanced Output Processing

Sometimes, command outputs are complex, and you might need to use tools like `awk`, `sed`, or `grep` to process them effectively.

#### Example: Extracting Specific Information

Imagine you want to check the disk usage of a specific directory and extract just the percentage used:

```bash
#!/bin/bash
output=$(df /home | tail -n 1 | awk '{print $5}')
echo "Disk usage for /home: $output"
```

This script uses `df` to get disk usage, `tail` to get the last line (which contains the usage), and `awk` to extract the fifth field (the percentage).

## Detailed Code Examples

Let’s combine what we’ve learned into a more complex script. This script will check disk space and warn if usage exceeds a certain threshold:

```bash
#!/bin/bash
threshold=90
usage=$(df / | tail -n 1 | awk '{print $5}' | sed 's/%//')

if [ $usage -gt $threshold ]
then
  echo "Warning: Disk usage for root is above $threshold%."
else
  echo "Disk usage for root is within acceptable limits."
fi
```

This script does the following:
- Checks the disk usage for the root directory.
- Extracts and cleans the percentage value.
- Compares it against a set threshold.
- Prints a warning if the threshold is exceeded.

## Conclusion

In this tutorial, we explored how to create simple shell scripts that effectively process the output of shell commands. By learning to capture, manipulate, and use this output, you can create more dynamic and useful scripts. Practice these techniques to build more complex scripts tailored to your needs. Remember, the possibilities with shell scripting are vast, and mastering it can significantly improve your efficiency and productivity.