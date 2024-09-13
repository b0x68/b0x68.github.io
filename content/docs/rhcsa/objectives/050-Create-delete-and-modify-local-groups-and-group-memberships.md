# Tech Tutorial: Manage Users and Groups on RHEL

Managing users and groups is a fundamental task for system administrators. In Red Hat Enterprise Linux (RHEL), this involves creating, deleting, and modifying local groups and their memberships. This tutorial is designed to help you prepare for the Red Hat Certified System Administrator (RHCSA) exam by providing detailed instructions and examples for managing users and groups on a RHEL system.

## Introduction

In RHEL, user and group management is typically handled through a set of command-line utilities. These tools allow you to add, remove, and alter user accounts and groups, as well as modify group memberships. Understanding these commands and their options is crucial for effective system administration.

### Prerequisites

- Access to a terminal on a RHEL system.
- Sudo or root privileges.

## Step-by-Step Guide

In this section, we will walk through the process of creating, deleting, and modifying local groups and managing group memberships.

### 1. Creating a Group

To create a new group, use the `groupadd` command. The basic syntax is:

```bash
sudo groupadd [options] groupname
```

**Example:**

```bash
sudo groupadd developers
```

This command creates a new group named `developers`.

### 2. Deleting a Group

To delete an existing group, use the `groupdel` command:

```bash
sudo groupdel groupname
```

**Example:**

```bash
sudo groupdel developers
```

This command deletes the group named `developers`. Be careful when deleting groups, as this cannot be undone.

### 3. Modifying a Group

To modify an existing group's attributes (such as its name), use the `groupmod` command:

```bash
sudo groupmod -n new_group_name old_group_name
```

**Example:**

```bash
sudo groupmod -n dev_team developers
```

This command renames the group `developers` to `dev_team`.

### 4. Creating a User and Adding to a Group

To add a user and simultaneously assign them to a group, use the `useradd` command with the `-G` option:

```bash
sudo useradd -G groupname username
```

**Example:**

```bash
sudo useradd -G dev_team johndoe
```

This command creates a new user `johndoe` and adds them to the `dev_team` group.

### 5. Modifying User Group Membership

To add or change a user's group membership, use the `usermod` command:

```bash
sudo usermod -aG groupname username
```

**Example:**

```bash
sudo usermod -aG project1 johndoe
```

This adds `johndoe` to the `project1` group without removing him from other groups.

### 6. Viewing Group Membership

To view the members of a group, use the `getent` command:

```bash
getent group groupname
```

**Example:**

```bash
getent group dev_team
```

This displays the group ID and the members of `dev_team`.

## Detailed Code Examples

Here are some real-world scenarios using the commands discussed:

**Scenario 1: Creating a Group for Developers**

```bash
sudo groupadd developers
echo "Group 'developers' created."
```

**Scenario 2: Deleting a Temporary Group**

```bash
sudo groupdel temp_group
echo "Temporary group 'temp_group' deleted."
```

**Scenario 3: Changing Group Name from 'test_group' to 'test_team'**

```bash
sudo groupmod -n test_team test_group
echo "Group name changed from 'test_group' to 'test_team'."
```

## Conclusion

In this tutorial, you learned how to manage users and groups in RHEL. You now know how to create, delete, and modify groups, as well as manage user memberships in groups. These skills are essential for system administration and are important for the RHCSA exam. Practice these commands to become proficient in user and group management on RHEL systems.