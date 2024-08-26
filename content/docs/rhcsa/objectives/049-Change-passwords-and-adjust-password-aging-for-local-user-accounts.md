# Tech Tutorial: Manage Users and Groups – Changing Passwords and Adjusting Password Aging for Local User Accounts

## Introduction

Managing user accounts effectively is crucial for maintaining the security and operational efficiency of systems. In this tutorial, we will focus on how to change passwords and adjust password aging for local user accounts on a Linux system. Password aging is an important security measure that ensures users change their passwords periodically, thus potentially reducing the risk of unauthorized access through old or compromised passwords.

## Prerequisites

Before proceeding with this tutorial, ensure you have:
- Access to a Linux machine
- Sudo or root privileges
- Basic understanding of Linux command line interface

## Step-by-Step Guide

### 1. Changing User Passwords

To change a user's password, you can use the `passwd` command. This command allows you to update the password of any user account, provided you have the necessary administrative privileges.

#### **Example: Changing a Password for a User**

```bash
# Change password for user 'john'
sudo passwd john
```

You will be prompted to enter the new password twice to confirm it. The system will automatically update the password and inform you of the successful change.

### 2. Understanding Password Aging

Password aging is controlled in Linux through the `/etc/login.defs` file and the `chage` command. The `chage` command is used to change the number of days between required password changes and to set password expiration dates.

#### **Key Parameters in `/etc/login.defs`:**
- `PASS_MAX_DAYS` : Maximum number of days a password may be used.
- `PASS_MIN_DAYS` : Minimum number of days allowed between password changes.
- `PASS_WARN_AGE` : Number of days warning given before a password expires.

#### **Example: Viewing Default Password Aging Policies**

```bash
cat /etc/login.defs | grep -E "PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_WARN_AGE"
```

### 3. Adjusting Password Aging for a User

The `chage` command is used to modify password aging and expiration settings for user accounts.

#### **Example: Setting Password Aging Policy for User**

```bash
# Set the maximum number of days during which a password is valid
sudo chage -M 90 john

# Set the minimum number of days before which password cannot be changed
sudo chage -m 7 john

# Set the number of days of warning before a password change is required
sudo chage -W 10 john
```

#### **Detailed Example: Viewing and Setting Password Expiry Information**

To view the current password aging information for a user:

```bash
sudo chage -l john
```

To set a password to expire on a specific date:

```bash
sudo chage -E 2023-12-31 john
```

This command sets the user 'john's password to expire at the end of the year 2023.

### 4. Automating Password Expiration Checks

It's useful to regularly check and report on user accounts with expiring passwords. Here’s a simple script to help with that:

#### **Example: Check Expiring Passwords Script**

```bash
#!/bin/bash
# This script checks for all users with passwords expiring within the next 7 days.

echo "Users with expiring passwords:"
for user in $(cut -d: -f1 /etc/passwd)
do
    expiring=$(chage -l $user | grep 'Password expires' | cut -d: -f2)
    if [[ $(date -d "$expiring" +%s) -le $(date -d "+7 days" +%s) ]]; then
        echo "$user's password expires on $expiring"
    fi
done
```

Make the script executable and run it:

```bash
chmod +x check_expiring_passwords.sh
./check_expiring_passwords.sh
```

## Conclusion

In this tutorial, we covered how to change user passwords and manage password aging policies on Linux systems. Managing these settings is crucial for system security and helps in enforcing good password practices among users. Use these tools and techniques to keep your system secure and ensure that user credentials are regularly updated and managed effectively.