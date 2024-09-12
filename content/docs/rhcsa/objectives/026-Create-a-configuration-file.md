# Tech Tutorial: Install and Configure an Ansible Control Node

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and system administration activities. It is widely used for application deployment, configuration management, and continuous delivery. This tutorial will guide you through the process of installing and configuring an Ansible control node specifically on a Red Hat Enterprise Linux (RHEL) system, aligning with the Red Hat Certified System Administrator (RHCSA) exam objectives.

## Prerequisites

- A RHEL 8 system with root or sudo privileges.
- Basic familiarity with Linux command line and text editing (using vi, vim, or nano).

## Step-by-Step Guide

### Step 1: Install Ansible on RHEL

1. **Enable the EPEL Repository**

   Before installing Ansible, you need to enable the Extra Packages for Enterprise Linux (EPEL) repository which provides additional packages for RHEL.

   ```bash
   sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   ```

2. **Install Ansible**

   Once the EPEL repository is enabled, you can install Ansible using the following command:

   ```bash
   sudo dnf install ansible
   ```

3. **Verify Installation**

   To confirm that Ansible has been successfully installed, you can run:

   ```bash
   ansible --version
   ```
   This command will display the Ansible version along with some configuration file locations.

### Step 2: Configure Ansible

1. **Ansible Configuration File**

   Ansible’s behavior can be customized via settings in the `/etc/ansible/ansible.cfg` configuration file. This file is well documented and provides a great resource for understanding configuration options.

2. **Edit the Configuration File**

   Use a text editor to open the configuration file:

   ```bash
   sudo vi /etc/ansible/ansible.cfg
   ```

   Here are a few common configurations you might want to adjust:

   - **`inventory`**: Defines the path to the inventory file.
   - **`remote_user`**: The default username to use for playbooks that do not specify a user.
   - **`ask_pass`**: Enables a prompt for a password by default (e.g., for SSH).
   - **`sudo_user`**: Specify a default user for sudo.

   For example, to set up a default inventory file, locate the `[defaults]` section and modify the `inventory` option:

   ```ini
   [defaults]
   inventory = /etc/ansible/hosts
   ```

3. **Create Inventory File**

   Ansible works against multiple managed nodes (or "hosts"), using a list or group of lists known as inventory. Create or edit the inventory file as follows:

   ```bash
   sudo vi /etc/ansible/hosts
   ```

   Add your hosts under a group, for instance:

   ```ini
   [webservers]
   server1.example.com
   server2.example.com
   ```

   Save and close the file.

### Step 3: Testing Ansible

To ensure that Ansible can communicate with your managed nodes, use the `ansible` command to ping all nodes:

```bash
ansible all -m ping
```

You should receive a "pong" response from each managed node if everything is configured correctly.

## Detailed Code Examples

To further demonstrate configuring Ansible, let’s look at a simple playbook example:

```yaml
---
- name: Test Playbook
  hosts: webservers
  become: yes

  tasks:
  - name: Ensure Apache is installed
    yum:
      name: httpd
      state: present
```

This playbook ensures Apache is installed on all servers listed under the `[webservers]` group in your inventory file.

## Conclusion

You have successfully installed and configured an Ansible control node on your RHEL system. Now, you are well on your way to automating your infrastructure using Ansible. This foundation will also assist you in preparing for the Red Hat Certified System Administrator (RHCSA) exam, specifically focusing on automation skills. Continue to explore and expand your Ansible capabilities by creating more complex playbooks and exploring other Ansible features.