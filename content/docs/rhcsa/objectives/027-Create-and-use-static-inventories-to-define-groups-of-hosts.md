# Tech Tutorial: Install and Configure an Ansible Control Node

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and streamlines IT workflows. It is widely used for configuration management, application deployment, and task automation. In this tutorial, we will focus on how to install and configure an Ansible control node on a Red Hat Enterprise Linux (RHEL) system. Additionally, we'll cover how to create and use static inventories to define groups of hosts, aligning with the Red Hat Certified Systems Administrator (RHCSA) exam objectives.

## Prerequisites

Before starting, ensure you have the following:
- A RHEL 8 system set up to use as the Ansible control node.
- `sudo` or root access on this system.
- One or more managed nodes (these can be RHEL or any other Linux distribution).

## Step-by-Step Guide

### Step 1: Install Ansible on RHEL

1. **Enable the EPEL repository:**
   Ansible packages are available in the Extra Packages for Enterprise Linux (EPEL) repository. Install the EPEL release package with:
   ```bash
   sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   ```

2. **Install Ansible:**
   Once the EPEL repository is enabled, you can install Ansible by running:
   ```bash
   sudo dnf install ansible
   ```

3. **Verify the installation:**
   Check the installed version of Ansible to ensure it is correctly installed:
   ```bash
   ansible --version
   ```

### Step 2: Configure SSH Access

1. **Create SSH keys (skip if already available):**
   If you do not have SSH keys, generate them using:
   ```bash
   ssh-keygen -t rsa -b 2048
   ```
   Press ENTER to accept default values.

2. **Copy the SSH key to managed nodes:**
   Use `ssh-copy-id` to copy your public key to each managed node:
   ```bash
   ssh-copy-id user@managed-node-ip
   ```
   Replace `user` with the actual username and `managed-node-ip` with the IP address of the managed node.

### Step 3: Create and Use Static Inventories

1. **Create an inventory file:**
   Ansible uses inventory files to track which hosts it can interact with. Create a file named `inventory`:
   ```bash
   nano inventory
   ```

2. **Add hosts to the inventory file:**
   Define groups and include hostnames or IP addresses. For example:
   ```ini
   [webservers]
   webserver1.example.com
   webserver2.example.com

   [dbservers]
   dbserver1.example.com
   ```

3. **Use the inventory in an Ansible command:**
   Test connectivity to all hosts using:
   ```bash
   ansible all -m ping -i inventory
   ```

### Step 4: Running Your First Ansible Commands

1. **Gather facts from all servers:**
   Use the `setup` module to collect and display detailed information about your hosts:
   ```bash
   ansible all -m setup -i inventory
   ```

2. **Execute a simple shell command:**
   For instance, check the uptime of all web servers:
   ```bash
   ansible webservers -m command -a "uptime" -i inventory
   ```

## Detailed Code Examples

Here's a more detailed example of an Ansible playbook that installs nginx on all webservers defined in your inventory:

1. **Create a playbook file:**
   ```yaml
   nano install_nginx.yml
   ```

2. **Add the following content to the playbook:**
   ```yaml
   ---
   - name: Install nginx on all web servers
     hosts: webservers
     become: yes
     tasks:
       - name: Install nginx
         dnf:
           name: nginx
           state: present
       - name: Start nginx
         systemd:
           name: nginx
           state: started
           enabled: yes
   ```

3. **Run the playbook:**
   ```bash
   ansible-playbook -i inventory install_nginx.yml
   ```

## Conclusion

In this tutorial, we covered the basics of setting up an Ansible control node on RHEL, configuring SSH for Ansible, and creating static inventories to manage different groups of hosts. We also explored running ad-hoc commands and simple playbooks. With these foundational skills, you can begin to explore more complex Ansible functions and modules to automate a wide range of tasks in your environment. Remember, practice and experimentation are key to mastering Ansible.