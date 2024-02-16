+++
title = "Create, delete, and modify local user accounts"
date = "2024-02-16T10:36:35-05:00"
author = "root"
cover = ""
tags = ["shell,", "selinux", "group,", "userdel", "`usermod`", "`--shell`", "adduser", "`adduser`"]
keywords = ["tasks,", "command", "selinux", "user,", "`--shell`", "system.", "user", "(group"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Create, delete, and modify local user accounts

## Introduction
In order to effectively manage a Red Hat system, it is important for a system administrator to have knowledge and skills in creating, deleting, and modifying local user accounts. Understanding this objective is essential for passing the Red Hat Certified Systems Administrator Exam 200. In this tutorial, we will provide a step-by-step guide on how to perform these tasks, in detail.

## Prerequisites
Before getting started, make sure you have the following prerequisites:
- A Red Hat system to work on
- Access to the root user or a user with sudo privileges
- Basic knowledge of the Linux command line interface (CLI)

## Creating a Local User Account
To create a new local user account, follow these steps:

1. Log in to the system as the root user or a user with sudo privileges.

2. Use the `adduser` command to add a new user. For example:
    ```
    sudo adduser johndoe
    ```
   This will create a new local user named "johndoe" with default options.

3. You will be prompted to set a password for the new user. Enter a strong password and confirm it.

4. The `adduser` command also allows you to specify additional options for the new user. You can use the `--comment` option to add a brief description or full name for the user, the `--home` option to specify a different home directory for the user, and the `--shell` option to set a specific login shell for the user.

5. Once the user is created, you can verify it by using the `id` command:
    ```
    id johndoe
    ```
   This will display the user's information, including their UID (user ID) and GID (group ID).

## Deleting a Local User Account
To delete a local user account, follow these steps:

1. Log in to the system as the root user or a user with sudo privileges.

2. Use the `userdel` command to delete the user. For example:
    ```
    sudo userdel johndoe
    ```
   This will delete the "johndoe" user from the system.

3. If you want to also delete the user's home directory and mail spool, use the `userdel` command with the `-r` option:
    ```
    sudo userdel -r johndoe
    ```
   This will delete the user's home directory and any associated files.

4. You can also use the `userdel` command with other options, such as `-f` to force the deletion of the user even if they are currently logged in, or `-Z` to remove SELinux user mapping for the user.

## Modifying a Local User Account
To modify a local user account, follow these steps:

1. Log in to the system as the root user or a user with sudo privileges.

2. Use the `usermod` command to modify the user's settings. For example, to change the user's login shell, you can use the `-s` option:
    ```
    sudo usermod -s /bin/bash johndoe
    ```
   This will change the login shell for the "johndoe" user to "/bin/bash".

3. Other options that can be used with `usermod` to modify a user account include `-c` to change the user's full name or description, `-d` to change the user's home directory, and `-l` to change the username.

4. To add or remove a user from a specific group, use the `usermod` command with the `-aG` option, followed by the group name. For example, to add the "johndoe" user to the "wheel" group, use the following command:
    ```
    sudo usermod -aG wheel johndoe
    ```

## Conclusion
In this tutorial, we have covered the Red Hat Certified Systems Administrator Exam 200 objective of creating, deleting, and modifying local user accounts in great depth. These skills are essential for managing a Red Hat system effectively. With the knowledge gained from this tutorial, you should be well prepared to tackle this objective in the exam. Good luck!