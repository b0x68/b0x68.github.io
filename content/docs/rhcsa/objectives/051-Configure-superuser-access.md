# Tech Tutorial: Manage Users and Groups - Configuring Superuser Access

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, one of the essential skills is managing superuser access. Superusers on Linux systems, typically known as `root`, have unrestricted access to the system. This tutorial will cover methods to configure superuser access on a Red Hat Enterprise Linux (RHEL) system, focusing on the `sudo` command, which allows specified users to execute commands with superuser privileges.

## Step-by-Step Guide

### Step 1: Understanding Root and Sudo

In RHEL, the `root` user is the default superuser account with full administrative rights to the system. However, constantly using the `root` account can be risky as it might lead to accidental system-wide changes. Instead, RHEL allows system administrators to grant limited superuser privileges to other users via the `sudo` command.

### Step 2: Installing Sudo

RHEL typically comes with `sudo` installed. If for some reason it is not installed, you can install it using the following command:

```bash
sudo yum install sudo
```

Make sure you are logged in as `root` or have root privileges to run this command.

### Step 3: Configuring the Sudoers File

The `sudo` privileges are configured in the `/etc/sudoers` file. It is crucial to use the `visudo` command to edit this file because it checks for syntax errors before saving, which can prevent configuration errors that might lock you out of root privileges.

```bash
visudo
```

### Step 4: Granting Sudo Access

To grant a user sudo access, you add them to the `sudoers` file. For instance, to allow user `john` to execute all commands as any user, you would add the following line:

```bash
john ALL=(ALL) ALL
```

Here is the breakdown:
- `john`: Username.
- `ALL`: Allow sudo access from any host.
- `(ALL)`: Allow acting as any user.
- `ALL`: Allow executing any command.

#### Example: Allowing a Group Sudo Access

Instead of adding users one by one, you can grant sudo privileges to an entire group. For example, to give all members of the group `wheel` sudo access:

```bash
%wheel ALL=(ALL) ALL
```

In RHEL, users in the `wheel` group are conventionally granted sudo privileges.

### Step 5: Using Sudo

Once a user has been granted sudo access, they can execute commands as root by prefixing them with `sudo`. For example:

```bash
sudo yum update
```

The system may prompt for the user's password, depending on the sudo configuration.

## Detailed Code Examples

### Creating a New User and Adding to the Wheel Group

Here is how you can create a new user and add them to the `wheel` group to grant them sudo access:

```bash
# Add new user
sudo useradd jane

# Set password for the new user
sudo passwd jane

# Add user to the wheel group
sudo usermod -aG wheel jane
```

### Restricting Sudo Commands

You can also restrict user commands in the sudoers file. For example, if you want to allow user `bob` only to restart the `httpd` service, you can specify:

```bash
bob ALL=(ALL) /sbin/service httpd restart
```

## Conclusion

Managing superuser access using `sudo` is a critical skill for RHEL administrators. It helps in minimizing the risks associated with the unrestricted use of the `root` account and allows for precise control over who can execute what commands. By following this guide, you should now be able to configure superuser access effectively on your RHEL systems, enhancing both security and manageability.