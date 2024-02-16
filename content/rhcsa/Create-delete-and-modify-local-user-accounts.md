+++
title = "Create, delete, and modify local user accounts"
date = "2024-02-16T11:52:01-05:00"
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
 #

# Tutorial: How to Create, Delete, and Modify Local User Accounts in Red Hat

In this tutorial, we will be discussing how to create, delete, and modify local user accounts in Red Hat. This is an important skill that is tested in the Red Hat Certified Systems Administrator Exam 200. By following the steps in this tutorial, you will gain a better understanding of the process and be prepared for the exam.

## Prerequisites

Before we begin, you will need to have a Red Hat system set up with administrative privileges. It is recommended to use a virtual machine for this tutorial. You will also need a basic understanding of the command line interface (CLI) and how to use it.

## Creating a Local User Account

Step 1: Log in as root or a user with administrative privileges.

Step 2: Open the terminal and type in the following command to create a new user account:

```
useradd [username]
```

Replace [username] with the desired username for the account.

Step 3: Set a password for the new account by using the 'passwd' command:

```
passwd [username]
```

Step 4: You will be prompted to provide and confirm the password for the user account.

Step 5: Next, you can set the expiry date for the user account (optional). To do this, use the 'chage' command:

```
chage -E [expiry date] [username]
```

Replace [expiry date] with the desired date in YYYY-MM-DD format.

Congratulations! You have successfully created a local user account.

## Deleting a Local User Account

Step 1: Log in as root or a user with administrative privileges.

Step 2: Open the terminal and type in the following command to delete a user account:

```
userdel [username]
```

Replace [username] with the username of the account you want to delete.

Step 3: Confirm the deletion by pressing 'y' when prompted.

## Modifying a Local User Account

Step 1: Log in as root or a user with administrative privileges.

Step 2: Open the terminal and type in the following command to modify a user account:

```
usermod [options] [username]
```

Replace [options] with the desired modifications, such as changing the username or home directory.

### Examples of common options:

- To change the username from 'user1' to 'newuser1':
```
usermod -l newuser1 user1
```

- To change the home directory from '/home/user1' to '/home/newuser1':
```
usermod -d /home/newuser1 user1
```

- To add the user to a specific group:
```
usermod -aG [groupname] [username]
```

Replace [groupname] with the name of the group you want to add the user to. You can add multiple groups by separating them with a comma.

Congratulations! You have successfully modified a local user account.

## Conclusion

In this tutorial, we have covered how to create, delete, and modify local user accounts in Red Hat. By following these steps, you should now have a better understanding of how to manage user accounts on a Red Hat system. Remember to practice these skills and read through the Red Hat documentation for further information. Good luck with your Red Hat Certified Systems Administrator Exam!