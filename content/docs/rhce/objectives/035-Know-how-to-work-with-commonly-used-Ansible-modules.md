# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and consistent IT application environments. It's used for application deployment, configuration management, and task automation. This tutorial will guide you through creating Ansible plays and playbooks, focusing on commonly used Ansible modules. By the end of this tutorial, you'll have a good grasp of creating and running Ansible playbooks for managing your infrastructure.

## Prerequisites

Before you start, you should have the following installed:
- Ansible (2.9 or higher recommended)
- A text editor (e.g., VSCode, Atom, Sublime)
- One or more managed nodes (servers) that Ansible can connect to via SSH

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure Ansible is installed on your control machine (the machine that will run Ansible commands). You can install Ansible using the following command on a Debian-based system:

```bash
sudo apt update
sudo apt install ansible
```

Verify the installation by checking the Ansible version:

```bash
ansible --version
```

### Step 2: Creating the Inventory File

Ansible uses an inventory file to track which servers it can interact with. Create an inventory file named `hosts.ini`:

```ini
[servers]
server1 ansible_host=192.168.1.101
server2 ansible_host=192.168.1.102

[all:vars]
ansible_user=your_username
ansible_ssh_private_key_file=/path/to/your/key
```

### Step 3: Writing Your First Playbook

Create a file named `site.yml`. This is your Ansible playbook where you define the tasks to be executed:

```yaml
---
- name: Update web servers
  hosts: servers
  become: yes
  tasks:
    - name: Ensure Apache is at the latest version
      apt:
        name: apache2
        state: latest
      when: ansible_os_family == "Debian"
```

This playbook has one play with one task that ensures Apache (`apache2`) is installed and updated to the latest version on all servers under the `servers` group in the inventory.

### Step 4: Running Your Playbook

Execute the playbook using the following command:

```bash
ansible-playbook -i hosts.ini site.yml
```

### Detailed Code Examples

#### Example 1: Creating Users

Suppose you want to create a new user on all servers. Here’s how you can do it using the `user` module:

```yaml
---
- name: Add a new user
  hosts: servers
  become: yes
  tasks:
    - name: Create a user named 'newuser'
      user:
        name: newuser
        state: present
        createhome: yes
```

#### Example 2: Copying Files

To copy a local file to the servers, use the `copy` module:

```yaml
---
- name: Copy file to servers
  hosts: servers
  become: yes
  tasks:
    - name: Copy sample.txt to /tmp
      copy:
        src: /path/to/sample.txt
        dest: /tmp/sample.txt
```

#### Example 3: Managing Services

To ensure a service (e.g., Nginx) is running on all servers, use the `service` module:

```yaml
---
- name: Ensure Nginx is running
  hosts: servers
  become: yes
  tasks:
    - name: Start Nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

## Conclusion

This tutorial provided a step-by-step guide on creating Ansible plays and playbooks, focusing on commonly used modules like `apt`, `user`, `copy`, and `service`. By mastering these modules, you can automate a significant portion of your server management tasks, improving both efficiency and consistency across environments. Start experimenting with different modules and parameters to tailor your automation to your specific needs. Happy automating!