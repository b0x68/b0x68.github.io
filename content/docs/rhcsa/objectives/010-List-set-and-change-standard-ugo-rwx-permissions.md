# Tech Tutorial: Understand and Use Essential Tools

## Introduction

Managing file permissions is a fundamental task for Linux administrators, particularly those preparing for the Red Hat Certified System Administrator (RHCSA) exam. This tutorial will focus on how to list, set, and change standard ugo/rwx permissions on Red Hat Enterprise Linux (RHEL), which are critical skills for any system administrator.

Permissions in Linux are crucial as they control the ability to read, write, and execute files and directories. In Linux, each file and directory has three types of permissions:
- **Read (r)**: Allows the contents of the file to be read.
- **Write (w)**: Allows writing or modifying the file or directory.
- **Execute (x)**: Allows executing a file or traversing a directory.

These permissions can be set for three types of users:
- **User (u)**: The owner of the file.
- **Group (g)**: The group associated with the file.
- **Others (o)**: Any other user who has access to the file.

This guide will walk you through how to list, set, and modify these permissions using command-line tools available in RHEL.

## Step-by-Step Guide

### 1. Listing Current Permissions

Before changing file permissions, it's important to know how to view them. The `ls` command, combined with `-l` option, is used to list down the detailed information about files and directories, including their permissions.

```bash
ls -l filename
```

This command will output something like:

```
-rw-r--r--. 1 root root 0 Sep 29 12:00 filename
```

Here, `-rw-r--r--` represents the type and the permission of the file. The first character indicates the type of the file (`-` for regular file, `d` for directory). The next nine characters are the permissions for user, group, and others respectively.

### 2. Changing Permissions

To change the file permissions, you use the `chmod` (change mode) command. Permissions can be set in either symbolic mode or numeric mode.

#### Using Symbolic Mode

In symbolic mode, you can modify permissions by specifying the user type (`u`, `g`, `o`, `a` for all), the operation (`+` to add, `-` to remove, `=` to set exactly), and the permissions (`r`, `w`, `x`).

**Example: Adding execute permission to the user**

```bash
chmod u+x filename
```

**Example: Removing write permission for the group**

```bash
chmod g-w filename
```

**Example: Setting read and write permissions for others**

```bash
chmod o=rw filename
```

#### Using Numeric Mode

Permissions can also be set using a three-digit number. Each digit is between 0 and 7 and corresponds to the permissions for user, group, and others. The value of each digit is the sum of:
- 4 for read (r)
- 2 for write (w)
- 1 for execute (x)

**Example: Setting permissions to read and write for user, read for group, and none for others (rw-r-----)**

```bash
chmod 640 filename
```

### 3. Verifying Changes

After changing permissions, always verify to ensure the correct permissions have been set:

```bash
ls -l filename
```

## Detailed Code Examples

Let's take a real-world scenario where you have a script file named `update.sh` that should be executable by the user and readable by the group, but not accessible by others.

1. **Check current permissions:**

    ```bash
    ls -l update.sh
    -rw-r--r--. 1 user user 0 Oct 1 17:00 update.sh
    ```

2. **Make the script executable by the user and remove all permissions for others:**

    ```bash
    chmod u+x,o= update.sh
    ```

3. **Verify the changes:**

    ```bash
    ls -l update.sh
    -rwxr----- 1 user user 0 Oct 1 17:00 update.sh
    ```

## Conclusion

Understanding and managing file permissions is vital for securing a Linux system. By learning how to list, set, and modify these permissions, you're ensuring that files and directories are only accessible to the users who have the right to view or modify them. This tutorial covered the basics, but remember, practice is key, especially if you're preparing for the RHCSA exam. Experiment with different scenarios and permission settings to become proficient in managing Linux permissions on RHEL.