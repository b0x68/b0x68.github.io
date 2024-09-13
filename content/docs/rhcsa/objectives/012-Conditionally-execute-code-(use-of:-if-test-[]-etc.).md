# Tech Tutorial: Create Simple Shell Scripts with Conditional Execution in RHEL

## Introduction

In this tutorial, we'll delve into writing simple shell scripts on Red Hat Enterprise Linux (RHEL) that incorporate conditional execution. Conditionals are fundamental in scripting as they allow the script to make decisions, execute code based on the conditions, and handle different inputs or environments gracefully.

This guide is particularly tailored for candidates preparing for the Red Hat Certified System Administrator (RHCSA) exam, focusing on the proper use of conditionals like `if`, `test`, and `[]`.

## Step-by-Step Guide

### 1. Understanding the Basics of `if` Statements

The `if` statement is one of the most common conditional structures in shell scripting. It allows the script to execute a set of commands only if a certain condition is true.

#### Syntax of `if` Statement:

```bash
if [ condition ]
then
    commands
fi
```

### 2. Using `test` and `[]` for Conditions

In shell scripts, `test` or `[ condition ]` is used to evaluate a condition. Both are used interchangeably, where `[` is a synonym for `test`.

#### Examples of Conditions:

- Numeric comparisons: `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`
- String comparisons: `=`, `!=`, `-z` (string is null), `-n` (string is not null)
- File tests: `-f` (file exists and is a regular file), `-d` (directory exists), `-r` (file is readable), etc.

### 3. Writing a Basic Conditional Script

Let's write a basic script that checks if a file exists and is readable.

```bash
#!/bin/bash

# Define the file path
file_path="/path/to/your/file.txt"

# Check if the file exists and is readable
if [ -f "$file_path" ] && [ -r "$file_path" ]
then
    echo "The file exists and is readable."
else
    echo "The file does not exist or is not readable."
fi
```

This script uses two tests `-f` and `-r` combined with logical AND `&&` to check both if the file exists and is readable.

### 4. Advanced Conditional Execution

Let's enhance our script by adding more conditions, such as checking if the file is writable and its size is greater than zero.

```bash
#!/bin/bash

# Define the file path
file_path="/path/to/your/file.txt"

# Check conditions using nested if
if [ -f "$file_path" ]; then
    echo "The file exists."

    if [ -r "$file_path" ]; then
        echo "The file is readable."
    else
        echo "The file is not readable."
    fi

    if [ -w "$file_path" ]; then
        echo "The file is writable."
    else
        echo "The file is not writable."
    fi

    if [ -s "$file_path" ]; then
        echo "The file size is greater than zero."
    else
        echo "The file is empty."
    fi
else
    echo "The file does not exist."
fi
```

This script uses nested `if` statements to check multiple properties of the file.

### 5. Best Practices

- Always quote your variables in test conditions to avoid errors and unexpected behaviors, especially when dealing with strings that might contain spaces.
- Prefer `[[ ]]` over `[ ]` in Bash scripts for conditional testing, as it provides more features and is less error-prone.
- Use meaningful comments in your scripts to explain the purpose of each section or condition.

## Conclusion

Understanding and using conditional statements effectively is crucial for writing robust shell scripts in RHEL. This tutorial covered the basics and some advanced aspects of using `if`, `test`, and `[]` in shell scripts. Practice these concepts thoroughly to enhance your scripting skills and prepare effectively for the RHCSA exam. Remember, mastery of conditionals opens up a plethora of scripting possibilities and makes your scripts more dynamic and responsive to different runtime conditions.