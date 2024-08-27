# Tech Tutorial: Install and Configure an Ansible Control Node

## Introduction

In this tutorial, we will explore how to set up an Ansible control node and create static inventories to define groups of hosts. Ansible is a powerful automation tool used for configuration management, application deployment, task automation, and much more. One of its core components is the inventory file, which lists the hosts and groups of hosts upon which commands, modules, and tasks in a playbook operate. 

## Prerequisites

Before we begin, ensure you have the following:
- A Linux environment (Ubuntu 20.04 LTS is used in this tutorial)
- Sudo or root privileges on the system
- Internet connectivity

## Step-by-Step Guide

### Step 1: Install Ansible

First, update your system's package index and install Ansible using the following commands:

```bash
sudo apt update
sudo apt install ansible -y
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

You should see output detailing the installed version of Ansible.

### Step 2: Create a Static Inventory File

Ansible uses inventory files to track which servers it can communicate with. We'll create a static inventory file to list our hosts.

1. Create a directory for your Ansible project:

    ```bash
    mkdir ~/ansible-project
    cd ~/ansible-project
    ```

2. Create an inventory file named `hosts`:

    ```bash
    touch hosts
    ```

3. Open the `hosts` file with a text editor:

    ```bash
    nano hosts
    ```

4. Add the following content to the `hosts` file:

    ```ini
    [web]
    server1.example.com

    [database]
    server2.example.com

    [all:vars]
    ansible_user=your_username
    ansible_ssh_private_key_file=/path/to/your/private/key
    ```

    In this inventory file:
    - `[web]` and `[database]` are groups containing different hosts.
    - `server1.example.com` and `server2.example.com` are the hostnames. Replace them with your actual hostnames or IP addresses.
    - Under `[all:vars]`, common variables applied to all hosts are defined. Adjust `ansible_user` and `ansible_ssh_private_key_file` to match your environment.

### Step 3: Test Connectivity

With your inventory file set up, test if Ansible can connect to the hosts listed:

```bash
ansible all -m ping -i hosts
```

This command should return a `SUCCESS` message from each server, indicating that Ansible can communicate effectively with all nodes in your inventory.

### Step 4: Run Ad-hoc Commands

Now, let's try running an ad-hoc command to see Ansible in action. To check disk usage on all web servers, use:

```bash
ansible web -a "df -h" -i hosts
```

This command runs `df -h` on all hosts under the `[web]` group.

## Detailed Code Examples

Here’s a more complex example of using the inventory file to run a playbook:

1. Create a simple playbook named `sample-playbook.yml`:

    ```yaml
    ---
    - name: Check Disk Space
      hosts: web
      tasks:
        - name: Disk space check
          command: df -h
          register: disk_space

        - name: Print disk space
          debug:
            msg: "{{ disk_space.stdout }}"
    ```

2. Run the playbook:

    ```bash
    ansible-playbook -i hosts sample-playbook.yml
    ```

This playbook performs a disk space check on all hosts in the `web` group and prints the output.

## Conclusion

This tutorial covered the basics of setting up an Ansible control node, creating a static inventory, and running commands and playbooks against that inventory. With this foundation, you can expand your Ansible skills to automate virtually any aspect of your IT environment. Happy automating!