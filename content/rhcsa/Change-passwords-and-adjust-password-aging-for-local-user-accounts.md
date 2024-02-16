+++
title = "Change passwords and adjust password aging for local user accounts"
date = "2024-02-16T10:36:45-05:00"
author = "root"
cover = ""
tags = ["system", "systems", "user's", "`/etc/default/useradd`", "passwords:", "user", "log", "passwords"]
keywords = ["`/etc/default/useradd`", "security", "`password", "user.", "passwords.", "amount", "file", "`/etc/pam.d/system-auth`"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Change Passwords and Adjust Password Aging for Local User Accounts

## Introduction

In this tutorial, we will cover one of the objectives of the Red Hat Certified Systems Administrator (RHCSA) Exam 200: Change passwords and adjust password aging for local user accounts. This knowledge is crucial for any administrator who wants to ensure the security of their system by managing user passwords effectively.

## Prerequisites

Before we begin, it is assumed that you have a basic understanding of the Linux command line and user management. This tutorial will be focused on Red Hat Enterprise Linux (RHEL) system, but the concepts can be applied to any Linux distribution.

## Step 1: Changing User Passwords

The first step in managing passwords for local user accounts is to change the default passwords. This is important because default passwords are usually well-known and can be a security vulnerability. To change a user's password, follow these steps:

1. Log into the system as the root user.
2. Use the `passwd` command followed by the username to change the password for that user. For example: `passwd username`
3. You will be prompted to enter the new password and confirm it by entering it again.
4. Once the password is changed, you will receive a confirmation message.

## Step 2: Setting Password Expiration

To ensure the security of the system, it is important to enforce password expiration for user accounts. This means that the password will expire after a certain amount of time and users will be required to change it. To set password expiration, follow these steps:

1. Log into the system as the root user.
2. Use the `chage` command followed by the username to view and modify password expiration settings for that user. For example: `chage -l username`
3. You will see information about the user's password aging, including the password expiration date and the number of days before the password expires.
4. To set a specific password expiration date, use the `-E` flag followed by the date in the format MM/DD/YY. For example: `chage -E 05/01/21 username`
5. To set the number of days before the password expires, use the `-M` flag followed by the number of days. For example: `chage -M 90 username`

## Step 3: Enforcing Strong Passwords

Another important aspect of managing local user passwords is to enforce strong password policies. This helps to prevent users from setting weak passwords that are easily guessable. To enforce strong passwords, follow these steps:

1. Log into the system as the root user.
2. Edit the `/etc/pam.d/system-auth` file using a text editor such as `vi` or `nano`.
3. Look for the line that starts with `password requisite pam_cracklib.so`. This line specifies the parameters for password complexity requirements.
4. Add or modify the following parameters to enforce strong passwords:
  - `minlen` - sets the minimum length for passwords.
  - `dcredit` - sets the minimum number of digits required in the password.
  - `ucredit` - sets the minimum number of uppercase letters required in the password.
  - `ocredit` - sets the minimum number of special characters required in the password.
  - `lcredit` - sets the minimum number of lowercase letters required in the password.

## Step 4: Disabling Inactive User Accounts

To ensure the security of the system, it is important to disable inactive user accounts. These are accounts that have not been used for a set period of time and could potentially be a security risk. To disable inactive user accounts, follow these steps:

1. Log into the system as the root user.
2. Edit the `/etc/default/useradd` file using a text editor such as `vi` or `nano`.
3. Look for the line that starts with `INACTIVE=`. This line specifies the number of days before a user account is disabled due to inactivity.
4. Set the value to the desired number of days, or `0` to disable the feature completely.
5. Save the changes and exit the editor.

## Conclusion

In this tutorial, we have covered the Red Hat Certified Systems Administrator Exam 200 objective: Change passwords and adjust password aging for local user accounts. By following these steps, you should now have a good understanding of how to effectively manage user passwords on your system to enhance its security. 

Remember to regularly change passwords, set password expiration, enforce strong passwords, and disable inactive user accounts to minimize potential security risks. Good luck on your RHCSA exam!