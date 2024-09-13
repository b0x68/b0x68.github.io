# Tech Tutorial: Manage Users and Groups – Changing Passwords and Adjusting Password Aging for Local User Accounts

## Introduction

In this tutorial, we will cover how to manage user passwords and set password aging policies on Red Hat Enterprise Linux (RHEL). This is a crucial skill for system administrators, as it helps in maintaining security and compliance in Linux environments. Managing passwords and password policies effectively can protect against unauthorized access and ensure that user credentials are periodically updated.

## Step-by-Step Guide

### 1. Changing User Passwords

To change a user's password in RHEL, you use the `passwd` command. This command is used by both administrators and users to change passwords.

#### Syntax:
```bash
passwd [options] [user]
```

#### Example: Changing a Password for a User

If you are logged in as a root user and need to change the password for another user, you would use the following command:

```bash
sudo passwd username
```

Replace `username` with the actual user's username. You will be prompted to enter and confirm the new password.

### 2. Understanding Password Aging

Password aging is a policy used to manage how often users must change their passwords. It can help improve system security by enforcing regular password updates.

### 3. Checking Password Aging Information

To check the current password aging information for a user, use the `chage` command with the `-l` option.

#### Syntax:
```bash
chage -l username
```

#### Example: Viewing Password Aging for a User

```bash
chage -l johndoe
```

This command will display password aging information for the user `johndoe`, such as the last password change date, password expiry date, and warning days.

### 4. Setting Password Aging Policies

The `chage` command is also used to modify password aging policies.

#### Syntax:
```bash
chage [options] username
```

#### Options Include:
- `-m`: Set the minimum number of days between password changes.
- `-M`: Set the maximum number of days the password is valid.
- `-W`: Set the number of days of warning before a password change is required.

#### Example: Setting Minimum and Maximum Days for Password Changes

To enforce that the user `johndoe` must change his password at least every 90 days and not more frequently than every 7 days, use:

```bash
sudo chage -m 7 -M 90 johndoe
```

To setup a warning 10 days before the password expires:

```bash
sudo chage -W 10 johndoe
```

### 5. Enforcing Password Expiration

If you want to immediately expire a password to force a user to change it at the next login, you can use:

```bash
sudo chage -d 0 username
```

This sets the last password change to the day zero (01/01/1970), effectively expiring the password.

#### Example: Forcing a Password Change on Next Login

```bash
sudo chage -d 0 johndoe
```

This command requires `johndoe` to change his password the next time he logs in.

## Detailed Code Examples

Let's consider a scenario where you need to set up a new user and configure password policies suitable for a secure environment:

```bash
# Add a new user
sudo useradd alice

# Set an initial password
sudo passwd alice

# Set password aging requirements: change every 60 days, minimum 7 days, warn 15 days before expiration
sudo chage -m 7 -M 60 -W 15 alice

# Check the password aging setup
chage -l alice
```

This script automates the process of adding a user and setting secure password policies.

## Conclusion

In this tutorial, we have explored how to change user passwords and manage password aging policies on RHEL. These operations are fundamental for system administrators to ensure the security and proper management of user accounts. Regularly updating these policies and monitoring user compliance can significantly enhance your system's security posture.

Remember, managing passwords and password policies is a continuous process and should be part of your regular system administration duties.