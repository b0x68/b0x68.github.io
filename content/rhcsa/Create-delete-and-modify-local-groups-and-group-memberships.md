+++
title = "Create, delete, and modify local groups and group memberships"
date = "2024-02-16T11:52:20-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: "Create, delete, and modify local groups and group memberships"

In this tutorial, we will be discussing the objective "Create, delete, and modify local groups and group memberships" from the Red Hat Certified Systems Administrator Exam 200. This objective focuses on managing local user groups and their memberships on a Red Hat Enterprise Linux system.

## Introduction
Local groups are a way to organize and manage users on a system by providing them with a common set of permissions and access to resources. Red Hat Enterprise Linux provides a robust set of tools for creating, deleting, and modifying local groups, making it easy to manage users and their access levels.

## Prerequisites
In order to follow along with this tutorial, you will need the following:
- A Red Hat Enterprise Linux system
- A user account with administrative privileges
- Basic knowledge of the Linux command-line interface

## Creating Local Groups
Local groups can be created using the `groupadd` command. This command takes the following syntax:
```
groupadd [options] group_name
```
Let's create a group called "engineers" using the `groupadd` command:
```
sudo groupadd engineers
```
This will create a new group with the name "engineers". Note that the group name must be unique and cannot already exist on the system.

## Adding Users to Groups
Now that our group has been created, we can add users to it using the `usermod` command. This command allows us to modify user accounts, including their group memberships. The syntax for adding a user to a group is as follows:
```
usermod -a -G group_name user_name
```
The `-a` flag indicates that the group should be added to the user's existing group memberships, rather than replacing them. Let's add a user named "jane" to the "engineers" group:
```
sudo usermod -a -G engineers jane
```
It is important to note that changes made to a user's group memberships will only take effect when the user logs in again.

## Viewing Group Memberships
To view the current members of a group, we can use the `members` command. This command requires the `libuser` package to be installed on the system. To install it, use the following command:
```
sudo yum install libuser
```
Once it is installed, we can use the `members` command to view the members of a group:
```
members group_name
```
In our case, to view the members of the "engineers" group, we would use the following command:
```
members engineers
```

## Modifying Group Properties
Using the `groupmod` command, we can modify the properties of a local group. This command takes the following syntax:
```
groupmod [options] group_name
```
Some common options that can be used with this command are:
- `-n`: to change the name of the group
- `-g`: to change the group's GID (Group ID number)
- `-R`: to set default shell and home directory for newly created users

Let's say we want to change the name of our "engineers" group to "developers". We would use the following command:
```
sudo groupmod -n developers engineers
```

## Deleting Local Groups
To delete a local group, we can use the `groupdel` command. The syntax for this command is simple:
```
groupdel group_name
```
For example, to delete the "developers" group, we would use the following command:
```
sudo groupdel developers
```
Note that this command will also remove the group's associated files and directories, including the group's home directory if it has one.

## Conclusion
In this tutorial, we have covered the basic commands and options for creating, modifying, and deleting local groups and group memberships on a Red Hat Enterprise Linux system. Understanding how to manage local groups and their memberships is an important skill for any Red Hat Certified Systems Administrator, as it allows for efficient and secure user management on a Linux system. 