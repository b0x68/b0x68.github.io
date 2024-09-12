# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool that simplifies system configuration, application deployment, and other IT needs through automation. In this tutorial, we will focus on creating Ansible plays and playbooks, which are essential for configuring systems to a specified state. This guide is especially tailored for the Red Hat Certified System Administrator (RHCSA) exam, and thus will strictly adhere to configurations and commands applicable to Red Hat Enterprise Linux (RHEL) distributions.

## Prerequisites

Before we dive into the creation of plays and playbooks, ensure you have the following:
- A RHEL system (physical or virtual) for testing.
- Ansible installed on a control node (which could also be your RHEL system).
- SSH access configured from the control node to any managed nodes.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure that Ansible is installed on your RHEL system. You can install Ansible using the following YUM command:

```bash
sudo yum install ansible -y
```

Verify the installation with:

```bash
ansible --version
```

### Step 2: Configure Ansible Inventory

Ansible uses an inventory file to track which servers it can communicate with. By default, this file is located at `/etc/ansible/hosts`. Edit this file to add the RHEL systems you want to manage:

```ini
[webservers]
webserver1.example.com

[dbservers]
dbserver1.example.com
```

### Step 3: Create Your First Playbook

Playbooks are YAML files where Ansible’s configuration, deployment, and orchestration activities are defined. Let's create a simple playbook to update all packages on a RHEL server.

Create a file named `update.yml`:

```yaml
---
- name: Update all packages on a RHEL system
  hosts: all
  become: yes
  tasks:
    - name: Ensure all packages are up to date
      yum:
        name: '*'
        state: latest
```

### Step 4: Run the Playbook

Execute the playbook using the `ansible-playbook` command:

```bash
ansible-playbook update.yml
```

This command will connect to the specified hosts in your inventory, escalate privileges via `become: yes`, and execute the task to update all packages.

## Detailed Code Examples

### Example: Configure a Web Server

Let's say you want to configure a RHEL system as a web server using Apache. Below is a playbook that installs Apache, starts the service, and ensures it runs at boot.

Create a file named `webserver.yml`:

```yaml
---
- name: Configure Apache web server
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

    - name: Start Apache service
      systemd:
        name: httpd
        state: started
        enabled: yes
```

Run the playbook:

```bash
ansible-playbook webserver.yml
```

### Step 5: Adding Handlers

Handlers are used in Ansible to manage services and perform tasks triggered by other tasks. Modify the `webserver.yml` to include a handler that restarts Apache if the configuration changes.

Add a handler to the `webserver.yml`:

```yaml
---
- name: Configure Apache web server
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

    - name: Start Apache service
      systemd:
        name: httpd
        state: started
        enabled: yes
      notify:
        - restart apache
      
  handlers:
    - name: restart apache
      systemd:
        name: httpd
        state: restarted
        enabled: yes
```

## Conclusion

In this tutorial, we covered the basics of creating Ansible plays and playbooks tailored for managing RHEL systems. These examples provide a foundation for automating system configurations and managing state across multiple systems efficiently. With practice, you can expand upon these basics to handle more complex tasks and orchestrate entire environments using Ansible.