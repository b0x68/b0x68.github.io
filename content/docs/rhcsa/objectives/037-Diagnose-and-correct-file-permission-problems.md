# Tech Tutorial: Create and Configure File Systems

## Introduction

This tutorial is tailored for individuals preparing for the Red Hat Certified System Administrator (RHCSA) exam, focusing on the exam objective: **Diagnose and correct file permission problems**. File permissions in Linux are crucial for protecting the security and integrity of the data on your system. Misconfigured file permissions can lead to unauthorized access or prevent legitimate access, leading to operational issues. We will explore how to effectively manage and troubleshoot file permissions on Red Hat Enterprise Linux (RHEL).

## Step-by-Step Guide

### Understanding Linux File Permissions

Before we dive into correcting permissions, it's essential to understand the basics. In Linux, file permissions control the read (r), write (w), and execute (x) access for the user (u), group (g), and others (o).

To view the permissions of a file or directory, use the `ls -l` command:

```bash
ls -l filename
```

This command will output something like:

```
-rwxr-xr-- 1 user group 0 Sep 29 12:00 filename
```

Here, `-rwxr-xr--` represents the type and permissions of the file:
- The first character `-` indicates if it's a regular file (use `d` for directories).
- The next three characters `rwx` indicate that the user has read, write, and execute permissions.
- The following three `r-x` show that the group has read and execute permissions.
- The last three `r--` show that others have only read permissions.

### Diagnosing Permission Issues

To diagnose permission issues, first identify which user needs access and what type of access they require (read, write, execute). Use `ls -l` to inspect current permissions.

Example scenario: A user reports that they cannot execute a script named `script.sh`.

1. Check current permissions:
   ```bash
   ls -l script.sh
   ```
   Output might be:
   ```
   -rw-r--r-- 1 admin admin 0 Sep 29 12:00 script.sh
   ```
   Here, only the owner (admin) has read and write permissions, and no execute permissions are set.

### Correcting File Permissions

Use the `chmod` (change mode) command to correct permissions.

1. **Adding Execute Permission to the User:**
   ```bash
   chmod u+x script.sh
   ```
   This command adds execute permission for the user.

2. **Setting Specific Permissions:**
   If you need to set the permissions explicitly, you can specify them numerically (r=4, w=2, x=1):
   ```bash
   chmod 755 script.sh
   ```
   This sets read, write, and execute for the user, and read and execute for the group and others.

### Detailed Code Examples

#### Example 1: Correcting Group Write Access

Suppose a file, `example.txt`, needs to be editable by the group.

- Check the permissions:
  ```bash
  ls -l example.txt
  ```
  Output:
  ```
  -rw-r--r-- 1 user group 0 Sep 29 12:00 example.txt
  ```
- Add write permission for the group:
  ```bash
  chmod g+w example.txt
  ```
- Verify the change:
  ```bash
  ls -l example.txt
  ```
  Output:
  ```
  -rw-rw-r-- 1 user group 0 Sep 29 12:00 example.txt
  ```

#### Example 2: Removing Execute Permission for Others

For security, you might want to remove execute permissions for 'others' on a script, `secure.sh`.

- Check the permissions:
  ```bash
  ls -l secure.sh
  ```
  Output:
  ```
  -rwxr-xr-x 1 admin admin 0 Sep 29 12:00 secure.sh
  ```
- Remove execute permission for others:
  ```bash
  chmod o-x secure.sh
  ```
- Verify the change:
  ```bash
  ls -l secure.sh
  ```
  Output:
  ```
  -rwxr-xr-- 1 admin admin 0 Sep 29 12:00 secure.sh
  ```

## Conclusion

Understanding and managing file permissions is a fundamental skill for system administrators, especially when preparing for the RHCSA exam. By following the steps outlined in this tutorial, you can diagnose and correct common file permission issues on RHEL systems, ensuring secure and efficient access control. Practice these commands and scenarios to build your confidence and expertise in handling real-world Linux administration challenges.