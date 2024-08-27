# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration management, application deployment, and task automation. It uses a straightforward YAML syntax, making it easy for sysadmins, developers, and IT professionals to define tasks and orchestrate their automatic execution. This tutorial will guide you through the process of creating Ansible plays and playbooks to configure systems into a specified state.

## Prerequisites

Before diving into creating Ansible playbooks, you should have the following:

- Ansible installed on a control node (your workstation or a management server).
- One or more managed nodes (servers) that the Ansible control node can access over SSH.
- Python installed on the managed nodes, as it's required by Ansible.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Ansible interacts with the machines it manages using an inventory file that lists all the nodes. Here's a simple example of an inventory file:

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[dbservers]
dbserver1.example.com
```

### Step 2: Writing Your First Playbook

A playbook is a file where Ansible code is written. Playbooks describe the desired state of your systems using a series of plays. Let's create a simple playbook to install and start Apache on a group of web servers.

1. **Create a file named `install_apache.yml`:**

```yaml
---
- name: Install and start Apache
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present
    
    - name: Start Apache
      service:
        name: httpd
        state: started
        enabled: yes
```

This playbook consists of two main tasks:
- Installing Apache using the `yum` module.
- Ensuring the Apache service is started and enabled to start at boot.

### Step 3: Running Your Playbook

Execute the playbook using the `ansible-playbook` command:

```bash
ansible-playbook -i inventory install_apache.yml
```

This command tells Ansible to use the `install_apache.yml` playbook and the specified inventory file.

## Detailed Code Examples

Let's expand our playbook to configure server-specific settings using variables and templates.

### Using Variables

Variables in Ansible can be defined in several places like in inventory, playbook, or in separate variable files. Here’s how to define and use variables in a playbook:

```yaml
---
- name: Configure Apache
  hosts: webservers
  become: yes
  vars:
    http_port: 80
    max_clients: 200
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

    - name: Configure httpd.conf
      template:
        src: templates/httpd.conf.j2
        dest: /etc/httpd/conf/httpd.conf
      notify:
        - restart apache

  handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```

### Using Templates

Ansible uses Jinja2 templates to manage configuration files. Here’s an example of a template for `httpd.conf`:

```jinja2
ServerName "localhost"
Listen {{ http_port }}
MaxClients {{ max_clients }}
```

This template (`httpd.conf.j2`) will use the variables defined in the playbook.

## Conclusion

In this tutorial, you've learned how to create Ansible plays and playbooks to automate the configuration of servers. By using Ansible, you can ensure that your systems are configured consistently and correctly, reducing the potential for human error and increasing the efficiency of your operations. Continue exploring more complex playbooks and more of Ansible's powerful features to fully leverage its capabilities in your environment.