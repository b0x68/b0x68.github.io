+++
title = "Change passwords and adjust password aging for local user accounts"
date = "2024-02-16T11:52:11-05:00"
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


# Tutorial: Changing Passwords and Adjusting Password Aging for Local User Accounts

In this tutorial, we will discuss the Red Hat Certified Systems Administrator Exam 200 objective: "Change passwords and adjust password aging for local user accounts". This objective requires knowledge of how to manage user accounts on a Red Hat Linux system, specifically the password settings. We will cover the steps to change passwords and adjust password aging for local user accounts in great depth, providing clear instructions and explanations along the way.

## Prerequisites
Before we begin, it is assumed that you have a basic understanding of Linux and the terminal. Additionally, make sure you have administrative privileges to modify user accounts on the system. Now, let's get started!

## Step 1: Check User Account Details
The first step is to check the details of the user account whose password you want to change. You can do this by using the `id` command followed by the username. For example:

```
id username
```
This command will display information about the user's groups, UID, and GID. Make note of the user's UID and GID for later use.

## Step 2: Change Password
To change the password for a local user account, we will use the `passwd` command. This command allows us to specify a new password for the user. It is important to note that only a user with administrative privileges can use this command to modify the password for another user.

To change the password, simply type the following command:

```
passwd username
```

where **username** is the name of the user whose password you want to change. You will be prompted to enter the new password twice for verification. Make sure to use a strong and secure password.

## Step 3: Verify Password Change
After changing the password, it is always a good idea to verify that it has been changed successfully. To do this, you can use the `su` command to switch to the user whose password you just changed. If you are able to log in with the new password, then it means the password has been successfully changed.

## Step 4: Adjust Password Aging
To adjust password aging for local user accounts, we will use the `chage` command. This command allows us to set and modify the expiration dates for user passwords. It is important to set password expiration dates to ensure that passwords are regularly updated for security purposes.

To view current password aging settings, use the following command:

```
chage -l username
```

This will display information about the user's password aging, including the last password change date, password expiration date, and more.

## Step 5: Set Password Expiration Date
To set a password expiration date, we will use the `-E` flag with the `chage` command. For example, to set a password expiration date of 60 days from today for the user, we would use the following command:

```
chage -E 2021-09-12 username
```

This will set the password expiration date for the user to 60 days from the current date.

## Step 6: Set Password Inactivity Period
In addition to setting an expiration date, we can also set an inactivity period for passwords using the `-I` flag with the `chage` command. This will force users to change their password after a certain number of days of inactivity. For example, to set an inactivity period of 15 days for the user, we would use the following command:

```
chage -I 15 username
```

## Step 7: Set Password Warning Days
We can also set the number of days before a password expiration date that a warning will be displayed to the user. This can be done using the `-W` flag with the `chage` command. For example, to set a warning of 7 days before the password expires, we would use the following command:

```
chage -W 7 username
```

## Step 8: Disable Password Aging
If you wish to disable password aging for a user, you can use the `-M` flag with the `chage` command. This will set the maximum number of days between password changes to unlimited. For example, if we want to disable password aging for the user, we would use the following command:

```
chage -M -1 username
```

## Conclusion
Congratulations, you have now successfully learned how to change passwords and adjust password aging for local user accounts in Red Hat Linux! These steps are essential knowledge for managing user accounts on a Linux system. Remember to regularly update passwords and adjust aging settings to ensure the security of your system. Thank you for following along with this tutorial.  