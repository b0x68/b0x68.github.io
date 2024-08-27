# Tech Tutorial: Understand Core Components of Ansible - Focus on Plays

## Introduction

In this tutorial, we will explore one of the core components of Ansible: Plays. Understanding plays is crucial as they are the building blocks of playbooks, which are used to orchestrate tasks on various hosts. This guide will provide a step-by-step exploration of Ansible plays, complete with detailed code examples to help you learn how to effectively utilize them in real-world scenarios.

## What is a Play in Ansible?

A "play" in Ansible is essentially a set of tasks that are executed on a defined group of hosts. It is a structured unit of execution within a playbook. Each play must specify a host or group of hosts and the tasks that need to be run on those hosts.

## Prerequisites

Before diving into the details of plays, ensure you have the following setup:
- **Ansible installed** on your control machine (the machine from which you are running the commands).
- **Access to at least one or more managed nodes** (the servers you want to configure with Ansible).
- **SSH access configured** between the control machine and your managed nodes.
- **Python installed** on the managed nodes, as it’s required by Ansible.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Create an inventory file named `hosts.ini` that defines the groups of hosts on which tasks will be executed. Here’s an example:

```ini
[web_servers]
192.168.1.101
192.168.1.102

[db_servers]
192.168.1.201

[all:vars]
ansible_user=your_username
ansible_ssh_private_key_file=/path/to/your/private/key
```

In this inventory file, we have two groups: `web_servers` and `db_servers`, with IPs assigned to each group.

### Step 2: Writing Your First Play

Create a file named `site.yml`. This is where we will define our play. Here's a simple example that ensures the Apache web server is installed on all web servers:

```yaml
---
- name: Ensure Apache is installed on all web servers
  hosts: web_servers
  become: yes  # Use privilege escalation
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
```

This play is named "Ensure Apache is installed on all web servers" and targets hosts under `web_servers`. It escalates privileges to execute tasks (important for installing packages) and defines a single task to install Apache using the `apt` module.

### Step 3: Running Your Play

To run the playbook, use the following command:

```bash
ansible-playbook -i hosts.ini site.yml
```

This command tells Ansible to use the `hosts.ini` inventory file and execute the `site.yml` playbook.

### Step 4: Adding More Complexity

Let’s enhance our playbook to not only install Apache but also ensure it is running and enabled at boot:

```yaml
---
- name: Ensure Apache is installed and running on web servers
  hosts: web_servers
  become: yes
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present

    - name: Start and enable Apache
      systemd:
        name: apache2
        state: started
        enabled: yes
```

This play now has an additional task that uses the `systemd` module to start the Apache service and ensure it’s enabled at boot.

## Conclusion

In this tutorial, you've learned what Ansible plays are and how to write them. We covered how to set up an inventory, write a play, and execute it. Plays are powerful as they allow you to define what you want to happen on which hosts, making Ansible a very flexible tool for managing your infrastructure.

From here, you can expand your knowledge by exploring more complex playbooks, different modules, and other advanced features of Ansible. Happy automating!