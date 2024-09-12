# Tech Tutorial: Install and Configure an Ansible Control Node

In this tutorial, we will focus on setting up an Ansible control node and creating a static host inventory file as part of the preparation for the Red Hat Certified Systems Administrator (RHCSA) exam. Ansible is a powerful automation tool that simplifies complex configuration tasks and system administration processes.

## Introduction

Ansible is an open-source automation tool that offers simplicity and flexibility for managing various types of operations such as configuration management, application deployment, task automation, and orchestration. One of the fundamental components of Ansible is the inventory file, which contains information about the hosts you manage. We'll cover how to set up Ansible on a Red Hat Enterprise Linux (RHEL) system and configure a static host inventory file.

## Prerequisites

- A RHEL 8 system set up as the Ansible control node.
- One or more managed nodes (these can be RHEL or any other server accessible over SSH).
- Root or sudo privileges on the control node.

## Step-by-Step Guide

### Step 1: Installing Ansible on RHEL

1. **Enable the EPEL Repository:**
   Before installing Ansible, you need to enable the EPEL (Extra Packages for Enterprise Linux) repository, as Ansible is part of this repository on RHEL systems.

   ```bash
   sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   ```

2. **Install Ansible:**
   Once the EPEL repository is enabled, you can install Ansible using the following command:

   ```bash
   sudo dnf install ansible -y
   ```

3. **Verify Installation:**
   Check that Ansible has been installed correctly by running:

   ```bash
   ansible --version
   ```
   This command will display the Ansible version and some configuration details.

### Step 2: Configuring SSH Access

1. **Set Up SSH Keys (on the control node):**
   To allow Ansible to communicate securely with the managed nodes, set up SSH key-based authentication.

   ```bash
   ssh-keygen -t rsa -b 2048
   ```

2. **Copy the Public Key to Managed Nodes:**
   Use the `ssh-copy-id` command to copy your public key to each managed node.

   ```bash
   ssh-copy-id user@managed-node-ip
   ```

### Step 3: Creating a Static Host Inventory File

1. **Create the Inventory Directory and File:**
   It's a good practice to keep your inventory file organized in a specific directory.

   ```bash
   sudo mkdir -p /etc/ansible/inventory
   sudo touch /etc/ansible/inventory/hosts
   ```

2. **Edit the Inventory File:**
   Open the newly created `hosts` file with your preferred text editor, such as `vi`.

   ```bash
   sudo vi /etc/ansible/inventory/hosts
   ```

3. **Add Hosts to the Inventory File:**
   In the inventory file, you can group hosts and specify individual host details. Here’s an example of what the file might look like:

   ```ini
   [web_servers]
   web1.example.com
   web2.example.com

   [db_servers]
   db1.example.com ansible_ssh_user=dbadmin ansible_ssh_private_key_file=/path/to/key

   [all:vars]
   ansible_python_interpreter=/usr/bin/python3
   ```

   - `[web_servers]` and `[db_servers]` are groups containing different servers.
   - `ansible_ssh_user` and `ansible_ssh_private_key_file` are optional parameters to specify connection details.

### Step 4: Testing the Configuration

1. **Ping the Managed Nodes:**
   Use the ansible `ping` module to check if the control node can communicate with the managed nodes.

   ```bash
   ansible all -i /etc/ansible/inventory/hosts -m ping
   ```

## Conclusion

You now have a basic Ansible control node setup and a static host inventory file configured on your RHEL system. This setup is crucial for managing and automating tasks across multiple servers efficiently. As you prepare for the RHCSA exam, continue to explore Ansible’s capabilities and experiment with more complex playbooks and configurations.

Remember, mastering Ansible can significantly streamline your system administration tasks and enhance your capabilities as a systems administrator in Red Hat environments.