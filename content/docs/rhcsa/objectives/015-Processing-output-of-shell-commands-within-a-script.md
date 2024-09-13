# Tech Tutorial: Create Simple Shell Scripts

## Introduction

Shell scripting is an essential skill for system administrators, particularly for those preparing for the Red Hat Certified Systems Administrator (RHCSA) exam. In this tutorial, we will focus on how to write shell scripts that process the output of shell commands. This capability is vital in automating tasks, managing systems efficiently, and extracting necessary information from the command output.

## Step-by-Step Guide

### Step 1: Understanding Shell Script Basics

Before diving into processing command outputs, it is crucial to grasp some basics of shell scripting. A shell script is a text file containing a sequence of commands that the shell can execute. Scripts can simplify complex tasks, automate repetitive processes, and manage system operations.

### Step 2: Setting Up Your Environment

For this tutorial, ensure you are using a Red Hat Enterprise Linux (RHEL) system or a compatible environment. Open your terminal to begin scripting.

### Step 3: Creating a Basic Shell Script

1. Open a text editor:
   ```bash
   vi myscript.sh
   ```

2. Start the script with the shebang line:
   ```bash
   #!/bin/bash
   ```

3. Save and close the editor:
   ```bash
   :wq
   ```

4. Make the script executable:
   ```bash
   chmod +x myscript.sh
   ```

### Detailed Code Examples

#### Example 1: Script to Find and List All JPEG Images

Suppose you want to find all JPEG files in a directory and its subdirectories, and then list them in a file.

```bash
#!/bin/bash
# Script to find and list JPEG images

# Find all .jpg files in the current and sub-directories
files=$(find . -type f -name "*.jpg")

# Loop through the files and output to a list
echo "Listing all JPEG files:" > jpeg_list.txt
for file in $files; do
    echo "$file" >> jpeg_list.txt
done

echo "Operation completed. Check jpeg_list.txt for the list of JPEG files."
```

#### Example 2: Script to Check Disk Usage and Alert if Above Threshold

This script checks the disk usage of the `/home` directory. If usage exceeds 80%, it sends an alert message.

```bash
#!/bin/bash
# Script to check disk usage and send an alert

# Check disk usage of /home directory
disk_usage=$(df /home | awk 'NR==2 {print $(NF-1)}' | sed 's/%//')

# Define threshold
threshold=80

# Compare usage with threshold
if [ $disk_usage -gt $threshold ]; then
    echo "Alert: Disk usage of /home directory is above ${threshold}%."
else
    echo "Disk usage of /home directory is within the acceptable range."
fi
```

### Conclusion

In this tutorial, we covered the basics of creating shell scripts in Red Hat Enterprise Linux and explored how to process the output of shell commands within scripts. These examples demonstrate how to handle file searches and system monitoring, which are common tasks for system administrators. Practicing these scripts will help you understand how to leverage shell scripting to automate and streamline tasks in a RHEL environment.

Remember, the key to mastering shell scripting is consistent practice and exploring various command capabilities. Good luck with your RHCSA exam preparation!