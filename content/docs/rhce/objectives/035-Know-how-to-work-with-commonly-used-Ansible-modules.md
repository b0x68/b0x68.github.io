# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool that simplifies cloud provisioning, configuration management, application deployment, and several other IT needs. Leveraging Ansible for system administration allows you to automate repetitive tasks and to deploy applications and manage configurations across a wide range of systems in a consistent and reliable manner. In this tutorial, we will focus on creating Ansible plays and playbooks with an emphasis on commonly used modules in the context of a Red Hat Enterprise Linux (RHEL) environment.

## Step-by-Step Guide

### Prerequisites

- A RHEL server or VM setup for running Ansible.
- Ansible installed on a control node (could be the same RHEL system or another system).
- SSH access configured for the target node(s) from the control node.

### Step 1: Setting Up Your Inventory

An inventory file defines the hosts and groups of hosts upon which commands, modules, and tasks in a playbook operate. The default location for the inventory file is `/etc/ansible/hosts`, but you can create custom inventory files.

```ini
# Example of a simple inventory file
[webservers]
webserver1.example.com
webserver2.example.com

[dbservers]
dbserver1.example.com
```

### Step 2: Writing Your First Playbook

A playbook is a YAML file where you define tasks, the hosts on which to run those tasks, and the order in which to run them. Here's a simple playbook that ensures that the Apache web server is installed and running on all webservers.

```yaml
---
- name: Ensure Apache is at the latest version and running
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: latest

    - name: Start Apache
      service:
        name: httpd
        state: started
        enabled: yes
```

### Step 3: Running Your Playbook

Run the playbook using the `ansible-playbook` command:

```bash
ansible-playbook -i /path/to/your/inventory playbook.yml
```

### Detailed Code Examples

#### Example 1: Using the `user` Module

The `user` module manages user accounts in Linux. The following playbook creates a user on all servers in the `dbservers` group.

```yaml
---
- name: Add a new user
  hosts: dbservers
  become: yes
  tasks:
    - name: Create user account
      user:
        name: johndoe
        state: present
        createhome: yes
```

#### Example 2: Using the `copy` Module

The `copy` module copies files from the local machine to the remote machine. This playbook copies a configuration file to the webservers.

```yaml
---
- name: Copy configuration file to webservers
  hosts: webservers
  become: yes
  tasks:
    - name: Copy file
      copy:
        src: /files/sample.conf
        dest: /etc/httpd/conf.d/sample.conf
        owner: root
        group: root
        mode: '0644'
```

#### Example 3: Using the `command` Module

While Ansible encourages using modules, sometimes you might need to run commands directly. Here's how to use the `command` module to check disk space usage:

```yaml
---
- name: Check disk space
  hosts: all
  become: yes
  tasks:
    - name: Check disk space using df
      command: df -hT
      register: disk_space

    - name: Print disk space
      debug:
        var: disk_space.stdout_lines
```

## Conclusion

In this tutorial, you've learned how to create basic Ansible plays and playbooks focusing on commonly used modules like `yum`, `service`, `user`, `copy`, and `command`. These playbooks are fundamental building blocks for automating system administration tasks in a RHEL environment. As you become more familiar with Ansible, you'll be able to leverage its full capabilities to manage your infrastructure efficiently and reliably. Remember, the key to mastering Ansible is consistent practice and experimentation. Happy automating!