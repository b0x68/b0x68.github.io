# Tech Tutorial: Understand and Use Essential Tools

## Introduction

In this tutorial, we will delve into how to efficiently locate, read, and utilize system documentation within Red Hat Enterprise Linux (RHEL). Mastering these tools is crucial for any systems administrator, especially those preparing for the Red Hat Certified System Administrator (RHCSA) exam. We will focus on three primary sources of system documentation: `man` pages, `info` pages, and the `/usr/share/doc` directory.

Understanding how to access and interpret these resources is key to troubleshooting and mastering Linux commands and configurations. Let's get started by exploring each tool individually.

## Step-by-Step Guide

### 1. The `man` Command

The `man` command displays the manual pages for other commands and programs. It’s one of the first tools you should use when you need documentation about a command or configuration on your system.

#### Usage

```bash
man [option] [command]
```

#### Example: Viewing the `man` page for the `ls` command

```bash
man ls
```

This command will display the manual page for the `ls` command, which lists directory contents. You can navigate through the man page using the arrow keys, or search for specific terms by pressing `/`, typing your search term, and pressing enter.

### 2. The `info` Command

While `man` pages are useful, they can sometimes be brief and lacking in practical examples. The `info` command provides more detailed documentation.

#### Usage

```bash
info [option] [command]
```

#### Example: Viewing the `info` page for the `grep` command

```bash
info grep
```

This command will show a detailed document about the `grep` command, complete with practical examples and in-depth descriptions. `info` pages are navigated similarly to web pages, using links and nodes.

### 3. Browsing `/usr/share/doc`

This directory contains documentation and examples for many packages installed on your system. It’s a valuable resource for more in-depth information that might not be available in `man` or `info` pages.

#### Example: Exploring documentation for the `httpd` package

```bash
ls /usr/share/doc/httpd*
```

This command lists all documentation available for the `httpd` package. You can use `cat` or `less` to read these files:

```bash
less /usr/share/doc/httpd-2.4.37/README
```

This will display the README file for the `httpd` package, which can include configuration tips, directory structures, and other useful information.

## Detailed Code Examples

Let’s consolidate our learning with a more complex, real-world example of using these documentation tools together.

### Scenario: Configuring SSH

Suppose you need to configure SSH on a RHEL system and want to ensure you understand all options available.

1. **Check the `man` page for sshd_config:**

    ```bash
    man sshd_config
    ```

    This command will show all available configuration options for the SSH daemon.

2. **Use `info` to learn about the `ssh` command:**

    ```bash
    info ssh
    ```

    This will provide a detailed document about the SSH client.

3. **Look for additional examples or common issues in `/usr/share/doc`:**

    ```bash
    ls /usr/share/doc/openssh*
    cat /usr/share/doc/openssh-server-*/README
    ```

    This will help you find any additional documentation or README files related to OpenSSH server.

## Conclusion

Mastering the `man`, `info` commands and understanding how to navigate and utilize the `/usr/share/doc` directory are fundamental skills for any RHEL system administrator. These tools provide a wealth of information that can help you understand and configure your system effectively. Regularly referring to these resources can enhance your troubleshooting skills and deepen your understanding of Linux systems. Keep exploring and practicing, and you'll be well-prepared for the RHCSA exam and your duties as a systems administrator.