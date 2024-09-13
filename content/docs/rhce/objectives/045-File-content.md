# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible Modules for File Content Management

## Introduction

In the world of system administration, consistency and efficiency are key. Ansible, a powerful automation tool, excels in ensuring that both are achieved with minimal fuss. This tutorial focuses on automating file content management tasks on Red Hat Enterprise Linux (RHEL) systems, aligning with specific RHCSA exam objectives. We will explore how to use Ansible to manage file contents effectively, ensuring your systems are configured correctly and consistently.

## Prerequisites

Before you begin, ensure you have the following:

- A working RHEL system (version 7 or 8) for testing.
- Ansible installed on a control node (which can be the same RHEL system or another system).
- Sudo privileges on the managed nodes.

## Step-by-Step Guide

This guide will cover several tasks:

1. Installing and configuring Ansible on RHEL.
2. Creating and managing file contents using Ansible modules.
3. Validating the file content changes.

### Step 1: Installing Ansible on RHEL

First, you need to install Ansible on your control node. On RHEL, you can do this using the EPEL repository:

```bash
sudo subscription-manager repos --enable rhel-7-server-optional-rpms
sudo yum install epel-release -y
sudo yum install ansible -y
```

### Step 2: Setting Up Your Ansible Inventory

Create an inventory file `/etc/ansible/hosts` and add the RHEL systems you will manage:

```ini
[rhel]
192.168.1.100 ansible_user=your_username ansible_ssh_private_key_file=/path/to/key
```

Replace `192.168.1.100` with the IP address of your RHEL node, and adjust `your_username` and `/path/to/key` accordingly.

### Step 3: Managing File Content with Ansible

#### A. Creating and Writing to Files

Suppose you need to ensure that a specific configuration file on all servers contains certain lines. You can use the `copy` module for simple content or `template` for more dynamic content.

**Example: Using the `copy` module**

Create a playbook named `file-content.yml`:

```yaml
---
- name: Ensure the admin user configuration is set
  hosts: rhel
  become: yes
  tasks:
    - name: Set admin user config
      copy:
        dest: "/etc/admin.conf"
        content: |
          USER=admin
          TIMEOUT=60
        owner: root
        group: root
        mode: '0644'
```

Run the playbook:

```bash
ansible-playbook file-content.yml
```

#### B. Modifying Existing File Content

For scenarios where you need to ensure certain lines are present or absent in existing files, use the `lineinfile` module.

**Example: Ensuring a specific line is present**

Add the following task to your playbook:

```yaml
    - name: Ensure timeout is configured
      lineinfile:
        path: /etc/admin.conf
        line: 'TIMEOUT=60'
        create: yes
        owner: root
        group: root
        mode: '0644'
```

### Step 4: Validating File Changes

You can validate the changes by either manually checking the file on the managed node or using the `ansible` command to fetch the file content:

```bash
ansible rhel -m fetch -a "src=/etc/admin.conf dest=./"
```

## Detailed Code Examples

The provided YAML configurations in Step 3 are ready-to-use examples that you can incorporate into your Ansible playbooks. Adjust the IP addresses, user names, and file paths according to your environment.

## Conclusion

Using Ansible for managing file contents on RHEL systems not only automates routine tasks but also ensures compliance and consistency across the infrastructure. This tutorial covered basic yet crucial aspects of file management using Ansible, providing a solid foundation for further exploration and customization of your automation workflows. As you prepare for the RHCSA exam, consider how these techniques can be applied to manage other system configurations and resources effectively.