# Tech Tutorial: Manage Users and Groups on Linux Systems

## Introduction

In Linux systems, managing user accounts and groups is a fundamental administrative task that ensures the right users have the correct access privileges to the system and its resources. This tutorial will guide you through creating, deleting, and modifying local user accounts on a Linux machine. Understanding these operations is crucial for system administrators, especially those preparing for Linux administration certifications.

## Step-by-Step Guide

### Prerequisites

- A Linux machine (any distribution like Ubuntu, CentOS, etc.)
- Access to a terminal or command line interface
- Sudo or root privileges

### 1. Creating a User Account

To create a new user in Linux, we use the `useradd` command. This command allows you to create a new user account that users can use to login and access the system.

#### Syntax:
```bash
sudo useradd [options] username
```

#### Example:
To create a new user named `john`, you would issue the following command:

```bash
sudo useradd john
```

#### Setting a Password:
After creating a user, set a password using the `passwd` command:

```bash
sudo passwd john
```
You will be prompted to enter a password twice for confirmation.

#### Detailed Options:
- `-m`: Create the user's home directory if it doesn't exist.
- `-s`: Specify the user's default shell.
- `-g`: Specify the primary group.
- `-G`: Specify additional groups.

#### Full Example with Options:
```bash
sudo useradd -m -s /bin/bash -g users -G sudo,adm john
sudo passwd john
```

### 2. Modifying a User Account

To modify an existing user, use the `usermod` command. It allows you to change the user's settings like username, home directory, shell, etc.

#### Syntax:
```bash
sudo usermod [options] username
```

#### Example:
To change the shell for user `john` to `/bin/zsh`:

```bash
sudo usermod -s /bin/zsh john
```

To add user `john` to additional groups `ftp` and `www-data`:

```bash
sudo usermod -aG ftp,www-data john
```

### 3. Deleting a User Account

To delete a user account, use the `userdel` command. Be careful with this command, as it can remove user data.

#### Syntax:
```bash
sudo userdel [options] username
```

#### Example:
To delete the user `john`:

```bash
sudo userdel john
```

To delete the user `john` and remove his home directory:

```bash
sudo userdel -r john
```

## Detailed Code Examples

Let's go through a real-world scenario where you need to add a user, modify their details, and eventually delete their account.

### Creating a User for a New Employee

```bash
# Adding a new user for John Doe
sudo useradd -m -s /bin/bash -g users -G sudo,adm johndoe
sudo passwd johndoe
```

### Modifying the User's Shell

Suppose the new employee prefers using `fish` shell:

```bash
# Changing shell to fish
sudo usermod -s /usr/bin/fish johndoe
```

### Deleting the User Upon Resignation

When the employee leaves the company:

```bash
# Removing user account and home directory
sudo userdel -r johndoe
```

## Conclusion

Managing user accounts is a fundamental task for system administrators. The commands `useradd`, `usermod`, and `userdel` are powerful tools that help in efficiently managing users on a Linux system. By mastering these commands, you can ensure that your system is organized and secure, with appropriate access given to the right individuals. Always remember to use these commands with caution, especially when deleting users, to avoid unintended data loss.