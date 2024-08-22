# Tech Tutorial: Create Simple Shell Scripts Using Conditional Statements

## Introduction

In this tutorial, we will explore how to use conditional statements in shell scripting to make decisions. Conditional statements are a fundamental aspect of programming, allowing the script to execute different code blocks based on certain conditions. We will focus mainly on the `if` statement, the `test` command, and the `[` (which is a synonym for `test`) in Bash scripting.

## Prerequisites

For this tutorial, you will need:
- Access to a Unix-like operating system (Linux, macOS, etc.)
- Basic knowledge of command-line interface and shell commands
- A text editor (like vim, nano, or even a graphical text editor)

## Step-by-Step Guide

### 1. Understanding the `if` Statement

The `if` statement is used to test a condition and execute a block of code if the condition is true. Here’s the basic syntax:

```bash
if [ condition ]
then
    # code to execute if condition is true
fi
```

### 2. The `test` Command and `[ ]`

`test` and `[ ]` are used to evaluate conditions. When using `[ ]`, make sure to leave a space after `[` and before `]`. Here's how you can use them:

```bash
if test condition
then
    # code if condition is true
fi

# OR

if [ condition ]
then
    # code if condition is true
fi
```

### 3. Writing Your First Script

Let's start by creating a simple script that checks if a file exists.

#### Step 3.1: Create the Script

Open your terminal, and type:

```bash
nano file_exist.sh
```

#### Step 3.2: Add the Following Script

```bash
#!/bin/bash

# Script to check if a file exists

filename="$1"

if [ -e "$filename" ]; then
    echo "The file $filename exists."
else
    echo "The file $filename does not exist."
fi
```

#### Step 3.3: Save and Exit

Press `CTRL+X`, then `Y` to save and exit.

#### Step 3.4: Make the Script Executable

Run:

```bash
chmod +x file_exist.sh
```

#### Step 3.5: Test the Script

```bash
./file_exist.sh /path/to/your/file.txt
```

Replace `/path/to/your/file.txt` with the actual file path.

### 4. Detailed Code Examples

#### Example 1: Check if a Number is Positive

```bash
#!/bin/bash

# Check if the number is positive

number=$1

if [ $number -gt 0 ]; then
    echo "$number is positive."
else
    echo "$number is not positive."
fi
```

#### Example 2: Using Multiple Conditions

```bash
#!/bin/bash

# Check file size is greater than 1KB and owner has write permission

filename="$1"

if [ -s "$filename" ] && [ -w "$filename" ]; then
    echo "The file $filename is larger than 1KB and writable."
else
    echo "The file $filename is not meeting criteria."
fi
```

## Conclusion

In this tutorial, you learned how to use conditional statements in shell scripts to perform different actions based on conditions. We covered how to use `if`, `test`, and `[ ]` for condition checking. These tools are incredibly powerful for writing scripts that require decision-making based on the attributes of files, user input, or other computational results. You're now equipped to add more sophisticated logic to your shell scripts, adapting them to more complex real-world scenarios.