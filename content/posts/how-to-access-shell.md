+++
title = "Accessing an Enterprise Linux Shell Prompt and Using the `ps` Command"
date = "2023-12-03T09:51:07-05:00"
author = "Admin"
cover = "bitcat.gif"
tags = ["", ""]
keywords = ["", ""]
description = "Red Hat Enterprise Linux (RHEL) provides a powerful command-line interface known as the shell. In this guide, we will walk through the steps to access the Red Hat Enterprise Linux s    hell prompt and explore one of the commonly used commands, `ps` (process status)."
showFullContent = false
readingTime = false
hideComments = false
color = "" #color from the theme settings
+++

**Accessing the Linux Shell Prompt and Using the `ps` Command**

**Introduction**

Enterprise Linux provides a powerful command-line interface known as the shell. In this guide, we will walk through the steps to access the Linux shell prompt and explore one of the commonly used commands, `ps` (process status).

> Examples of popular Enterprise Linux distributions include:
>
>    * Red Hat Enterprise Linux (RHEL): One of the most widely used enterprise Linux distributions. It is known for its stability, security features, and extensive support services.
>
>    * SUSE Linux Enterprise Server (SLES): Another major player in the enterprise Linux space, offering a reliable and scalable platform with a focus on interoperability.
>
>    * Oracle Linux: Based on RHEL, Oracle Linux is designed for enterprise applications and Oracle Database deployments.

**Accessing the Shell Prompt**


To access the shell prompt in Red Hat Enterprise Linux, follow these steps:

1. **Login to your Red Hat Enterprise Linux System:**
   - Use your credentials to log in to the system.

2. **Open a Terminal:**
   - Once logged in, open a terminal window. You can find the terminal application in the system menu or use the keyboard shortcut `Ctrl + Alt + T`.

3. **Access the Shell Prompt:**
   - The terminal opens with a shell prompt where you can enter commands.

```bash
[user@hostname ~]$
```
Now that you are at the shell prompt, you can start issuing commands, and one of the commonly used commands is `ps`.

Using the `ps` Command

The `ps` command is used to display information about processes running on the system. Here are some common options with the `ps` command:

- **ps aux:**
  - Displays a detailed list of all processes running on the system.

```bash
ps aux
```

- **ps -ef:**
  - Similar to `ps aux`, but uses the BSD syntax.

```bash
ps -ef
```

- **ps aux | grep <process_name>:**
  - Filters the process list to show only the processes matching the specified name.

```bash
ps aux | grep sshd
```

- **ps -e --forest:**
  - Displays a hierarchical tree view of processes.

```bash
ps -e --forest
```

- **ps -o pid,cmd:**
  - Customizes the output to display only the process ID and command.

```bash
ps -o pid,cmd
```

Explore more options and combinations by referring to the `ps` command's manual page:

```bash
man ps
```

Remember, the `ps` command provides valuable insights into the processes running on your system, helping you monitor and manage them effectively.

Conclusion

In this guide, we covered the steps to access the shell and explored the `ps` command for viewing information about processes. The command-line interface is a powerful tool for system administrators and users to interact with the operating system efficiently.
