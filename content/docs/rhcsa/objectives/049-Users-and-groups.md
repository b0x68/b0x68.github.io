# Tech Tutorial: Automating User and Group Management in RHEL with Ansible

## Introduction

Managing users and groups is a fundamental task for any system administrator. For Red Hat Certified System Administrator (RHCSA) candidates, understanding how to automate these tasks can significantly enhance system management efficiency and accuracy. In this tutorial, we will explore how to use Ansible, a powerful automation tool, to manage users and groups on Red Hat Enterprise Linux (RHEL).

Ansible simplifies complex configuration tasks and ensures that the environments are set up consistently every time. This tutorial will cover how to automate the creation, modification, and deletion of users and groups using Ansible modules designed specifically for these tasks.

## Prerequisites

Before proceeding with this tutorial, ensure you have the following setup:
- A RHEL 8 or later system set up for testing.
- Ansible installed on a control node (which can be your RHEL system or another system that can manage your RHEL node remotely).
- SSH access configured for the managed nodes (the RHEL systems where users and groups will be managed).
- Sudo privileges on the managed nodes for the user under which Ansible will execute commands.

## Step-by-Step Guide

### Step 1: Setting Up the Ansible Environment

First, ensure Ansible is installed on your control node. You can install Ansible on a RHEL system using the following command:

```bash
sudo dnf install ansible
```

Create an inventory file to list the RHEL nodes you intend to manage. Here is an example of what the inventory file (`hosts.ini`) might look like:

```ini
[rhel-nodes]
192.168.1.100 ansible_user=rhel_user
```

### Step 2: Creating an Ansible Playbook for User Management

An Ansible playbook is a blueprint of automation tasks, which are executed in a sequential order. Create a file named `manage_users.yml` and add the following contents to define tasks for managing users.

```yaml
---
- name: Manage Users on RHEL Systems
  hosts: rhel-nodes
  become: yes
  tasks:
    - name: Ensure user 'john_doe' is present
      ansible.builtin.user:
        name: john_doe
        comment: "John Doe User"
        uid: 1040
        group: users
        password: "{{ 'password123' | password_hash('sha512') }}"
        state: present
        createhome: yes

    - name: Ensure user 'jane_doe' is absent
      ansible.builtin.user:
        name: jane_doe
        state: absent
```

This playbook contains two tasks:
1. Creating a user `john_doe` with a specified UID and encrypted password.
2. Ensuring the user `jane_doe` is removed from the system.

### Step 3: Running the Playbook

To execute the playbook, use the following command:

```bash
ansible-playbook -i hosts.ini manage_users.yml
```

### Step 4: Managing Groups with Ansible

Add the following tasks to your playbook to manage groups:

```yaml
    - name: Ensure group 'developers' is present
      ansible.builtin.group:
        name: developers
        state: present

    - name: Add 'john_doe' to 'developers' group
      ansible.builtin.user:
        name: john_doe
        groups: developers
        append: yes
```

These tasks ensure:
1. A group called `developers` is present.
2. User `john_doe` is added to the `developers` group.

## Detailed Code Examples

Here are detailed explanations for some of the key attributes used in the playbook:

- `ansible.builtin.user`: This module manages user accounts.
- `name`: Specifies the name of the user or group.
- `state`: Defines whether the resource should be `present` or `absent`.
- `password_hash('sha512')`: Encrypts the password using SHA-512.

You can extend the playbook by adding more users, modifying user properties, or managing user removals.

## Conclusion

Ansible provides an efficient and scalable way to manage users and groups in a RHEL environment. By automating these tasks, system administrators can ensure consistency across multiple systems and reduce the potential for human error. Whether you are preparing for the RHCSA exam or looking to streamline administrative tasks, mastering Ansible for user and group management is a valuable skill.