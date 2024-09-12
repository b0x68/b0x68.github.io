# Tech Tutorial: Automate RHCSA Tasks Using Ansible for Software Packages and Repositories Management

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, efficient management of software packages and repositories is a critical skill. Ansible, an IT automation tool, simplifies and automates the management of software packages and repositories on Red Hat Enterprise Linux (RHEL). This tutorial will guide you through automating standard RHCSA tasks related to software packages and repositories using Ansible.

The focus will be on using Ansible modules such as `yum`, `yum_repository`, and `package` to manage packages and repositories on RHEL systems. By the end of this tutorial, you will be able to create Ansible playbooks that install, update, and remove software packages, as well as configure and manage repositories.

## Prerequisites

- A working RHEL 8 or RHEL 9 environment.
- Ansible installed on a control node (can be a RHEL machine).
- One or more managed nodes (RHEL systems).
- Sudo privileges on all machines.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

Ensure Ansible is installed on your control node. If not, install it using the following command:

```bash
sudo dnf install ansible
```

Set up SSH key-based authentication between the control node and your managed nodes to allow Ansible to communicate and control the managed nodes.

### Step 2: Creating an Inventory File

Create an inventory file `/etc/ansible/hosts` or in your project directory. Add your managed nodes under a group `[rhel_hosts]`:

```ini
[rhel_hosts]
192.168.1.101
192.168.1.102
```

### Step 3: Writing Your First Playbook

Create a playbook named `package_management.yml`. This playbook will ensure that the `vim` package is installed on all managed nodes.

```yaml
---
- name: Ensure vim is installed on all RHEL hosts
  hosts: rhel_hosts
  become: yes
  tasks:
    - name: Install vim
      yum:
        name: vim
        state: present
```

Run the playbook using the ansible-playbook command:

```bash
ansible-playbook package_management.yml
```

### Step 4: Managing Repositories

Add a task to configure a repository. This example will add the EPEL repository to the managed nodes.

```yaml
    - name: Add EPEL Repository
      yum_repository:
        name: epel
        description: EPEL YUM repo
        baseurl: https://dl.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/
        enabled: yes
        gpgcheck: yes
        repo_gpgcheck: yes
        gpgkey: https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8
```

### Step 5: Updating and Removing Packages

Update a package to the latest version, and remove an unnecessary package.

```yaml
    - name: Ensure the latest version of git is installed
      yum:
        name: git
        state: latest

    - name: Remove the package "httpd"
      yum:
        name: httpd
        state: absent
```

## Detailed Code Examples

Here's the complete playbook with all the tasks discussed:

```yaml
---
- name: Manage packages and repositories on RHEL hosts
  hosts: rhel_hosts
  become: yes
  tasks:
    - name: Install vim
      yum:
        name: vim
        state: present
    - name: Add EPEL Repository
      yum_repository:
        name: epel
        description: EPEL YUM repo
        baseurl: https://dl.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/
        enabled: yes
        gpgcheck: yes
        repo_gpgcheck: yes
        gpgkey: https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8
    - name: Ensure the latest version of git is installed
      yum:
        name: git
        state: latest
    - name: Remove the package "httpd"
      yum:
        name: httpd
        state: absent
```

## Conclusion

This tutorial introduced you to automating software package and repository management tasks on RHEL systems using Ansible. By leveraging Ansible's `yum` and `yum_repository` modules, you can streamline the installation, update, and removal of packages, as well as manage repositories across multiple systems efficiently. This automation not only saves time but also increases the consistency and reliability of system configurations in your IT environment. As you prepare for your RHCSA exam, incorporating Ansible into your study and practice will undoubtedly prove beneficial.