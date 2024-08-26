# Tech Tutorial: Create Simple Shell Scripts with Conditional Execution

## Introduction

In this tutorial, we will explore how to create simple shell scripts that conditionally execute code in a Unix-like environment. Conditional execution is fundamental in scripting and programming, allowing the script to make decisions and perform different actions based on certain conditions. We'll focus on the use of conditional statements like `if`, and the `test` command, also represented by `[]`. By the end of this tutorial, you will understand how to implement these in your shell scripts to perform complex decision-making processes.

## Step-by-Step Guide

### 1. Understanding the Basics

Before we dive into writing scripts, it's important to understand the basic syntax of the `if` statement in shell scripting:

```bash
if [ condition ]
then
    # Commands to execute if the condition is true
fi
```

The `condition` inside the brackets can be any expression that evaluates to true or false. The `if` statement executes the command between `then` and `fi` only if the condition is true.

### 2. Writing Your First Conditional Script

Let's start with a simple script that checks if a file exists.

Create a file named `check_file.sh` and add the following content:

```bash
#!/bin/bash

# Script to check if a file exists

FILE="/path/to/your/file.txt"

if [ -e "$FILE" ]; then
    echo "The file exists."
else
    echo "The file does not exist."
fi
```

In this script:
- `-e` is a test option to check if a file exists.
- `$FILE` is a variable holding the path to the file we want to check.
- The `else` block executes if the condition is false.

### 3. Expanding the Script with More Conditions

We can use other test options like `-z` to check if a string is empty, or `-gt` to compare numbers. Let's enhance our script to check if a file is empty:

```bash
#!/bin/bash

# Enhanced script to check file existence and emptiness

FILE="/path/to/your/file.txt"

if [ -e "$FILE" ]; then
    if [ -s "$FILE" ]; then
        echo "The file exists and is not empty."
    else
        echo "The file exists but is empty."
    fi
else
    echo "The file does not exist."
fi
```

Here, `-s` checks if the file has a size greater than zero.

### 4. Using Advanced Conditional Logic

You can also use logical operators like `&&` (AND) and `||` (OR) to combine conditions:

```bash
#!/bin/bash

# Script to check multiple conditions

USER="exampleuser"
FILE="/path/to/your/file.txt"

if [ "$USER" = "exampleuser" ] && [ -e "$FILE" ]; then
    echo "$USER has a file at $FILE."
else
    echo "$USER does not have a file at $FILE, or the file does not exist."
fi
```

This script checks whether the user is "exampleuser" and whether the file exists.

## Detailed Code Examples

Let's consider a real-world scenario where you need to check disk space and notify the user if it's below a threshold:

```bash
#!/bin/bash

# Script to check disk space and notify

THRESHOLD=90
DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$DISK_USAGE" -gt "$THRESHOLD" ]; then
    echo "Disk space critical: ${DISK_USAGE}% used."
else
    echo "Disk space check passed: ${DISK_USAGE}% used."
fi
```

In this script, `df` and `awk` are used to get the disk usage percentage, and the script notifies the user if the usage exceeds 90%.

## Conclusion

Conditional execution in shell scripts is a powerful feature that allows scripts to respond dynamically to different conditions and environments. By mastering the use of `if`, `test`, and `[ ]`, you can automate many tasks in your system and handle various scenarios effectively. Practice by writing scripts for different use cases and explore more test options to enhance your scripting skills. Happy scripting!