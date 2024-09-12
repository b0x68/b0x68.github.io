# Automate Standard RHCSA Tasks Using Ansible for File Systems Management

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and repetitive administrative work. For those preparing for the Red Hat Certified System Administrator (RHCSA) exam, mastering Ansible can be a significant advantage, especially when managing file systems on Red Hat Enterprise Linux (RHEL) systems.

In this tutorial, we will explore how to use Ansible to automate various file system tasks that are part of the RHCSA exam objectives. These include creating, mounting, and managing file systems, ensuring these tasks are repeatable and less error-prone.

## Prerequisites

- A working RHEL 8 or later installation.
- Ansible installed on a control node (which could be your RHEL system or another system that can manage RHEL nodes).

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure that Ansible is installed on your control node. You can install Ansible on a RHEL system using the following command:

```bash
sudo dnf install ansible
```

Next, configure your Ansible inventory. This is typically done in the `/etc/ansible/hosts` file. Add your RHEL managed nodes under a group:

```ini
[rhel-servers]
rhel-node1 ansible_host=192.168.1.100
```

### Step 2: Creating a File System with Ansible

To manage file systems, you'll typically use the `filesystem` module in Ansible. Here is an example playbook to create an ext4 file system on a given block device.

Create a file named `create_filesystem.yml`:

```yaml
---
- name: Create Ext4 File System
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Ensure the filesystem exists on /dev/sdb1
      community.general.filesystem:
        fstype: ext4
        dev: /dev/sdb1
```

Run the playbook using:

```bash
ansible-playbook create_filesystem.yml
```

### Step 3: Mounting the File System

After creating the file system, you need to ensure it is mounted. This can be managed using the `mount` module.

Append the following task to your `create_filesystem.yml` playbook:

```yaml
    - name: Mount the filesystem
      ansible.builtin.mount:
        path: /mnt/data
        src: /dev/sdb1
        fstype: ext4
        state: mounted
```

This playbook will now create and mount the file system at `/mnt/data`.

### Step 4: Ensuring File System Mounts on Reboot

To ensure the file system is automatically mounted on reboot, you need to manage the `/etc/fstab` file. The `mount` module conveniently handles this if you specify the `state: present` and include the `dump` and `passno` options:

```yaml
    - name: Ensure the filesystem is mounted on boot
      ansible.builtin.mount:
        path: /mnt/data
        src: /dev/sdb1
        fstype: ext4
        opts: defaults
        dump: 0
        passno: 2
        state: present
```

### Step 5: Cleanup - Unmounting and Removing the File System

For completeness, here's how you would unmount and remove a file system:

```yaml
    - name: Unmount the filesystem
      ansible.builtin.mount:
        path: /mnt/data
        state: unmounted

    - name: Remove the filesystem entirely from /dev/sdb1
      community.general.filesystem:
        fstype: ext4
        dev: /dev/sdb1
        state: absent
```

## Conclusion

With Ansible, repetitive and error-prone tasks such as file system management become automated and efficient. By leveraging Ansible modules like `filesystem` and `mount`, sysadmins can ensure consistency and reliability across managed nodes, reducing manual overhead and enhancing system configuration standards.

This tutorial has covered creating, mounting, ensuring persistence across reboots, and cleaning up file systems using Ansible, aligning with RHCSA exam objectives. Mastery of these techniques will not only aid in exam preparation but also in real-world system administration tasks on RHEL systems.