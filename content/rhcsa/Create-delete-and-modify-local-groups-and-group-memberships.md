+++
title = "Create, delete, and modify local groups and group memberships"
date = "2024-02-16T10:36:59-05:00"
author = "root"
cover = ""
tags = ["new_password`:", "permissions.", "groupmod", "`groupdel`,", "user_name", "groups", "commands", "group_name`"]
keywords = ["`groupmod`,", "command", "`group_name`:", "users.", "`user_name`:", "password.", "group_name", "group_name`"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: "Create, delete, and modify local groups and group memberships"

## Introduction
In this tutorial, we will cover the Red Hat Certified Systems Administrator Exam 200 objective of creating, deleting, and modifying local groups and group memberships. Groups play an important role in Linux systems as they allow users to share resources and permissions, making it easier to manage user access. It is essential for a Red Hat Certified Systems Administrator to have a thorough understanding of how to create, delete, and modify local groups and group memberships.

## Prerequisites
Before we begin, make sure you have a Red Hat Enterprise Linux system and have administrative privileges. It is also helpful to have basic knowledge of the Linux command line.

## Creating Local Groups
To create a new group in Linux, we will use the `groupadd` command. This command will add a new group to the system, along with a group ID (GID) and group password. The syntax for `groupadd` is as follows:

`groupadd [options] group_name`

Let's break down the command:

- `groupadd`: This is the command used to add a new group.
- `[options]`: These are additional options that can be used with `groupadd`. Some common options include:
  - `--gid GID`: This allows you to specify a specific GID for the group.
  - `--password PASSWORD`: This allows you to set a group password, which is typically used for secure group access control.
  - `--system`: This creates a system group with a GID less than 1000, which is reserved for system users.
- `group_name`: This is the name of the group you want to create.

To create a new group named "marketing" with a GID of 1001, we would use the following command:

`groupadd --gid 1001 marketing`

Note: If you do not specify a GID, the system will automatically assign one by incrementing the last GID created on the system.

## Deleting Local Groups
To delete a group in Linux, we will use the `groupdel` command. Only users with administrative privileges can delete groups. The syntax for `groupdel` is as follows:

`groupdel group_name`

Let's break down the command:

- `groupdel`: This is the command used to delete a group.
- `group_name`: This is the name of the group you want to delete.

To delete the "sales" group, we would use the following command:

`groupdel sales`

Note: Before deleting a group, make sure no users are currently members of the group. Otherwise, you will receive an error message and will not be able to delete the group.

## Modifying Local Groups
There are several ways to modify local groups in Linux. The most common methods are using the `groupmod` command or directly editing the `/etc/group` file.

### Using the groupmod command
The `groupmod` command allows us to modify group attributes such as the group name, GID, or group password. The syntax for `groupmod` is as follows:

`groupmod [options] group_name`

Let's break down the command:

- `groupmod`: This is the command used to modify a group.
- `[options]`: These are additional options that can be used with `groupmod`. Some common options include:
  - `--new-name NEW_NAME`: This allows you to change the group name to the specified value.
  - `--gid NEW_GID`: This allows you to change the GID of the group.
  - `--password NEW_PASSWORD`: This allows you to change the group password.
- `group_name`: This is the name of the group you want to modify.

To change the group name of "hr" to "human_resources", we would use the following command:

`groupmod --new-name human_resources hr`

### Editing the /etc/group file
Another way to modify group information is by directly editing the `/etc/group` file. This file contains a list of all groups on the system and their associated information. You can use a text editor, such as `vi` or `nano`, to edit this file.

To modify a group, open the `/etc/group` file with your preferred text editor and locate the line containing the group information you want to change. Make the necessary modifications and save the file.

Note: Be cautious when editing system files, as any mistakes can lead to system stability issues.

## Managing Group Memberships
Group memberships determine which users have access to group resources and permissions. As a Red Hat Certified Systems Administrator, it is crucial to know how to add or remove users from groups.

### Adding Users to a Group
To add a user to a group, we will use the `usermod` command with the `-aG` option. The syntax for this command is as follows:

`usermod -aG group_name user_name`

Let's break down the command:

- `usermod`: This is the command used to modify a user's information.
- `-aG`: This option appends the user to the specified group without removing any existing group memberships.
- `group_name`: This is the name of the group you want to add the user to.
- `user_name`: This is the name of the user you want to add to the group.

To add the user "John" to the "marketing" group, we would use the following command:

`usermod -aG marketing John`

### Removing Users from a Group
To remove a user from a group, we will use the `deluser` command. The syntax for this command is as follows:

`deluser user_name group_name`

Let's break down the command:

- `deluser`: This is the command used to remove a user from a group.
- `user_name`: This is the name of the user you want to remove from the group.
- `group_name`: This is the name of the group you want to remove the user from.

To remove the user "Jane" from the "human_resources" group, we would use the following command:

`deluser Jane human_resources`

## Conclusion
In this tutorial, we covered the Red Hat Certified Systems Administrator Exam 200 objective of creating, deleting, and modifying local groups and group memberships. You should now have a good understanding of how to manage group access in your Linux system using commands such as `groupadd`, `groupdel`, `groupmod`, and `usermod`. It is essential to regularly review and maintain group memberships to ensure proper access control in your system. 