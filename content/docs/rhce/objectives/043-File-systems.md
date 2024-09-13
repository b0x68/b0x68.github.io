# Automate Standard RHCSA Tasks Using Ansible for File Systems

## Introduction

File system management is a critical skill for system administrators, especially those preparing for the Red Hat Certified System Administrator (RHCSA) exam. In this tutorial, we will focus on automating file system tasks using Ansible, a powerful automation tool that simplifies complex configuration management and application deployment.

Ansible works by connecting to your nodes and pushing out small programs, called "Ansible modules". These programs are designed to be resource models of the desired state of the system. Once they are finished running, they are removed, leaving you with a system configured as specified.

This tutorial aims to cover essential file system tasks such as creating, mounting, and managing file systems in Red Hat Enterprise Linux (RHEL) environments using Ansible.

## Prerequisites

- A working RHEL-based system (RHEL 7 or 8)
- Ansible installed on a control node (can be your workstation or a dedicated server)
- SSH access and necessary privileges on your managed nodes

## Step-by-Step Guide

### Step 1: Install Ansible on the Control Node

Before we begin, ensure that Ansible is installed on your control node. You can install Ansible on a RHEL system using the following commands:

```bash
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
sudo dnf install ansible
```

### Step 2: Configure Ansible Inventory

Create or edit your Ansible inventory file, typically located at `/etc/ansible/hosts`. Add your managed nodes under a group:

```ini
[managed_nodes]
192.168.1.100 ansible_user=rhel-user
192.168.1.101 ansible_user=rhel-user
```

Replace `192.168.1.100` and `192.168.1.101` with the IP addresses of your managed nodes and `rhel-user` with an appropriate user.

### Step 3: Create a Playbook for File System Tasks

Ansible playbooks are YAML files where you define automation tasks. Below is an example playbook that includes tasks for creating and mounting a file system.

Create a file named `filesystem_tasks.yml`:

```yaml
---
- name: File System Management
  hosts: managed_nodes
  become: yes
  tasks:
    - name: Install required packages
      yum:
        name: "{{ item }}"
        state: present
      loop:
        - xfsprogs
        - util-linux

    - name: Create a partition and a file system
      block:
        - name: Create a partition
          community.general.parted:
            device: /dev/sdb
            number: 1
            state: present
            part_end: 100%

        - name: Create XFS file system
          filesystem:
            fstype: xfs
            dev: /dev/sdb1
      when: ansible_facts['distribution'] == 'RedHat'

    - name: Create mount point
      file:
        path: /mnt/data
        state: directory
        owner: root
        group: root
        mode: '0755'

    - name: Mount the file system
      mount:
        path: /mnt/data
        src: /dev/sdb1
        fstype: xfs
        state: mounted
        opts: defaults
```

### Step 4: Run the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook filesystem_tasks.yml
```

This command will start the automation process, handling package installations, partition creation, file system creation, and mounting—all based on the tasks defined in the playbook.

## Conclusion

In this tutorial, we covered how to automate common file system tasks in a RHEL environment using Ansible. By utilizing Ansible modules such as `yum`, `community.general.parted`, `filesystem`, and `mount`, we were able to simplify complex system administration tasks, ensuring consistency and efficiency in managing file systems across multiple nodes.

Ansible provides a robust framework for automating a wide range of system administration tasks beyond what we've explored here. As you prepare for the RHCSA exam, consider expanding your Ansible playbooks to cover other essential system administration areas, enhancing both your skills and your system's manageability.