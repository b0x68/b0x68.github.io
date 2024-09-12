# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will delve into configuring privilege escalation on managed nodes using Ansible, specifically tailored for Red Hat Enterprise Linux (RHEL) environments. This is a critical skill for those preparing for the Red Hat Certified Systems Administrator (RHCSA) exam, as Ansible is a powerful tool for automation across multiple systems.

Privilege escalation in Ansible is essential when tasks require elevated permissions to execute. Typically, this is handled via the `become` directive in Ansible, which allows an ordinary user to execute commands as the `root` user or another user by leveraging privilege escalation tools such as `sudo`.

## Step-by-Step Guide

### Pre-requisites

Before we begin, ensure that you have the following set up:
- Ansible installed on a control node (Your workstation or a central management node).
- One or more RHEL 8 managed nodes.
- SSH access configured from the control node to the managed nodes.
- `sudo` privileges set up on the managed nodes for the user Ansible will use.

### 1. Configure Ansible Control Node

Firstly, make sure Ansible is installed on your control node. If it's not installed, you can install it using the following RHEL command:

```bash
sudo dnf install ansible
```

### 2. Setting Up SSH Keys

Generate an SSH key pair on the control node if you haven't already done so:

```bash
ssh-keygen
```

Copy the public key to your RHEL managed node(s):

```bash
ssh-copy-id user@managed-node-ip
```

### 3. Testing Basic Connectivity

Ensure that Ansible can communicate with your managed node:

```bash
ansible all -m ping -u user -i managed-node-ip,
```

This command should return a success message from the managed node.

### 4. Enable Privilege Escalation

In your Ansible control node, edit the `/etc/ansible/ansible.cfg` file or create a custom configuration in your working directory. Ensure that the `become` options are enabled:

```ini
[defaults]
become = true
become_method = sudo
become_user = root
become_ask_pass = false
```

### 5. Configure `sudo` on Managed Nodes

On your RHEL managed nodes, ensure that the user which Ansible uses has the necessary `sudo` privileges. Edit the `sudoers` file using:

```bash
sudo visudo
```

Add the following line to grant the user the required privileges without a password prompt:

```
username ALL=(ALL) NOPASSWD: ALL
```

Replace `username` with the actual username used by Ansible.

### 6. Creating an Ansible Playbook

Create a simple playbook to test running a command that requires root privileges:

```yaml
---
- name: Test Privilege Escalation
  hosts: all
  become: true

  tasks:
    - name: Install a package
      yum:
        name: tree
        state: present
```

Save this as `test-playbook.yml`. This playbook will install the `tree` package on the managed nodes.

### 7. Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook -i managed-node-ip, -u user test-playbook.yml
```

This command runs the playbook, connecting as 'user', and performs tasks with elevated privileges.

## Detailed Code Examples

Ensure you review the code snippets provided above for setting up SSH keys, configuring `sudo` without a password, and the Ansible playbook example. These are crucial for successfully managing privilege escalation in a controlled and secure manner.

## Conclusion

In this tutorial, you've learned how to configure privilege escalation on RHEL managed nodes using Ansible, from setting up SSH keys to creating and running a playbook with elevated privileges. Mastering these steps is essential for automating administration tasks securely and efficiently, especially in preparation for the RHCSA exam.

By understanding and implementing these configurations, you can ensure that your automated tasks run smoothly and securely across your RHEL infrastructure, leveraging the full power of Ansible for system administration.