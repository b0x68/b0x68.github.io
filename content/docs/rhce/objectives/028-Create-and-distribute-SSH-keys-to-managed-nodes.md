# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration and management tasks. It uses SSH for communication between the control node and managed nodes, which means setting up SSH keys is a crucial step. This tutorial will guide you through creating and distributing SSH keys to managed nodes, enabling Ansible to interact with these nodes without requiring manual password authentication each time.

## Prerequisites

- **Ansible installed** on the control node.
- **SSH access** enabled on all managed nodes.
- **Sudo privileges** on the control node to install packages and edit configuration files.
- **User accounts** on the managed nodes that you plan to use for automation.

## Step-by-Step Guide

### Step 1: Generate SSH Keys on the Control Node

If you do not already have an SSH key pair on the control node, you'll need to generate one. SSH keys come in pairs, the private key and the public key. The private key remains on the control node, and the public key will be copied to the managed nodes.

1. Open a terminal on the control node.
2. Run the following command to generate a new SSH key pair:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "ansible-automation"
   ```
3. When prompted to "Enter a file in which to save the key," press Enter to use the default location, typically `~/.ssh/id_rsa`.
4. At the prompt, enter a secure passphrase or press Enter to create a key without a passphrase.

### Step 2: Copy the Public Key to Managed Nodes

Now that you have an SSH key pair, the next step is to copy the public key to each managed node. The `ssh-copy-id` tool can simplify this process.

1. For each managed node, use the following command, replacing `username@managed-node-ip` with the appropriate user and IP address:
   ```bash
   ssh-copy-id username@managed-node-ip
   ```
2. You may be prompted to enter the user's password for the managed node.
3. Once the password is entered, the public key will be added to the `~/.ssh/authorized_keys` file on the managed node.

### Step 3: Test SSH Access

After copying the SSH key, test the connection from the control node to each managed node to ensure that it works without prompting for a password.

1. Use the SSH command to connect to the managed node:
   ```bash
   ssh username@managed-node-ip
   ```
2. If setup correctly, you should log in to the managed node without being prompted for a password.

### Step 4: Configure Ansible to Use SSH Keys

With SSH keys configured, update your Ansible configuration to use the new keys.

1. Create or edit the Ansible hosts file, typically found at `/etc/ansible/hosts`, and add your managed nodes.
   ```ini
   [managed_nodes]
   node1 ansible_host=192.168.1.101 ansible_user=username
   node2 ansible_host=192.168.1.102 ansible_user=username
   ```
2. Optionally, define the private key file in your Ansible configuration if not using the default `~/.ssh/id_rsa`. Add this to the Ansible configuration file (`/etc/ansible/ansible.cfg`):
   ```ini
   [defaults]
   private_key_file = /path/to/your/private/key
   ```

### Step 5: Running a Test Playbook

Create a simple Ansible playbook to ensure everything is configured correctly:

1. Create a file named `test_playbook.yml`:
   ```yaml
   ---
   - name: Test Ansible SSH Keys
     hosts: managed_nodes
     tasks:
       - name: Check connectivity
         command: echo "Hello from $(hostname)"
   ```
2. Run the playbook:
   ```bash
   ansible-playbook test_playbook.yml
   ```

## Conclusion

You have successfully set up SSH keys for Ansible managed nodes, which enhances security by eliminating the need to use passwords for SSH connections. This setup not only secures your automation tasks but also streamlines processes, making Ansible an even more powerful tool for managing a network of machines efficiently.

With this foundation, you can now expand your Ansible projects, secure in the knowledge that your connections are protected. Remember, always keep your private keys secure and manage your SSH access with best practices in mind.