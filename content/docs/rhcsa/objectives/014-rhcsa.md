# Tech Tutorial: Create Simple Shell Scripts

## Introduction

Shell scripting is a crucial skill in any system administrator's or developer's arsenal. It allows you to automate repetitive tasks, manage system operations, and improve your overall productivity. In this tutorial, we will focus on how to process script inputs, which are often referred to by their positional parameters ($1, $2, etc.). Understanding how to effectively capture and use these inputs can greatly enhance the versatility of your scripts.

## Step-by-Step Guide

### 1. Understanding Positional Parameters

In shell scripting, positional parameters are variables that hold the values of command-line arguments passed to the script. They are named numerically, starting from `$1` for the first argument, `$2` for the second, and so on. `$0` is a special parameter that holds the name of the script itself.

### 2. Accessing the Parameters

To access these parameters, you simply use their corresponding dollar-sign notation within your script. Here's a basic example:

```bash
#!/bin/bash
# This script prints the first and second command line arguments.

echo "First argument: $1"
echo "Second argument: $2"
```

### 3. Using Parameters in a Real Script

Let's say you want to create a script that greets a user differently depending on the time of day. The user's name and the current hour (in 24-hour format) are passed as command-line arguments.

```bash
#!/bin/bash
# This script greets the user based on the time of day.

name=$1
hour=$2

if [ "$hour" -lt 12 ]; then
    greeting="Good morning"
elif [ "$hour" -lt 17 ]; then
    greeting="Good afternoon"
else
    greeting="Good evening"
fi

echo "$greeting, $name!"
```

To run this script, you would enter something like:

```bash
bash greet.sh Emily 14
```

This would output:

```
Good afternoon, Emily!
```

### 4. Handling Multiple Inputs

If your script needs to handle an unknown number of inputs, you can use a loop to process each argument. Here's an example that sums multiple numbers passed to the script:

```bash
#!/bin/bash
# This script sums all the numbers passed as arguments.

sum=0
for num in "$@"
do
    sum=$(($sum + $num))
done

echo "The total sum is: $sum"
```

Running this script with `bash sum.sh 3 5 7` would output:

```
The total sum is: 15
```

## Detailed Code Examples

### Example 1: File Backup Script

This script takes filenames as arguments and creates a backup of each file.

```bash
#!/bin/bash
# Backup script

for filename in "$@"
do
    cp "$filename" "${filename}.bak"
    echo "Backup of $filename created as ${filename}.bak"
done
```

### Example 2: Directory Creation Script

This script takes multiple directory names as arguments and creates each one, verifying its creation.

```bash
#!/bin/bash
# Directory creation script

for dir in "$@"
do
    mkdir -p "$dir"
    if [ $? -eq 0 ]; then
        echo "Directory $dir created successfully."
    else
        echo "Failed to create directory $dir."
    fi
done
```

## Conclusion

In this tutorial, we explored how to handle script inputs using positional parameters in shell scripts. By effectively utilizing these parameters, you can create flexible and powerful scripts that are capable of performing a wide range of tasks. Whether you're automating system maintenance, managing file backups, or processing user inputs, mastering these techniques is essential for any aspiring shell scripter.