# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Software Packages and Repositories

## Introduction

In this tutorial, we will explore how to automate common Red Hat Certified System Administrator (RHCSA) tasks related to software packages and repositories using Ansible. We'll cover how to manage RPM packages, handle repositories, and ensure your systems are always up to date with the required software, all by using Ansible modules specifically designed for these purposes.

Ansible is an open-source automation tool that simplifies complex configuration management, application deployment, and task automation. It uses a simple syntax written in YAML, called playbooks. Ansible communicates over normal SSH channels to retrieve information from remote systems, perform tasks, and write the results back to the Ansible server.

## Prerequisites

Before we dive into the specifics, make sure you have the following setup:
- A control node with Ansible installed.
- One or more managed nodes (CentOS/RHEL systems), accessible via SSH from the control node.
- Sudo privileges on the managed nodes.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Firstly, you need to define your inventory. Ansible inventory is a list of hosts (nodes) which Ansible manages. Create a file named `hosts` in your working directory and add your nodes:

```ini
[all]
node1 ansible_host=192.168.1.101 ansible_user=root
node2 ansible_host=192.168.1.102 ansible_user=root
```

### Step 2: Writing Your First Playbook

Create a new YAML file named `manage-packages.yml`. This will contain the Ansible playbook.

#### Managing Software Packages

We will start by ensuring that a package is installed, updated, or removed.

```yaml
---
- name: Manage Packages and Repositories
  hosts: all
  become: yes
  tasks:
    - name: Ensure vim is installed
      yum:
        name: vim
        state: present

    - name: Upgrade all packages
      yum:
        name: '*'
        state: latest

    - name: Remove the package 'httpd'
      yum:
        name: httpd
        state: absent
```

This playbook performs three tasks:
1. Ensures that `vim` is installed.
2. Upgrades all the packages to the latest version.
3. Removes the `httpd` package if it is installed.

### Step 3: Managing Repositories

Now let's manage the YUM repositories. Add the following tasks to your playbook:

```yaml
    - name: Add a new repository
      yum_repository:
        name: EPEL
        description: EPEL YUM repo
        baseurl: https://download.fedoraproject.org/pub/epel/$releasever/$basearch/
        enabled: yes
        gpgcheck: no

    - name: Remove a repository
      yum_repository:
        name: EPEL
        state: absent
```

These tasks will add a new repository (EPEL in this case) and remove it. The `gpgcheck: no` disables GPG signature checking; change this as per your security policy.

### Step 4: Running Your Playbook

Save the playbook and run it using the following command:

```bash
ansible-playbook -i hosts manage-packages.yml
```

## Detailed Code Examples

Let's dissect one of the tasks to understand what each parameter does:

```yaml
- name: Ensure vim is installed
  yum:
    name: vim
    state: present
```

- `name`: Descriptive name of the task.
- `yum`: Ansible module for managing packages with Yum.
- `name: vim`: Specifies the name of the package.
- `state: present`: Desired state of the package (`present` ensures the package is installed).

## Conclusion

In this tutorial, you have learned how to automate package and repository management tasks on CentOS/RHEL systems using Ansible. By integrating these practices, you can ensure consistency across your environment, reduce manual errors, and save time on routine administration tasks. As you grow more familiar with Ansible's capabilities, you can expand your playbooks to automate more complex setups and configurations across your infrastructure.