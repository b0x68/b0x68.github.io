# Tech Tutorial: Understand and Use Essential Tools

## Introduction

Accessing a shell prompt and issuing commands with correct syntax is a foundational skill for anyone in IT, particularly those pursuing roles involving systems administration, DevOps, or software development. This tutorial will guide you through the basics of accessing a shell prompt, understanding its environment, and using command-line syntax to execute and manipulate commands effectively.

## Step-by-Step Guide

### Accessing the Shell Prompt

#### On Windows

1. **Using Command Prompt:**
   - Press `Win + R`, type `cmd`, and press Enter.
   - This opens the Windows Command Prompt, which is a native shell for Windows.

2. **Using PowerShell:**
   - Search for PowerShell in the Start menu and click on it.
   - PowerShell is a more powerful shell compared to the traditional Command Prompt.

3. **Using Windows Subsystem for Linux (WSL):**
   - Install WSL from the Microsoft Store (choose your preferred Linux distribution, e.g., Ubuntu).
   - After installation, open the Linux distribution from the Start menu to access the Linux shell.

#### On macOS

1. **Using Terminal:**
   - Press `Cmd + Space` to open Spotlight Search, type `Terminal`, and press Enter.
   - This opens the macOS Terminal, which provides access to a Unix shell.

#### On Linux

1. **Using Terminal:**
   - Most Linux distributions can access the terminal by pressing `Ctrl + Alt + T`.
   - Alternatively, you can search for "Terminal" in your desktop environment’s application launcher.

### Basic Shell Commands and Syntax

Understanding the basic syntax of shell commands is crucial. Here, we will cover the most commonly used commands and their syntax in a Unix-like shell (applicable to Linux and macOS or WSL on Windows).

#### 1. `echo`
**Purpose:** Prints text to the terminal.
```bash
echo "Hello, world!"
```

#### 2. `ls`
**Purpose:** Lists the contents of a directory.
```bash
ls                # List contents of the current directory
ls -l             # List with detailed information
ls -a             # List all files, including hidden files
```

#### 3. `cd`
**Purpose:** Changes the current directory.
```bash
cd /path/to/directory  # Move to specified directory
cd ..                 # Move up one directory
```

#### 4. `pwd`
**Purpose:** Displays the current directory path.
```bash
pwd
```

#### 5. `mkdir`
**Purpose:** Creates a new directory.
```bash
mkdir new_directory
```

#### 6. `rm`
**Purpose:** Removes files or directories.
```bash
rm file.txt             # Remove a file
rm -r directory_name    # Remove a directory and its contents
```

### Combining Commands

You can combine multiple commands using operators. The most common operators are:

- **Semicolon (`;`)**: Allows you to execute multiple commands in succession, regardless of whether the previous command succeeded.
- **AND (`&&`)**: Executes the second command only if the first command succeeds.
- **OR (`||`)**: Executes the second command only if the first command fails.
- **Pipe (`|`)**: Passes the output of the first command as input to the second command.

**Example:**
```bash
cd /var/log && ls -l || echo "Failed to change directory"
```

This command changes the directory to `/var/log`, lists its contents if the `cd` command is successful, and prints "Failed to change directory" if not.

## Detailed Code Examples

Let’s explore a real-world scenario where these commands can be utilized effectively.

**Scenario:** You need to check disk usage, clean up unnecessary files, and archive old logs.

```bash
# Check disk usage
df -h

# Go to log directory
cd /var/log

# Remove old .log files
find . -name '*.log' -mtime +90 -exec rm {} \;

# Archive remaining logs
tar -czvf archived_logs.tar.gz *.log

# Check space again
df -h
```

In this script:
- `df -h` checks the disk space.
- `find` command searches and removes `.log` files older than 90 days.
- `tar` command archives the remaining log files.

## Conclusion

Mastering the shell prompt and its command syntax is crucial for automating tasks and managing systems efficiently. This tutorial provides a foundation, but the best way to learn is through continuous practice and exploration. Experiment with different commands, read the man pages (`man command-name`), and use the shell to streamline your workflows. Remember, proficiency at the command line is a powerful tool in your tech toolkit.