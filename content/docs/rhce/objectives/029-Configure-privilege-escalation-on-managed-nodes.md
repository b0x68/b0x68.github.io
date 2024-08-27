# Tech Tutorial: Configure Ansible Managed Nodes for Privilege Escalation

In this tutorial, we will cover how to configure privilege escalation on managed nodes using Ansible, a powerful automation tool that simplifies many administrative tasks. Privilege escalation is crucial in scenarios where administrative permissions are required to perform specific operations on managed nodes.

## Introduction

**Ansible** is an open-source automation tool that automates software provisioning, configuration management, and application deployment. In many environments, tasks require elevated permissions to execute commands or install software. Ansible handles this through its privilege escalation mechanism, primarily using `become` directives.

This tutorial will guide you through the process of setting up privilege escalation on Ansible managed nodes, ensuring that Ansible can execute tasks that require higher privileges.

## Prerequisites

- **Ansible installed** on a control node (the machine that manages other machines).
- At least one **managed node** (a server or machine managed by Ansible).
- **SSH access** configured between the control node and the managed node.
- **sudo privileges** for the user on the managed node.

## Step-by-Step Guide

### Step 1: Configure SSH Access

Ensure that the Ansible control node can communicate with the managed node via SSH. Typically, this involves setting up SSH keys for passwordless authentication.

1. **Generate an SSH key pair** on the control node if you haven't already:
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
2. **Copy the public key to the managed node**:
   ```bash
   ssh-copy-id user@managed-node-ip
   ```

### Step 2: Testing Basic Connectivity

Before setting up privilege escalation, confirm that Ansible can communicate with the managed node.

1. **Create an inventory file** (`hosts.ini`):
   ```ini
   [managed_nodes]
   managed-node-ip ansible_user=user
   ```

2. **Test the connection**:
   ```bash
   ansible managed_nodes -i hosts.ini -m ping
   ```

### Step 3: Configure Privilege Escalation

To run commands that require sudo privileges, update the Ansible configuration to use privilege escalation.

1. **Edit the inventory file** to include privilege escalation options:
   ```ini
   [managed_nodes]
   managed-node-ip ansible_user=user ansible_become=yes ansible_become_method=sudo ansible_become_pass='yourPassword'
   ```

2. **Alternatively, use Ansible configuration file** (`ansible.cfg`):
   ```ini
   [defaults]
   inventory = ./hosts.ini
   remote_user = user
   become = yes
   become_method = sudo
   become_ask_pass = True
   ```

### Step 4: Run Ansible Playbook with Privilege Escalation

Create a simple playbook that installs a package, demonstrating privilege escalation in action.

1. **Create a playbook** (`install_package.yml`):
   ```yaml
   ---
   - name: Install a package on a managed node
     hosts: managed_nodes
     become: yes
     tasks:
       - name: Install tree
         ansible.builtin.apt:
           name: tree
           state: present
   ```

2. **Execute the playbook**:
   ```bash
   ansible-playbook -i hosts.ini install_package.yml --ask-become-pass
   ```

## Detailed Code Examples

Here’s a more complex example that updates system packages and installs Apache on a Ubuntu managed node.

```yaml
---
- name: Update and install Apache
  hosts: all
  become: true

  tasks:
    - name: Update apt repo and cache
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install apache2
      ansible.builtin.apt:
        name: apache2
        state: latest
```

## Conclusion

Configuring privilege escalation in Ansible is essential for performing tasks that require administrative rights on managed nodes. By using the `become` directive, you can elevate privileges seamlessly and securely. This capability makes Ansible an extremely powerful tool for managing a fleet of servers or devices in any IT environment.

Remember to secure your Ansible environment, particularly when handling sensitive data like passwords. Enjoy automating with elevated privileges!