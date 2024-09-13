# Tech Tutorial: Create Simple Shell Scripts Using Looping Constructs in RHEL

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, one of the key objectives is to demonstrate proficiency in writing shell scripts that leverage looping constructs to process files and command line input. This tutorial will guide you through the basics of creating shell scripts using `for` loops, which are particularly powerful in automating repetitive tasks in Red Hat Enterprise Linux (RHEL).

## Step-by-Step Guide

### 1. Understanding the Basics of Shell Scripting

Before diving into the specifics of looping constructs, it's essential to understand the basics of shell scripting in RHEL. A shell script is simply a text file with a list of commands that the shell can execute.

### 2. Setting Up Your Environment

Open your terminal in RHEL. You can create a new script file using any text editor, such as `vi` or `nano`. For instance:

```bash
vi myscript.sh
```

Start by adding the shebang line at the top of your script. This line tells the system what interpreter to use to execute the script, which will be the Bash shell in this case:

```bash
#!/bin/bash
```

### 3. Making the Script Executable

After writing your script, save and close the editor. You need to make the script executable:

```bash
chmod +x myscript.sh
```

### 4. Using `for` Loops in Scripts

The `for` loop is one of the most useful constructs in shell scripting for processing files and input. Here, we'll use it in several contexts.

#### Example 1: Loop Over a List of Numbers

To perform an action with a range of numbers, you can use:

```bash
#!/bin/bash

for i in {1..5}
do
  echo "Number $i"
done
```

This script will print numbers 1 to 5.

#### Example 2: Processing Command Line Input

This example shows how to process command line arguments passed to the script.

```bash
#!/bin/bash

# Loop through every argument given to the script
for arg in "$@"
do
  echo "Processing $arg"
done
```

Usage:

```bash
./myscript.sh file1.txt file2.txt file3.txt
```

#### Example 3: Looping Through Files in a Directory

This script will loop through all `.txt` files in a directory and display their names.

```bash
#!/bin/bash

for file in *.txt
do
  echo "Processing file $file"
done
```

### 5. Advanced Example: Processing Files Based on Content

Suppose you have multiple configuration files, and you need to apply a specific command to files containing a certain pattern. Here's how you could script that:

```bash
#!/bin/bash

for file in /etc/*.conf
do
  if grep -q 'specific-pattern' "$file"; then
    echo "Pattern found in $file"
    # You can add more commands here to process these files
  fi
done
```

## Detailed Code Examples

The following script demonstrates processing text files to find a specific pattern and reports each occurrence with its file:

```bash
#!/bin/bash

pattern=$1 # First command line argument as a pattern to search
shift      # Shift all arguments to the left, so $2 becomes $1, etc.

for file in "$@"
do
  echo "Searching in $file..."
  grep -Hn "$pattern" "$file" || echo "No match found in $file"
done
```

Usage:

```bash
./searchscript.sh "pattern" file1.txt file2.txt file3.txt
```

## Conclusion

In this tutorial, we've explored how to create simple yet powerful shell scripts using `for` loops in RHEL. These scripts can automate tasks like processing files and handling user input, significantly reducing manual effort and potential for error. As you prepare for the RHCSA exam, practice these examples and try to modify them according to different scenarios you might encounter.