# Tech Tutorial: Manage Users and Groups on RHEL

## Introduction

In Red Hat Enterprise Linux (RHEL), managing users and groups is a fundamental task for system administrators. This tutorial aims to provide a comprehensive guide on how to create, delete, and modify local user accounts in RHEL. This is particularly valuable for those preparing for the Red Hat Certified System Administrator (RHCSA) exam, as it covers essential exam objectives related to user management.

## Step-by-Step Guide

### 1. Creating a New User

To create a new user in RHEL, you use the `useradd` command. This command allows you to create a new user account that users can use to log in and access the system.

#### Syntax and Options

```
useradd [options] USERNAME
```

- `USERNAME` is the name of the user to be created.

Here are some commonly used options with `useradd`:

- `-c` : Comment field, generally used for the full name of the user.
- `-d` : Home directory for the user.
- `-m` : Create the user's home directory if it does not exist.
- `-s` : Default shell for the user.

#### Example:

```bash
sudo useradd -c "John Doe" -d /home/johndoe -m -s /bin/bash johndoe
```

This command creates a new user named `johndoe`, with a home directory `/home/johndoe`, and the default shell set to `/bin/bash`.

### 2. Setting or Changing a User’s Password

After creating a user, set the user's password using the `passwd` command.

#### Syntax

```
passwd USERNAME
```

#### Example:

```bash
sudo passwd johndoe
```

You will be prompted to enter and confirm the new password.

### 3. Modifying an Existing User

To modify an existing user, use the `usermod` command. This is useful for changing user details such as the user's login name, home directory, or shell.

#### Syntax and Options

```
usermod [options] USERNAME
```

Some options for `usermod` include:

- `-l` : New login name for the user.
- `-d` : New home directory for the user.
- `-m` : Move the contents from the user's current directory to the new directory.
- `-s` : New login shell for the user.

#### Example:

```bash
sudo usermod -l johnnew -d /home/johnnew -m -s /bin/zsh johndoe
```

This command changes `johndoe`’s username to `johnnew`, home directory to `/home/johnnew`, moves the old contents to the new directory, and changes the shell to `/bin/zsh`.

### 4. Deleting a User

To delete a user, use the `userdel` command.

#### Syntax and Options

```
userdel [options] USERNAME
```

- `-r` : Removes the user along with the user's home directory and mail spool.

#### Example:

```bash
sudo userdel -r johnnew
```

This command deletes the user `johnnew` and removes the home directory along with the mail spool.

## Detailed Code Examples

Let us create a user, modify them, and then delete them:

```bash
# Create a user
sudo useradd -c "Example User" -m -s /bin/bash exampleuser

# Set user password
sudo passwd exampleuser

# Modify the user
sudo usermod -l newexampleuser -d /home/newexampleuser -m exampleuser

# Delete the user
sudo userdel -r newexampleuser
```

## Conclusion

In this tutorial, we've covered how to manage users and groups on RHEL, focusing on creating, modifying, and deleting user accounts. These operations form the backbone of system administration and are crucial for anyone preparing for the RHCSA exam. With the commands and examples provided, you should be well-prepared to handle user management tasks on a RHEL system.