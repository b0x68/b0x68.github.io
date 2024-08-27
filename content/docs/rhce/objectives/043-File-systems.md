# Automate Standard RHCSA Tasks using Ansible for File Systems

## Introduction

In this tutorial, we will explore how to automate various file system-related tasks that are part of the RHCSA (Red Hat Certified System Administrator) exam objectives using Ansible. Ansible is an open-source automation tool that can be used for configuration management, application deployment, task automation, and multi-node orchestration. We'll specifically focus on managing file systems, which includes creating, mounting, and managing file permissions.

## Prerequisites

Before proceeding, ensure you have the following:

- A control node with Ansible installed. This is usually your workstation or a management server from which Ansible commands are executed.
- One or more managed nodes (servers) running a Red Hat-based distribution where you have SSH access and a user with sudo privileges.
- Basic understanding of Linux file system management and Ansible fundamentals.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

First, you need to define your managed nodes in Ansible's inventory. Create or edit an inventory file in your Ansible control node.

```ini
[fileservers]
server1.example.com
server2.example.com
```

### Step 2: Creating a Playbook for File System Tasks

A playbook in Ansible is where you define what you want to automate across your managed nodes. Here, we will create a playbook to handle file system creation and mounting.

#### Task Details:

1. **Create a new partition.**
2. **Create a filesystem on the partition.**
3. **Ensure a directory for mounting exists.**
4. **Mount the filesystem.**
5. **Set persistent filesystem mounts using fstab.**

Create a file named `filesystem.yml` and add the following content:

```yaml
---
- name: Configure File Systems on Servers
  hosts: fileservers
  become: yes  # Use sudo privileges

  tasks:
    - name: Install required packages
      yum:
        name: 
          - parted
          - e2fsprogs
        state: present

    - name: Create a new primary partition
      community.general.parted:
        device: /dev/sdb
        number: 1
        state: present
        part_type: primary
        part_start: 1MiB
        part_end: 100% 

    - name: Create a filesystem on the new partition
      filesystem:
        fstype: ext4
        dev: /dev/sdb1

    - name: Ensure the mount point directory exists
      file:
        path: /mnt/data
        state: directory

    - name: Mount the filesystem
      mount:
        path: /mnt/data
        src: /dev/sdb1
        fstype: ext4
        state: mounted

    - name: Set persistent mounting
      lineinfile:
        path: /etc/fstab
        line: "/dev/sdb1 /mnt/data ext4 defaults 0 0"
        create: yes
```

### Step 3: Running the Playbook

Execute the playbook using the following command from your control node:

```bash
ansible-playbook filesystem.yml
```

This command will communicate with the servers listed under `[fileservers]` in your inventory, and perform the tasks defined in the `filesystem.yml` playbook.

## Detailed Code Examples

In the playbook provided, each task is designed to handle specific parts of the filesystem setup:

- **Installing required packages**: Ensures that the necessary tools (`parted` for partitioning and `e2fsprogs` for creating ext filesystems) are installed.
- **Creating a partition**: Uses the `community.general.parted` module to make a new primary partition on `/dev/sdb`.
- **Creating a filesystem**: Applies the `filesystem` module to format the new partition with `ext4`.
- **Creating a mount point**: Ensures the directory for mounting the filesystem exists using the `file` module.
- **Mounting the filesystem**: Utilizes the `mount` module to mount the partition.
- **Setting up fstab**: Adds a persistent mount entry in `/etc/fstab` using the `lineinfile` module.

## Conclusion

Using Ansible to manage file systems provides a repeatable, declarative approach to server configuration. This automation ensures consistency across your infrastructure, reduces manual errors, and significantly cuts down on the time required to perform standard system administration tasks. This tutorial covered the basics, but Ansible's capabilities allow for much more complex operations and scenarios, making it a powerful tool for any system administrator's toolkit.