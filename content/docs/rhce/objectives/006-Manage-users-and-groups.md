# Tech Tutorial: Manage Users and Groups on Red Hat Systems

Managing users and groups is a fundamental task for any Red Hat Certified System Administrator (RHCSA). This tutorial will guide you through the essential commands and practices for user and group management on a Red Hat system.

## Introduction

In Linux, users and groups are used for managing permissions and controlling access to files and system resources. As an administrator, understanding how to effectively manage these entities is crucial for maintaining a secure and organized system.

## Step-by-Step Guide

This guide is divided into several sections, covering everything from creating users and groups to configuring advanced user attributes.

### 1. Creating Users

To create a new user in Red Hat, you use the `useradd` command. Here’s a basic example:

```bash
sudo useradd johndoe
```

This command creates a new user named `johndoe`. However, to make the account usable, you’ll typically want to set a password:

```bash
sudo passwd johndoe
```

You will be prompted to enter and confirm a password for the user.

#### Setting User Options

The `useradd` command has several options that can be used to customize the user’s environment. Here are a few useful ones:

- `-m`: Create a user's home directory if it does not exist.
- `-s`: Specify the default shell for the user.
- `-c`: Add a comment (usually the full name or description of the user).

Example:

```bash
sudo useradd -m -s /bin/bash -c "John Doe" johndoe
```

This command creates a new user with a home directory and bash shell, along with a description.

### 2. Modifying Users

To modify an existing user, use the `usermod` command. For example, to change the login name of a user:

```bash
sudo usermod -l newname oldname
```

To add a user to a supplementary group:

```bash
sudo usermod -aG groupname username
```

### 3. Deleting Users

To delete a user, use the `userdel` command:

```bash
sudo userdel username
```

To remove the user along with their home directory and mail spool:

```bash
sudo userdel -r username
```

### 4. Creating Groups

To create a new group:

```bash
sudo groupadd groupname
```

### 5. Modifying Groups

To modify a group, such as adding users to a group:

```bash
sudo usermod -aG groupname username
```

To change the name of a group:

```bash
sudo groupmod -n newgroupname oldgroupname
```

### 6. Deleting Groups

To delete a group:

```bash
sudo groupdel groupname
```

## Detailed Code Examples

Let's go through a scenario where we need to create a user, assign them to multiple groups, and set specific permissions.

### Scenario

Create a user named `alex`, add him to the groups `developers` and `projectx`, and give him a custom shell.

#### Step 1: Create the Groups

```bash
sudo groupadd developers
sudo groupadd projectx
```

#### Step 2: Create the User and Add to Groups

```bash
sudo useradd -m -s /bin/zsh -c "Alex Johnson" -G developers,projectx alex
```

#### Step 3: Set the Password

```bash
sudo passwd alex
```

## Conclusion

Managing users and groups is a critical skill for system administrators. By mastering the commands and options discussed in this tutorial, you’ll be well-equipped to manage access control on Red Hat systems, ensuring both security and operational efficiency.

Remember, each option and scenario might require specific adjustments, so always tailor your commands to fit your exact needs. Happy administering!