# Tech Tutorial: Managing Users and Groups on RHEL

## Introduction

In this tutorial, we will focus on how to manage users and groups on a Red Hat Enterprise Linux (RHEL) system. This is a crucial skill for any Red Hat Certified System Administrator (RHCSA), as it involves basic security and user management tasks that are foundational in system administration.

We will cover how to add, delete, and modify users and groups, and how to configure filesystem permissions based on those users and groups. This tutorial will strictly adhere to RHEL-specific commands and configurations.

## Step-by-Step Guide

### 1. Managing Users in RHEL

#### Adding a New User

To add a new user in RHEL, use the `useradd` command. Here's how you can create a new user named `john`:

```bash
sudo useradd john
```

After adding the user, it's common to set a password:

```bash
sudo passwd john
```

You will be prompted to enter and confirm the password.

#### Modifying User Attributes

To modify an existing user, use the `usermod` command. For example, to add the user `john` to a supplementary group `developers`, you would use:

```bash
sudo usermod -aG developers john
```

Here, `-aG` option adds the user to the specified group without removing him from other groups.

#### Deleting a User

To delete a user, use the `userdel` command. To remove `john` and his home directory, you would use:

```bash
sudo userdel -r john
```

The `-r` option removes the home directory associated with the user.

### 2. Managing Groups in RHEL

#### Adding a New Group

To add a new group, use the `groupadd` command:

```bash
sudo groupadd developers
```

#### Modifying Group Attributes

To modify a group, RHEL uses the `groupmod` command. For example, to rename a group:

```bash
sudo groupmod -n newname oldname
```

#### Deleting a Group

To delete a group, use the `groupdel` command:

```bash
sudo groupdel developers
```

### 3. Configuring Filesystem Permissions

#### Changing File Ownership

To change the owner of a file, use the `chown` command. For instance, to change the owner of `file.txt` to user `john`:

```bash
sudo chown john file.txt
```

To change both the owner and the group of a file:

```bash
sudo chown john:developers file.txt
```

#### Changing File Permissions

RHEL uses the `chmod` command to change file permissions. For example, to give the owner of `script.sh` execute permission:

```bash
sudo chmod u+x script.sh
```

To set read, write, and execute permissions for the owner, and read and execute permissions for the group and others:

```bash
sudo chmod 755 script.sh
```

### 4. Special Permissions

#### SetUID, SetGID, and Sticky Bit

- **SetUID**: If set on an executable file, allows the file to be executed with the privileges of the file owner.

  ```bash
  sudo chmod u+s /usr/bin/script
  ```

- **SetGID**: If set on a directory, files created within the directory inherit their group from the directory, not the user.

  ```bash
  sudo chmod g+s /data/docs
  ```

- **Sticky Bit**: Often set on directories to restrict file deletion. Users can only delete files they own.

  ```bash
  sudo chmod o+t /tmp
  ```

## Conclusion

Managing users and groups effectively is essential for maintaining the security and organization of a RHEL system. By mastering these commands, you are well on your way to becoming proficient in RHEL administration. Practice these commands, understand their implications, and you'll be prepared for managing real-world RHEL environments, as well as for the RHCSA exam.