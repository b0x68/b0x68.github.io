# Tech Tutorial: Install and Configure an Ansible Control Node

## Introduction

In this tutorial, we will focus on how to install and configure an Ansible control node on a Red Hat Enterprise Linux (RHEL) system. The key aspect of this setup will include creating and using static inventories to define groups of hosts, an essential skill for anyone preparing for the Red Hat Certified Engineer (RHCE) exam. Ansible is a powerful automation tool that simplifies complex configuration tasks and makes repetitive tasks more manageable.

## Prerequisites

- A RHEL 8 system (only RHEL commands and configurations will be used, as per the exam requirements).
- Root or sudo privileges on the system.
- Access to the internet for installing packages.

## Step-by-Step Guide

### Step 1: Installing Ansible on RHEL

First, ensure that your system is updated and that the required repository is enabled. Open a terminal and execute the following commands:

```bash
sudo dnf update -y
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
sudo dnf install ansible -y
```

### Step 2: Verify Ansible Installation

To confirm that Ansible has been installed correctly, run:

```bash
ansible --version
```

This command will display the version of Ansible installed along with some configuration details.

### Step 3: Setting Up the Inventory File

Ansible uses inventory files to track which servers it can interact with. By default, Ansible looks for the inventory file at `/etc/ansible/hosts`. We will create a static inventory to define our host groups.

1. Open the default Ansible inventory file in a text editor:

```bash
sudo vi /etc/ansible/hosts
```

2. Add the following configuration to define two groups of hosts, `web` and `db`:

```
[web]
webserver1.example.com
webserver2.example.com

[db]
dbserver1.example.com
```

In this setup, `webserver1.example.com` and `webserver2.example.com` are part of the 'web' group, and `dbserver1.example.com` is part of the 'db' group. Make sure to replace the hostnames with the actual hostnames or IP addresses of your servers.

### Step 4: Testing Connectivity

To test if Ansible can connect to the hosts defined in your inventory, use the `ansible` command with the `-m` (module) option to use the `ping` module, which is a simple way to check connectivity. Try pinging all hosts in the `web` group:

```bash
ansible web -m ping
```

This command should return a `SUCCESS` message for each host if Ansible can connect successfully.

### Step 5: Running Ad-Hoc Commands

Now that you have your inventory set up, you can start running ad-hoc commands to manage your hosts. For example, to check the disk space on all database servers, you can use:

```bash
ansible db -a "df -h"
```

This command runs the `df -h` command on all hosts in the `db` group and returns the disk usage.

## Detailed Code Examples

Here’s a more complex example where you use Ansible to ensure that the latest version of Apache is installed on all web servers:

```yaml
---
- name: Ensure Apache is at the latest version
  hosts: web
  become: yes
  tasks:
    - name: Install apache
      dnf:
        name: httpd
        state: latest
```

Save this as `install_apache.yml` and run it with:

```bash
ansible-playbook install_apache.yml
```

## Conclusion

By completing this tutorial, you have successfully installed and configured an Ansible control node on a RHEL system and created a static inventory to define and manage groups of hosts. This setup is fundamental for automation with Ansible, especially in preparation for the RHCE exam. Continue to experiment with different Ansible modules and playbooks to expand your automation capabilities.