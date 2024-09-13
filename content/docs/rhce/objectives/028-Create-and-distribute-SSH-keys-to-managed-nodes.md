# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will explore how to configure Ansible managed nodes by creating and distributing SSH keys on Red Hat Enterprise Linux (RHEL). The secure management of nodes using Ansible is crucial for automation and central management tasks, which are key components of the Red Hat Certified Engineer (RHCE) exam. SSH keys provide a secure way of logging into a Linux server without the need for passwords.

## Prerequisites

- Two or more RHEL servers (one Ansible control node and at least one Ansible managed node)
- Sudo privileges on all servers

## Step-by-Step Guide

### Step 1: Install Ansible on the Control Node

First, ensure that Ansible is installed on your control node. You can install Ansible on RHEL using the following commands:

```bash
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
sudo dnf install ansible
```

### Step 2: Create SSH Key Pair on the Control Node

Log in to your Ansible control node and create an SSH key pair by running:

```bash
ssh-keygen -t rsa -b 2048
```

When prompted, you can press Enter to accept the default file location and passphrase.

### Step 3: Copy the Public Key to Managed Nodes

Now that you have an SSH key pair, the next step is to copy the public key to each managed node. You can do this using the `ssh-copy-id` utility. For each managed node, use the following command:

```bash
ssh-copy-id user@managed-node-ip
```

Replace `user` with the username on the managed node and `managed-node-ip` with the IP address of the managed node.

### Step 4: Test SSH Connection

After copying the SSH key, test the connection from the control node to each managed node to ensure that it works without requiring a password:

```bash
ssh user@managed-node-ip
```

If you do not have to enter the user's password and you successfully log in, then the SSH key was set up correctly.

### Step 5: Configure Ansible Inventory

Create or edit the Ansible inventory file in `/etc/ansible/hosts`. Add the managed nodes under a group. For example:

```ini
[managed_nodes]
192.168.1.101 ansible_user=user
192.168.1.102 ansible_user=user
```

### Step 6: Test Ansible Connectivity

Run an Ansible ad-hoc command to make sure Ansible can communicate with all managed nodes securely via SSH:

```bash
ansible managed_nodes -m ping
```

You should receive a "pong" response from each node if everything is configured correctly.

## Detailed Code Examples

Here is a comprehensive example of setting up an Ansible inventory file and running a simple playbook.

### Example Ansible Inventory (`/etc/ansible/hosts`):

```ini
[managed_nodes]
node1 ansible_host=192.168.1.101 ansible_user=user
node2 ansible_host=192.168.1.102 ansible_user=user
```

### Example Ansible Playbook (`example-playbook.yml`):

```yaml
---
- name: Test Connectivity
  hosts: managed_nodes
  tasks:
    - name: Ping Test
      ping:
```

Run the playbook using:

```bash
ansible-playbook example-playbook.yml
```

## Conclusion

In this tutorial, we covered how to configure Ansible managed nodes by creating and distributing SSH keys on a RHEL environment. This setup allows you to manage your servers more efficiently and securely without the need for manual password authentication. By following these steps, you are now equipped to expand your Ansible automation further with more complex playbooks and roles.