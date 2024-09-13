# Tech Tutorial: Automate Standard RHCSA Tasks Using Ansible for Software Packages and Repositories Management

## Introduction

In this tutorial, we will explore how to automate key Red Hat Certified System Administrator (RHCSA) tasks related to software packages and repositories using Ansible. This will cover the management of software packages and repositories on Red Hat Enterprise Linux (RHEL) systems, strictly adhering to the commands and practices suitable for this distribution.

Ansible is an open-source automation tool that can be used to automate various system administration tasks. It uses a simple syntax written in YAML, called playbooks. We'll focus on using these playbooks to manage packages and repositories efficiently and reliably.

## Prerequisites

Before you proceed, ensure you have the following setup:

1. **Ansible Control Node:** A system from which you will run Ansible commands. This system must have Ansible installed.
2. **Managed Nodes:** One or more RHEL systems that Ansible will manage.
3. **SSH Access:** The control node should have SSH access to all managed nodes.
4. **Sudo Privileges:** The user under which Ansible runs should have sudo privileges on the managed nodes.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

First, you need to define your managed nodes in an Ansible inventory file. Create a file named `hosts` in your working directory:

```ini
[redhat_servers]
rhel1 ansible_host=192.168.1.101
rhel2 ansible_host=192.168.1.102
```

### Step 2: Ansible Playbook for Installing Packages

Create a YAML file named `install_packages.yml`. This playbook will ensure that certain packages are installed on all RHEL servers.

```yaml
---
- name: Ensure necessary packages are installed
  hosts: redhat_servers
  become: yes

  tasks:
    - name: Install packages
      yum:
        name:
          - vim
          - tree
          - wget
        state: present
```

### Explanation:

- **hosts**: Specifies the group of hosts from the inventory on which this playbook will run.
- **become**: Elevates privileges to become the `root` user.
- **yum module**: Used for managing packages with YUM. The state `present` ensures the packages are installed.

### Step 3: Ansible Playbook for Removing Packages

Create a YAML file named `remove_packages.yml`. This playbook will remove specified packages from the RHEL servers.

```yaml
---
- name: Ensure specified packages are removed
  hosts: redhat_servers
  become: yes

  tasks:
    - name: Remove packages
      yum:
        name:
          - nano
        state: absent
```

### Step 4: Managing Repositories

To manage YUM repositories, you can use the `yum_repository` module. Create a playbook named `manage_repos.yml`:

```yaml
---
- name: Manage YUM repositories
  hosts: redhat_servers
  become: yes

  tasks:
    - name: Enable EPEL Repository
      yum_repository:
        name: epel
        description: EPEL YUM repo
        baseurl: https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/
        enabled: yes
        gpgcheck: yes
        gpgkey: https://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8

    - name: Disable EPEL Repository
      yum_repository:
        name: epel
        state: absent
```

### Explanation:

- **yum_repository**: Manages YUM repository configurations. The first task enables the EPEL repository, and the second disables it.

## Conclusion

In this tutorial, we've covered how to use Ansible for automating tasks related to the management of software packages and repositories on RHEL systems. By leveraging Ansible's simple YAML syntax and powerful modules like `yum` and `yum_repository`, you can automate the provisioning and maintenance of RHEL servers efficiently, ensuring consistency and reliability in your infrastructure. This approach not only saves time but also reduces the potential for human error, making it an essential skill for RHCSA tasks.