# Tech Tutorial: Create Simple Shell Scripts Using Looping Constructs

## Introduction

In this tutorial, we will learn how to harness the power of looping constructs in shell scripting to automate repetitive tasks. Looping constructs such as `for` loops are invaluable tools for processing files and command-line inputs efficiently. By the end of this tutorial, you should be able to write shell scripts that perform complex file manipulations and handle user inputs dynamically.

## Step-by-Step Guide

### 1. Understanding Looping Constructs in Shell Scripting

Looping constructs allow a set of commands to be executed repeatedly based on a condition. In shell scripting, the most commonly used loop is the `for` loop. Here, we will focus on:

- `for` loops: To iterate over a list of items.
- Reading and processing file content.
- Handling command-line inputs within loops.

### 2. Setting Up Your Environment

To follow along with this tutorial, you will need access to a Unix-like operating system (Linux, macOS, etc.) and a basic text editor (vim, nano, etc.).

Create a new directory for your scripts:

```bash
mkdir shell_script_tutorial
cd shell_script_tutorial
```

### 3. Detailed Code Examples

#### Example 1: Looping Over a Set of Files

Suppose you have multiple text files in a directory and you want to print the name and line count of each file.

Create some sample files:

```bash
echo "Hello, World!" > file1.txt
echo "This is a test file." > file2.txt
echo "This file\ncontains\nmultiple lines." > file3.txt
```

Script `file_info.sh`:

```bash
#!/bin/bash

# Loop through all txt files in the current directory
for file in *.txt; do
    # Count the number of lines in the file
    line_count=$(wc -l < "$file")
    
    # Print the file name and line count
    echo "$file has $line_count lines"
done
```

Make the script executable and run it:

```bash
chmod +x file_info.sh
./file_info.sh
```

Output:

```
file1.txt has 1 lines
file2.txt has 1 lines
file3.txt has 3 lines
```

#### Example 2: Processing Command Line Inputs

Create a script that accepts filenames as command-line arguments and prints their line counts.

Script `line_counter.sh`:

```bash
#!/bin/bash

# Check if at least one filename is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 file1 [file2 ...]"
    exit 1
fi

# Loop over all arguments
for file in "$@"; do
    if [ -f "$file" ]; then
        line_count=$(wc -l < "$file")
        echo "$file has $line_count lines"
    else
        echo "Error: $file not found."
    fi
done
```

Make the script executable and test it:

```bash
chmod +x line_counter.sh
./line_counter.sh file1.txt file2.txt non_existent_file.txt
```

Output:

```
file1.txt has 1 lines
file2.txt has 1 lines
Error: non_existent_file.txt not found.
```

### 4. Conclusion

In this tutorial, we explored how to use `for` loops in shell scripting to process files and handle command-line inputs efficiently. These basic constructs form the backbone of many automation and data processing tasks in shell scripting, making it a powerful tool for any developer's toolkit.

Experimenting further with these examples and modifying them to suit specific needs will help solidify your understanding of shell scripting and its applications.