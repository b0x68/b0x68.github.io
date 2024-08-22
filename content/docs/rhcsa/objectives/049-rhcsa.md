# Tech Tutorial: Manage Users and Groups - Password Management

## Introduction

In the realm of system administration, managing user credentials is fundamental to securing access to the system. This tutorial will specifically focus on how to change passwords and adjust password aging for local user accounts on a Linux system. These operations are crucial for maintaining strong security policies and ensuring that users' credentials are regularly updated to prevent unauthorized access.

## Prerequisites

Before proceeding with this tutorial, ensure you have:
- A Linux system with administrative (root) access.
- Familiarity with using the command line interface (CLI).

## Step-by-Step Guide

### 1. Changing User Passwords

To change a user's password, the `passwd` command is used. This command is straightforward and requires administrative privileges if you are changing the password for another user.

#### Syntax:
```bash
sudo passwd [username]
```

#### Example:
To change the password for a user named `john`, you would run:
```bash
sudo passwd john
```
This command will prompt you to enter a new password twice to confirm it.

### 2. Understanding Password Aging

Password aging is a security practice that forces users to change their passwords regularly. This can prevent potential unauthorized access from long-term password cracking attempts.

- **`chage`** is the command used to view and modify password aging policies.

#### Viewing Current Password Aging Information
To see the current password aging settings for a user:
```bash
sudo chage -l [username]
```

#### Example:
```bash
sudo chage -l john
```
This will display information like the last password change date, password expiration date, password inactive period, account expiration date, and more.

### 3. Modifying Password Aging

You can modify several aspects of how password aging is handled for user accounts using the `chage` command.

#### Syntax to Set Password Expiration:
```bash
sudo chage -M [max_days] [username]
```
- **`max_days`** is the maximum number of days after which the user must change the password.

#### Example:
To set the password to expire every 90 days for user `john`:
```bash
sudo chage -M 90 john
```

#### Setting Minimum Days Between Password Changes:
```bash
sudo chage -m [min_days] [username]
```
- **`min_days`** is the minimum number of days before which the user cannot change the password again.

#### Example:
To prevent user `john` from changing the password more frequently than every 10 days:
```bash
sudo chage -m 10 john
```

#### Setting a Warning Period for Password Expiration:
```bash
sudo chage -W [warn_days] [username]
```
- **`warn_days`** is the number of days before password is going to expire during which the user is warned.

#### Example:
To set a 7-day warning period for user `john`:
```bash
sudo chage -W 7 john
```

### 4. Automating Password Policy Updates

For environments with many users, it's practical to automate the setting of password policies. Below is a simple script that updates password policies for all users in a specific group.

#### Example Script:
```bash
#!/bin/bash

# Define the group name
GROUP="staff"

# Loop through all users in the group
for USER in $(members $GROUP); do
  echo "Updating password policy for $USER"
  sudo chage -M 90 -m 10 -W 7 $USER
done
```
This script sets the password to expire every 90 days, prevents changes more frequently than every 10 days, and sets a 7-day warning period.

## Conclusion

Managing password policies and aging is essential for maintaining a secure and efficient system environment. By using the `passwd` and `chage` commands, system administrators can ensure that user accounts adhere to security best practices. Regular updates and audits of these policies are recommended to adapt to any new security threats or organizational changes. Remember, keeping your systems secure is an ongoing process and requires continuous attention.