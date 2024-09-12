# Automate Standard RHCSA Security Tasks Using Ansible

## Introduction

In this tutorial, we will explore how to automate various security tasks on Red Hat Enterprise Linux (RHEL) systems using Ansible. This is particularly relevant for the Red Hat Certified System Administrator (RHCSA) exam, which emphasizes the practical skills in system administration, including security management. Automating these tasks can help ensure consistency, reduce errors, and save time.

Ansible is a powerful automation tool that simplifies many system administration tasks. We will focus on using Ansible modules that are specifically designed for security tasks on RHEL systems.

## Prerequisites

Before you begin, you will need:
- A control node with Ansible installed. This could be your personal workstation or a management server.
- One or more RHEL 8 machines to use as Ansible nodes.
- SSH access and appropriate privileges on the RHEL nodes.
- Basic familiarity with YAML, the format used for Ansible playbooks.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure Ansible is installed on your control node. If it's not installed, you can install it using the following command:

```bash
sudo dnf install ansible
```

Next, set up SSH key-based authentication for your Ansible nodes to allow seamless connection from the control node.

### Step 2: Creating the Inventory File

Create an inventory file in your Ansible control node. This file contains information about the hosts you intend to manage.

```ini
# inventory.ini
[rhel-nodes]
192.168.1.101
192.168.1.102
```

### Step 3: Writing Your First Security Playbook

We will create a playbook to ensure that the firewall is enabled and configured properly on all RHEL nodes.

#### 3.1 Create the playbook file:

Create a file named `secure_firewall.yml`.

```yaml
---
- name: Ensure Firewall is Configured Properly
  hosts: rhel-nodes
  become: yes
  tasks:
    - name: Ensure firewalld is installed
      yum:
        name: firewalld
        state: present

    - name: Ensure firewalld is enabled and running
      systemd:
        name: firewalld
        state: started
        enabled: yes

    - name: Open SSH port in firewalld
      firewalld:
        service: ssh
        permanent: true
        state: enabled
        immediate: yes
```

#### 3.2 Run the playbook:

Run the playbook using the following command:

```bash
ansible-playbook -i inventory.ini secure_firewall.yml
```

### Step 4: Automating User Management

Create a playbook to ensure that only authorized users are present on the system and have the correct permissions.

#### 4.1 Create the playbook file:

Create a file named `manage_users.yml`.

```yaml
---
- name: Manage Users on RHEL Nodes
  hosts: rhel-nodes
  become: true
  tasks:
    - name: Ensure a specific user is present
      user:
        name: authorized_user
        state: present
        shell: /bin/bash

    - name: Remove unauthorized users
      user:
        name: "{{ item }}"
        state: absent
      loop:
        - unauthorized_user1
        - unauthorized_user2
```

#### 4.2 Run the playbook:

```bash
ansible-playbook -i inventory.ini manage_users.yml
```

## Conclusion

In this tutorial, we have covered how to automate two crucial security tasks on RHEL systems using Ansible: configuring the firewall and managing users. By using Ansible, we can ensure that these tasks are performed consistently and efficiently across multiple systems, which is a key part of maintaining a secure and reliable IT environment.

Automation with Ansible not only helps in achieving compliance with security standards but also significantly reduces the potential for human error, making system administration more effective and secure.