# Tech Tutorial: Manage Security - Restore Default File Contexts

## Introduction

In the realm of Linux systems, particularly those that use SELinux (Security-Enhanced Linux), managing file security contexts is critical for maintaining the security integrity of the system. SELinux adds mandatory access controls (MAC) to the Linux kernel, which are based on file contexts. Sometimes, due to various changes or misconfigurations, these file contexts can be altered, which might lead to software malfunctions or security vulnerabilities. Therefore, restoring default file contexts is an essential skill for any system administrator.

This tutorial will guide you through the process of restoring default file contexts on a Linux system using SELinux. We'll cover how to identify altered contexts, restore them, and verify that they have been set correctly.

## Prerequisites

- A Linux system with SELinux installed and enabled.
- Basic familiarity with Linux command line interface.
- Root or sudo access on the system.

## Step-by-Step Guide

### Step 1: Checking SELinux Status

Before proceeding, ensure that SELinux is enabled and set to enforcing mode. You can check this with the following command:

```bash
sestatus
```

The output should indicate whether SELinux is enabled and its current mode. If SELinux is disabled or in permissive mode, you might need to adjust this to adhere to your organization's security policies.

### Step 2: Identifying Modified File Contexts

To find files that do not have the default SELinux contexts, use the `restorecon` command with the `-n` and `-v` options. This will list the changes that would be made without applying them:

```bash
restorecon -rnv /
```

This command recursively (`-r`) checks files from the root directory (`/`), displaying verbose output (`-v`) of what would be changed without making any actual changes (`-n`).

### Step 3: Restoring Default File Contexts

To restore the default SELinux contexts to files, use the `restorecon` command without the `-n` option:

```bash
restorecon -rv /
```

This command will recursively apply the default SELinux context to all files starting from the root directory. The `-v` option provides verbose output, which is useful for logging and auditing purposes.

### Step 4: Verifying the Changes

After restoring the contexts, it's important to verify that the changes have been applied correctly. You can use the `ls -Z` command to check the SELinux contexts of files:

```bash
ls -Z /path/to/check
```

Replace `/path/to/check` with the actual path you wish to verify. This command displays the SELinux contexts for the files, allowing you to ensure that they have been restored to their defaults.

## Detailed Code Examples

Here’s a detailed example of how you might script the restoration of SELinux contexts in a more controlled manner, focusing on a specific directory, `/var/www/html`, often used for web content:

```bash
#!/bin/bash

# Target directory
TARGET_DIR="/var/www/html"

# Check and print the current SELinux status
echo "Checking SELinux status..."
sestatus

# Display current contexts
echo "Current SELinux contexts in $TARGET_DIR:"
ls -Z $TARGET_DIR

# Dry run to see what would be changed
echo "Performing dry run..."
restorecon -rnv $TARGET_DIR

# Applying restorecon to the target directory
echo "Restoring default contexts..."
restorecon -rv $TARGET_DIR

# Verify and display new contexts
echo "Verifying new contexts..."
ls -Z $TARGET_DIR
```

This script checks the SELinux status, lists the current contexts of files in `/var/www/html`, performs a dry run of `restorecon`, applies the default contexts, and then verifies the changes.

## Conclusion

Restoring default file contexts is a vital operation for maintaining the security posture of SELinux-enabled Linux systems. By routinely checking and correcting file contexts, system administrators can ensure that their systems adhere to the necessary security policies and reduce potential vulnerabilities. Remember, regular audits and checks are the best way to maintain a secure and stable system environment.