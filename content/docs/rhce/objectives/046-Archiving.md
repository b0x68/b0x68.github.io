# Automate Archiving Tasks in RHEL with Ansible

## Introduction

In this tutorial, we will explore how to automate archiving tasks in a Red Hat Enterprise Linux (RHEL) environment using Ansible. Archiving is a critical activity for managing file systems and backups, ensuring that data is safely stored and recoverable. Ansible, an open-source automation tool, provides an efficient way to handle these tasks across multiple systems, saving time and reducing human error.

The focus will be on using Ansible modules specifically designed for archiving purposes on RHEL systems, adhering to the Red Hat Certified Engineer (RHCE) exam objectives.

## Prerequisites

- A RHEL 8 server or VM for testing.
- Ansible installed on a control node (can be the RHEL server itself or another machine).
- SSH access configured between the Ansible control node and the RHEL server.

## Step-by-Step Guide

### Step 1: Setting Up Ansible

First, ensure that Ansible is installed on your control node. You can install Ansible on a RHEL system using the following command:

```bash
sudo dnf install ansible
```

Next, configure the hosts file (`/etc/ansible/hosts`) to include the RHEL server:

```ini
[rhel-servers]
rhel-server-ip ansible_ssh_user=rhel-user
```

### Step 2: Create an Ansible Playbook for Archiving

Create a YAML file for your playbook, for example, `archive_files.yml`. This playbook will define tasks to archive certain directories or files on your RHEL server.

```yaml
---
- name: Archive tasks on RHEL servers
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Install zip and unzip packages
      yum:
        name:
          - zip
          - unzip
        state: present

    - name: Archive /etc directory
      ansible.builtin.archive:
        path: /etc
        dest: /tmp/etc_backup.zip
        format: zip
        owner: root
        group: root
        mode: '0644'
```

This playbook performs two main tasks:
1. Installs the `zip` and `unzip` packages, which are necessary for creating and managing zip files.
2. Uses the `ansible.builtin.archive` module to compress the `/etc` directory into a zip file named `etc_backup.zip`, storing it in `/tmp`.

### Step 3: Run the Playbook

Execute the playbook by running the following command from your control node:

```bash
ansible-playbook archive_files.yml
```

### Step 4: Verify the Archive

SSH into your RHEL server and check that the `/tmp/etc_backup.zip` file exists and contains the expected data:

```bash
ssh rhel-user@rhel-server-ip
unzip -l /tmp/etc_backup.zip
```

This command lists the contents of the zip file without extracting them, allowing you to verify its contents.

## Detailed Code Examples

The key part of the playbook is the use of the `ansible.builtin.archive` module. Here's a deeper look at the options used:

- `path`: Specifies the directory or file to archive. Multiple paths can be provided as a list.
- `dest`: The destination path where the archive should be created.
- `format`: Type of the archive (`zip`, `tar`, etc.).
- `owner`, `group`, `mode`: Set ownership and permissions of the archive file.

## Conclusion

Automating archiving tasks using Ansible not only simplifies the process but also ensures consistency and reliability across multiple RHEL systems. By leveraging the `ansible.builtin.archive` module, RHEL system administrators can efficiently manage backups and data preservation strategies. As you continue to use Ansible for various system administration tasks, you'll discover more ways to enhance system management and operational workflows.