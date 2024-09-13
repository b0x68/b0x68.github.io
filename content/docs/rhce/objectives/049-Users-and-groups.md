# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for User and Group Management

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and repetitive jobs. In this tutorial, we will focus on automating common Red Hat Certified System Administrator (RHCSA) tasks pertaining to users and groups management using Ansible. Specifically, this will help in preparing for the Red Hat Certified Engineer (RHCE) exam, where proficiency in these areas is required.

## Prerequisites

Before diving into the tutorial, ensure you have the following setup:

- **Ansible installed** on a control node (e.g., your workstation).
- One or more managed nodes running **RHEL 7 or RHEL 8**.
- **SSH access** configured between the control node and the managed nodes.
- **Sudo privileges** for the user on managed nodes.

## Step-by-Step Guide

This guide will cover the following tasks:
1. Installing Ansible on RHEL
2. Configuring Ansible
3. Creating a playbook to manage users and groups

### Step 1: Installing Ansible on RHEL

First, ensure that the EPEL repository is enabled on your RHEL system:

```bash
sudo subscription-manager repos --enable rhel-7-server-optional-rpms  # For RHEL 7
sudo subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms  # For RHEL 8
```

Install Ansible using YUM:

```bash
sudo yum install ansible -y
```

### Step 2: Configuring Ansible

Create a directory for your Ansible projects and set up an inventory file:

```bash
mkdir ~/ansible-projects
cd ~/ansible-projects
echo "[rhel-servers]" > hosts
echo "192.168.1.100" >> hosts  # Replace with your managed node's IP
```

Test the connection to your managed node:

```bash
ansible all -m ping -i hosts
```

### Step 3: Creating a Playbook to Manage Users and Groups

Create a playbook named `user_group_mgmt.yml`:

```yaml
---
- name: Manage Users and Groups
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Ensure group "developers" exists
      ansible.builtin.group:
        name: developers
        state: present

    - name: Create user "john_doe"
      ansible.builtin.user:
        name: john_doe
        comment: "John Doe"
        uid: 1040
        group: developers

    - name: Ensure user "jane_doe" is removed
      ansible.builtin.user:
        name: jane_doe
        state: absent
```

#### Detailed Code Examples

**1. Managing Groups:**

The `ansible.builtin.group` module manages groups on the managed host.

```yaml
- name: Ensure group "developers" exists
  ansible.builtin.group:
    name: developers
    state: present
```

**2. Managing Users:**

The `ansible.builtin.user` module manages user accounts.

```yaml
- name: Create user "john_doe"
  ansible.builtin.user:
    name: john_doe
    comment: "John Doe"
    uid: 1040
    group: developers
```

To remove a user, set `state: absent`.

```yaml
- name: Ensure user "jane_doe" is removed
  ansible.builtin.user:
    name: jane_doe
    state: absent
```

### Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook -i hosts user_group_mgmt.yml
```

## Conclusion

In this tutorial, we explored how to automate user and group management tasks on RHEL using Ansible. This automation not only helps in reducing manual errors but also ensures consistency across multiple systems, making it an essential skill for the RHCE exam. By mastering these tasks, you can significantly streamline system administration in RHEL environments.