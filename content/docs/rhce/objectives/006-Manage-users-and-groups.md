# Tech Tutorial: Manage Users and Groups on Red Hat Enterprise Linux (RHEL)

## Introduction
In this tutorial, we will delve into the essential task of managing users and groups on a Red Hat Enterprise Linux (RHEL) system, a fundamental skill for any Red Hat Certified System Administrator (RHCSA). Effective user and group management ensures proper security and accessibility controls are in place, which is critical for maintaining the integrity and functionality of the system.

We will cover how to create, modify, delete users and groups, and also how to configure file permissions associated with these users and groups to ensure secure access to system files and resources.

## Step-by-Step Guide

### 1. Managing Users

#### a. Creating a New User
To create a new user in RHEL, you use the `useradd` command. Here’s the basic syntax:

```bash
useradd [options] username
```

**Example:**
```bash
useradd johndoe
```

This command creates a new user named `johndoe` with default settings. To specify additional options such as the home directory or the shell, you can use:

```bash
useradd -d /home/johndoe -s /bin/bash johndoe
```

#### b. Modifying a User
To modify an existing user, use the `usermod` command. It is similar to `useradd` but used for modifying the existing users.

**Example:**
```bash
usermod -s /bin/csh johndoe
```

This changes the default shell for `johndoe` to C shell (`/bin/csh`).

#### c. Deleting a User
To delete a user, the `userdel` command is used. You can also remove the home directory and mail spool by using the `-r` option.

**Example:**
```bash
userdel -r johndoe
```

### 2. Managing Groups

#### a. Creating a Group
To create a new group, use the `groupadd` command.

**Example:**
```bash
groupadd developers
```

This command creates a new group named `developers`.

#### b. Modifying a Group
To modify an existing group, you use the `groupmod` command.

**Example:**
```bash
groupmod -n devteam developers
```

This renames the group from `developers` to `devteam`.

#### c. Deleting a Group
To delete a group, use the `groupdel` command.

**Example:**
```bash
groupdel devteam
```

### 3. Managing User and Group Relationships

#### a. Adding a User to a Group
To add a user to a group, use the `usermod` command with the `-G` option.

**Example:**
```bash
usermod -aG developers johndoe
```

This adds `johndoe` to the `developers` group.

#### b. Removing a User from a Group
To remove a user from a group, you will need to edit the `/etc/group` file manually or use a tool like `gpasswd`.

**Example:**
```bash
gpasswd -d johndoe developers
```

This removes `johndoe` from the `developers` group.

### 4. Setting Permissions

The `chmod` (change mode) command is used to change the file access permissions.

#### a. Granting File Permissions
To give read, write, and execute permissions to the user and group, while keeping read-only access for others:

**Example:**
```bash
chmod 774 example.txt
```

#### b. Changing File Ownership
The `chown` command changes the user and/or group ownership of a given file.

**Example:**
```bash
chown johndoe:developers example.txt
```

This changes the ownership of `example.txt` to user `johndoe` and group `developers`.

## Conclusion

Managing users and groups is a critical task for system administrators. This guide provides you with the necessary commands and examples to effectively manage users and groups on a RHEL system. Mastery of these commands ensures you can maintain proper security and operational efficiency in your Linux environments.