# Tech Tutorial: Manage Security - SELinux File and Process Contexts

Security-Enhanced Linux (SELinux) is a Linux kernel security module that provides a mechanism for supporting access control security policies. It is a powerful tool that enhances the security layer of Linux systems by allowing administrators and programs to control access based on security policies. Understanding how SELinux manages file and process contexts is crucial for system security and compliance.

## Introduction

In this tutorial, we will delve into how to list and identify SELinux file and process contexts. SELinux contexts are labels attached to objects (like files) or processes in the system, dictating what resources a process can access and how it can interact with them.

## Prerequisites

- A Linux system with SELinux installed and enabled (CentOS, Fedora, or RHEL are preferred as SELinux is enabled by default).
- Basic understanding of Linux command line.

## Step-by-Step Guide

### 1. Understanding SELinux Contexts

SELinux contexts are composed of four components:
- **User**: The SELinux user identity.
- **Role**: The role that defines a set of permissions.
- **Type**: Most important for defining access controls.
- **Level**: Used in MLS (Multi-Level Security), specifies the sensitivity.

Context format: `user:role:type:level`

### 2. Listing SELinux Contexts for Files

To view the SELinux context for files, use the `-Z` option with `ls`. Let’s check the SELinux context of the `/etc/passwd` file:

```bash
ls -Z /etc/passwd
```

This will output something like:
```
system_u:object_r:passwd_file_t:SystemLow /etc/passwd
```

### 3. Listing SELinux Contexts for Processes

To view the SELinux context of running processes, you can use `ps` with the `Z` option:

```bash
ps auxZ | grep httpd
```

Output:
```
system_u:system_r:httpd_t:SystemLow  1234 ? Ss 0:00 /usr/sbin/httpd
```

### 4. Changing SELinux File Contexts

To change the context of a file, use the `chcon` command. For example, to change the type of `/var/www/html/index.html` to `httpd_sys_content_t`, use:

```bash
chcon -t httpd_sys_content_t /var/www/html/index.html
```

Verify the change:
```bash
ls -Z /var/www/html/index.html
```

### 5. Restoring Default SELinux Contexts

If you change a file context incorrectly, you can restore the default context using `restorecon`:

```bash
restorecon /var/www/html/index.html
```

Again, verify the change:
```bash
ls -Z /var/www/html/index.html
```

### 6. Managing SELinux Contexts with `semanage`

For a permanent change to the context mapping, use `semanage fcontext`:

```bash
semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
restorecon -Rv /var/www/html
```

This command permanently associates the `httpd_sys_content_t` type with files under `/var/www/html`.

## Conclusion

Understanding and managing SELinux contexts is a fundamental skill for Linux system administrators, especially for maintaining proper security and compliance. By correctly setting and managing these contexts, administrators can prevent unauthorized access and potential security breaches. Always ensure to test configurations in a safe environment before applying them to production.

Remember, SELinux is there to help you. With the right knowledge and skills, you can harness its full potential to enhance the security of your systems.