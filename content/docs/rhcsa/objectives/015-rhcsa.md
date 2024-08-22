# Tech Tutorial: Create Simple Shell Scripts

## Introduction

Shell scripting is an essential skill for anyone in the IT field, particularly system administrators, developers, and DevOps professionals. Shell scripts allow you to automate repetitive tasks, manage system operations, and improve your productivity. This tutorial focuses on processing the output of shell commands within a script, which is a vital capability for creating dynamic and responsive scripts.

## Step-by-Step Guide

### 1. Understanding the Shell Environment
Before diving into scripting, it's important to have a basic understanding of the shell environment you are working in. Bash (Bourne Again SHell) is the most common shell used in Linux environments. It provides a powerful platform for writing scripts.

### 2. Basic Shell Script Syntax
A shell script is a text file containing a sequence of commands. To start writing a shell script, you first need to declare the interpreter that will execute the script. This is typically done with a "shebang" line at the top of the file:

```bash
#!/bin/bash
```

### 3. Making the Script Executable
After writing your script, you need to make it executable. This can be done with the `chmod` command:

```bash
chmod +x myscript.sh
```

### 4. Running the Script
To run your script, simply type the path to the script in the terminal:

```bash
./myscript.sh
```

## Detailed Code Examples

### Example 1: Capture and Process Output
The ability to capture and process the output from shell commands allows scripts to make decisions based on command outputs. Here's a simple script that checks the current directory's disk usage and warns if it exceeds a certain limit:

```bash
#!/bin/bash

# Capture the output of the `df` command and extract the use% of the current directory
current_usage=$(df . | tail -1 | awk '{print $5}' | sed 's/%//')

# Check if the current usage exceeds 80%
if [[ $current_usage -gt 80 ]]; then
    echo "Warning: Current disk usage is at $current_usage%."
else
    echo "Disk usage is under control."
fi
```

### Example 2: Process a List of Files
In this example, we'll write a script that processes a list of files and reports their line counts:

```bash
#!/bin/bash

# Directory containing the files
directory="/path/to/files"

# Loop through all text files in the directory
for file in $directory/*.txt; do
    # Count the lines in each file
    line_count=$(wc -l < "$file")
    
    echo "The file $file has $line_count lines."
done
```

### Example 3: Using Command Output in Conditions
Here, we demonstrate a script that checks if a specific process is running and takes action based on that:

```bash
#!/bin/bash

# Process to check
process_name="apache2"

# Check if the process is running
if pgrep $process_name > /dev/null 2>&1; then
    echo "$process_name is running."
else
    echo "$process_name is not running. Starting $process_name."
    systemctl start $process_name
fi
```

## Conclusion

This tutorial has introduced you to the basics of creating simple shell scripts with a focus on processing the output of shell commands. We've seen how to capture command outputs, use them in conditions, and loop through files for processing. Shell scripting is a powerful tool that can greatly enhance your ability to perform and automate tasks on Linux systems. With practice, you can extend these basics into more complex scripts that handle a variety of automation tasks effectively.

By mastering the concepts and examples provided in this tutorial, you'll be well-prepared to tackle real-world problems using shell scripting. Whether it's system monitoring, file management, or process control, your scripts can now dynamically react to the state of the system based on the output from shell commands. Happy scripting!