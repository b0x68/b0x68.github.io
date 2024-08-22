# Tech Tutorial: Manage Security – Restore Default File Contexts

## Introduction

In the sphere of system administration, particularly on systems running SELinux (Security Enhanced Linux), managing file security contexts is crucial for maintaining the security posture of the operating system. SELinux adds Mandatory Access Controls (MAC) on top of the traditional Discretionary Access Controls (DAC), providing a robust framework that limits program and user activities based on defined policies.

One common task that system administrators might encounter is the need to restore default file contexts. This can be necessary when file contexts have been incorrectly modified or lost due to software bugs, misconfigurations, or system restores from backups that did not preserve SELinux contexts.

This tutorial will guide you through the process of restoring default file contexts using tools available in SELinux-enabled Linux distributions. We will cover the `restorecon` and `fixfiles` utilities, which are integral to managing and repairing SELinux contexts.

## Step-by-Step Guide

### 1. Checking Current Contexts

Before making any changes, it's a good practice to check the current SELinux contexts of the files. You can use the `ls -Z` command to view the SELinux context of files and directories:

```bash
ls -Z /path/to/directory
```

### 2. Using restorecon

`restorecon` is a utility that restores the default SELinux context for files and directories based on the SELinux policy and file context configuration files.

#### Basic Usage

To restore a file or directory to its default SELinux context, you can use:

```bash
restorecon /path/to/file
```

To recursively apply this to a directory, use:

```bash
restorecon -R /path/to/directory
```

#### Verbose Mode

If you want to see what changes are being made, you can add the verbose flag `-v`:

```bash
restorecon -v -R /path/to/directory
```

This command will provide output for each file that is being relabeled.

### 3. Using fixfiles

While `restorecon` is great for specific files or directories, `fixfiles` is a utility to check and restore SELinux contexts for all files on the system. This is particularly useful after a major system update or when numerous file contexts need to be corrected.

#### Check Mode

To check what changes `fixfiles` would make without applying them, use:

```bash
fixfiles -C check
```

#### Restore Mode

To restore SELinux contexts system-wide, use:

```bash
fixfiles restore
```

This command can take considerable time on large filesystems as it relabels every file.

#### On Boot

To schedule a full relabel of the filesystem on the next boot, which can sometimes resolve issues with files that are in use during runtime, you can use:

```bash
fixfiles onboot
```

Then, reboot your system for the process to take effect.

## Detailed Code Examples

Here's a detailed example of how you might script the use of `restorecon` to ensure that a new application directory has the correct SELinux contexts:

```bash
#!/bin/bash

# Define the application directory
app_directory="/opt/myapp"

# Check current contexts
echo "Current SELinux contexts:"
ls -Z $app_directory

# Apply default SELinux contexts
echo "Applying default SELinux contexts..."
restorecon -Rv $app_directory

# Verify the changes
echo "Updated SELinux contexts:"
ls -Z $app_directory
```

This script checks the SELinux contexts before and after applying `restorecon`, providing clear output of the changes made.

## Conclusion

Restoring default file contexts is a powerful way to ensure that your system's security policy is correctly enforced, helping to protect against unintended access or behavior. Tools like `restorecon` and `fixfiles` are essential for system administrators managing SELinux environments. Regular checks and maintenance, especially after significant system changes, can help prevent security lapses due to incorrect SELinux contexts. Always ensure you have backups and test changes in a staging environment when possible to avoid disruptions in production systems.