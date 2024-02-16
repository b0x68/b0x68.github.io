+++
title = "Process script inputs ($1, $2, etc.)"
date = "2024-02-16T10:30:33-05:00"
author = "root"
cover = ""
tags = ["user", "shell", "systems", "command", "processing", ""process", "process", "commands"]
keywords = ["commands", "shell", "file", "processing", "files", "user.", "systems", "files,"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# How to Process Script Inputs in Red Hat Certified Systems Administrator Exam

In the Red Hat Certified Systems Administrator (RHCSA) exam, one of the objectives is "Process script inputs ($1, $2, etc.)". This objective focuses on understanding how to handle and use input arguments in shell scripts. In this tutorial, we will cover everything you need to know to successfully complete this objective in the exam.

## Understanding Script Inputs
Before diving into how to process script inputs, it is important to understand what they are and why they are important. Script inputs, also known as command line arguments, are values that are passed to a shell script when it is executed. These inputs can be used to provide additional information or instructions to the script, making it more versatile and dynamic.

For example, if you have a script that contains a list of commands to be executed, you can pass in the name of a file as an input argument to specify which file the commands should be applied to. This will allow the same script to be used for different files, making it more flexible and reusable.

## Accessing Script Inputs
To access the input arguments in a shell script, we use special variables known as positional parameters. These variables are automatically initialized when the script is executed and hold the values of the input arguments passed in. The first input argument is stored in the variable $1, the second in $2, and so on. It is important to note that $0 holds the name of the script itself.

Example:
```bash
#!/bin/bash
# This script takes in two input arguments and prints them to the screen

echo "Input argument 1: $1"
echo "Input argument 2: $2"
```

If we execute this script with the command `./script.sh foo bar`, it will output:
```
Input argument 1: foo
Input argument 2: bar
```

## Using Script Inputs
Now that we know how to access script inputs, let's see how we can use them in our scripts. The most common way to use input arguments is in conditional statements, where they are used to make decisions based on user input.

Example:
```bash
#!/bin/bash
# This script checks if the first input argument is greater than the second

if [ $1 -gt $2 ]
then
  echo "$1 is greater than $2"
else
  echo "$1 is not greater than $2"
fi
```

If we execute this script with the command `./script.sh 5 3`, it will output:
```
5 is greater than 3
```

Another way to use input arguments is in loops, where they can be used to iterate through a list of items provided by the user.

Example:
```bash
#!/bin/bash
# This script prints all the files in the directory specified by the user

for file in $1/*
do
  echo "$file"
done
```

If we execute this script with the command `./script.sh ~/Documents`, it will output the names of all the files in the Documents directory.

## Validating Script Inputs
In some cases, it may be necessary to validate the input arguments before using them in the script. This ensures that the correct type and format of data is provided by the user and prevents errors or unexpected behavior.

To validate input arguments, we can use conditional statements and check for specific conditions or patterns in the arguments. We can also use the `read` command to prompt the user for input and validate it before using it in the script.

Example:
```bash
#!/bin/bash
# This script checks if the first input argument is a valid IP address

# Validate the number of input arguments
if [ $# -ne 1 ]
then
  echo "Please provide one input argument"
  exit 1  # Exit with an error code
fi

# Validate the format of the IP address
if ! [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]
then
  echo "Invalid IP address format"
  exit 1  # Exit with an error code
fi

echo "$1 is a valid IP address"
```

If we execute this script with the command `./script.sh 192.168.1.1`, it will output:
```
192.168.1.1 is a valid IP address
```

However, if we execute it with the command `./script.sh 192.168`, it will output:
```
Invalid IP address format
```

## Conclusion
In this tutorial, we have covered the basics of processing script inputs in shell scripts. Remember to review the objectives thoroughly and practice using input arguments in different scenarios before taking the RHCSA exam. Best of luck!