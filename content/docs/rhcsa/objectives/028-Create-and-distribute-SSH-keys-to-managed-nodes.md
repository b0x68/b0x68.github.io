# Tech Tutorial: Configure Ansible Managed Nodes

Managing multiple servers efficiently in a network can be a daunting task. Ansible, an open-source tool, simplifies this process through automation. In this tutorial, we'll focus on a key aspect of setting up Ansible for managing nodes: creating and distributing SSH keys.

## Introduction

In the context of Ansible, the control machine manages nodes over SSH. For seamless and secure operations, Ansible uses SSH keys instead of passwords. This method enhances security and efficiency as it eliminates the need for manual password entry.

This tutorial is tailored for RHEL (Red Hat Enterprise Linux) systems, aligning with the Red Hat Certified Systems Administrator (RHCSA) exam requirements.

## Prerequisites

- A RHEL control machine (Ansible installed).
- One or more RHEL managed nodes.
- Sudo privileges on all machines.

## Step-by-Step Guide

### Step 1: Install Ansible on the Control Machine

Before setting up SSH keys, ensure Ansible is installed on your control machine:

```bash
sudo dnf install ansible
```

### Step 2: Create SSH Key Pair

On the control machine, generate an SSH key pair:

```bash
ssh-keygen -t rsa -b 4096 -C "ansible automation key"
```

Press `Enter` to accept the default file location and passphrase (optional but recommended for additional security).

### Step 3: Copy the SSH Public Key to Managed Nodes

Now, distribute the public key to each managed node. This can be done using the `ssh-copy-id` command. Replace `your_managed_node_ip` with the IP address of your managed node:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub your_username@your_managed_node_ip
```

Enter the user's password when prompted. This step will append the control machine’s public key to the managed node’s `~/.ssh/authorized_keys` file, allowing passwordless SSH access.

### Step 4: Test SSH Connection

To verify that you can SSH into the managed node without a password, try the following command:

```bash
ssh your_username@your_managed_node_ip
```

If setup correctly, you should log in without being prompted for a password.

### Step 5: Configure Ansible Inventory

Create or edit your Ansible inventory file, usually located at `/etc/ansible/hosts`. Add the managed nodes under a group:

```ini
[managed_nodes]
node1 ansible_host=your_managed_node_ip ansible_user=your_username
```

### Step 6: Test Ansible Communication

Run a simple Ansible command to check if Ansible can communicate with the managed node:

```bash
ansible managed_nodes -m ping
```

You should receive a `SUCCESS` message, indicating that Ansible is able to interact with the managed node using SSH keys.

## Detailed Code Examples

Here’s a comprehensive example of the inventory file setup and a test playbook to verify everything is configured correctly:

**Inventory File (`/etc/ansible/hosts`):**

```ini
[managed_nodes]
node1 ansible_host=192.168.1.10 ansible_user=ec2-user
node2 ansible_host=192.168.1.11 ansible_user=ec2-user
```

**Test Playbook (`check_ssh.yml`):**

```yaml
---
- name: Test SSH Key Configuration
  hosts: managed_nodes
  gather_facts: no

  tasks:
    - name: Ping Test
      ping:
```

Run the playbook:

```bash
ansible-playbook check_ssh.yml
```

## Conclusion

Setting up SSH keys for Ansible not only streamlines the management of multiple RHEL systems but also reinforces security protocols by eliminating the need for password-based authentications. Following this guide will ensure you are well-prepared to manage your infrastructure effectively using Ansible, aligning with RHCSA exam objectives.

As you expand your Ansible use, consider exploring more complex playbooks and roles to fully leverage Ansible’s capabilities in your environment.