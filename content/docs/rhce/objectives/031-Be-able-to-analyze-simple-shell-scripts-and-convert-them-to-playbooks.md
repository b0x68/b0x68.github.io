# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and repetitive jobs. It uses a simple syntax written in YAML called playbooks. In this tutorial, we will focus on converting simple shell scripts into Ansible playbooks. This skill is crucial for system administrators and DevOps professionals who are migrating from traditional script-based management to Ansible's more efficient and scalable management framework.

## Prerequisites

Before we begin, ensure you have the following:
- Ansible installed on a control node (your workstation or a management server).
- One or more managed nodes (servers you wish to manage with Ansible).
- SSH access from the control node to the managed nodes.
- Python installed on the managed nodes, as it’s required by Ansible.

## Step-by-Step Guide

### Step 1: Analyze the Shell Script

Consider a simple shell script that installs Apache and starts the service on a Linux server:

```bash
#!/bin/bash
apt-get update
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2
```

This script updates the package lists, installs Apache, and ensures the Apache service is running and enabled on boot.

### Step 2: Create an Ansible Playbook

To convert the above shell script into an Ansible playbook:
1. Open a text editor and create a new file named `install_apache.yml`.
2. Define the basic structure of a playbook:

```yaml
---
- name: Install and start Apache
  hosts: all
  become: yes
  tasks:
```

### Step 3: Add Tasks to the Playbook

Each command in the shell script translates to a task in the playbook.

#### Task 1: Update package lists

```yaml
    - name: Update package lists
      apt:
        update_cache: yes
```

#### Task 2: Install Apache

```yaml
    - name: Install Apache
      apt:
        name: apache2
        state: present
```

#### Task 3: Start and enable Apache service

```yaml
    - name: Ensure Apache is running and enabled
      systemd:
        name: apache2
        state: started
        enabled: yes
```

### Step 4: Running the Playbook

Save the file and run the playbook using the following command:

```bash
ansible-playbook -i hosts install_apache.yml
```

Here, `-i hosts` specifies the inventory file which lists the managed nodes. If you're using the default inventory, you can omit this option.

## Detailed Code Examples

Below is the complete playbook derived from the initial shell script:

```yaml
---
- name: Install and start Apache
  hosts: all
  become: yes
  tasks:
    - name: Update package lists
      apt:
        update_cache: yes

    - name: Install Apache
      apt:
        name: apache2
        state: present

    - name: Ensure Apache is running and enabled
      systemd:
        name: apache2
        state: started
        enabled: yes
```

This playbook demonstrates a basic translation from a shell script to an Ansible playbook, covering common tasks like package installation and service management.

## Conclusion

Converting shell scripts to Ansible playbooks not only streamlines configuration management but also enhances scalability and consistency across environments. By following the steps outlined in this tutorial, you can begin to leverage Ansible's powerful capabilities to automate your infrastructure efficiently. As you become more familiar with Ansible’s modules and playbook structures, you can tackle more complex automation tasks, further reducing manual overhead and potential human errors in your operational processes.