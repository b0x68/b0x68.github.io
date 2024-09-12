# Automate Standard RHCSA Tasks: Archiving with Ansible

## Introduction

In the Red Hat Certified Systems Administrator (RHCSA) exam, proficiency in managing files and directories, including archiving and compressing files, is essential. This tutorial focuses on automating these archiving tasks using Ansible, a powerful IT automation tool that can help system administrators manage their infrastructure more efficiently. We will explore how to use Ansible modules specifically designed for handling archiving operations in Red Hat Enterprise Linux (RHEL).

## Prerequisites

Before proceeding with this tutorial, ensure that you have the following setup:

- A RHEL 8 system set up for testing (either a VM or a physical machine).
- Ansible installed on a control node (can be the same RHEL system or a different one).
- SSH access configured from the control node to the RHEL system (if different).

## Step-by-Step Guide

### Step 1: Setting Up Ansible

First, ensure that Ansible is installed on your control node. If not already installed, you can install it using the following command:

```bash
sudo dnf install ansible
```

Next, configure Ansible to communicate with your RHEL target node. Create or edit the `/etc/ansible/hosts` inventory file to include your RHEL system:

```ini
[rhel]
192.168.1.100 ansible_user=rheluser
```

Replace `192.168.1.100` with the IP address of your RHEL system and `rheluser` with an appropriate user.

### Step 2: Creating an Ansible Playbook for Archiving

Create a new playbook named `archive_files.yml`. This playbook will demonstrate how to compress a directory, ensuring you can manage backups or archival efficiently.

```yaml
---
- name: Archive files example
  hosts: rhel
  tasks:
    - name: Ensure the directory to archive exists
      ansible.builtin.file:
        path: "/home/rheluser/data"
        state: directory

    - name: Copy example files into the directory
      ansible.builtin.copy:
        content: "Hello, this is file number {{ item }}"
        dest: "/home/rheluser/data/file{{ item }}.txt"
      loop: [1, 2, 3, 4, 5]

    - name: Archive the directory
      ansible.builtin.archive:
        path: "/home/rheluser/data"
        dest: "/home/rheluser/data/archive.zip"
        format: zip

    - name: Clean up the original files
      ansible.builtin.file:
        path: "/home/rheluser/data"
        state: absent
```

### Step 3: Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook archive_files.yml
```

This command will run the tasks defined in the playbook on the target RHEL node, which includes ensuring a directory exists, populating it with files, archiving it, and cleaning up.

## Detailed Code Examples

Let's break down the key parts of the playbook:

**Task 1: Ensure directory exists**
This task makes sure that the directory `/home/rheluser/data` is present on the system. If it doesn't exist, Ansible will create it.

**Task 2: Copy example files**
This loop creates five text files within the directory. Each file contains a simple text message.

**Task 3: Archive the directory**
The `ansible.builtin.archive` module compresses the entire `data` directory into a single zip file named `archive.zip`. You can change the format to `tar` if required.

**Task 4: Clean up**
After archiving, this task removes the original `data` directory and its contents, which simulates a move operation.

## Conclusion

Using Ansible for automating archiving tasks in a RHEL environment can significantly streamline operations, making it easier to manage file backups and transfers systematically. This tutorial gives you a foundational understanding of how you can leverage Ansible to automate typical sysadmin tasks for the RHCSA certification, focusing specifically on file archiving. Dive deeper into Ansible's documentation to explore more complex workflows and improve your automation skills.