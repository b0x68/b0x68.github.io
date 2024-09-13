# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is a powerful automation tool widely used for configuration management, application deployment, and task automation. One of its core components is the playbook, which allows you to describe your automation jobs in a declarative manner. This tutorial aims to guide you through the process of creating Ansible plays and playbooks specifically tailored for Red Hat Enterprise Linux (RHEL) systems, aligning with the Red Hat Certified Engineer (RHCE) exam objectives.

## Step-by-Step Guide

### Prerequisites
- A RHEL server (or a VM) set up with Ansible installed.
- Basic understanding of YAML syntax.
- SSH access set up for the target RHEL systems.

### 1. Setting up Your Environment

Before creating your playbook, ensure Ansible is installed on your RHEL system:

```bash
sudo dnf install ansible
```

Verify the installation:

```bash
ansible --version
```

### 2. Inventory File

Create an inventory file to define the hosts on which the playbook will run. Save this as `hosts.ini`:

```ini
[rhel-servers]
192.168.1.100 ansible_user=rhel-user
192.168.1.101 ansible_user=rhel-user
```

### 3. Simple Playbook to Update and Install Packages

Create a YAML file for the playbook. We'll start with a simple example that updates all packages and installs Apache on RHEL servers:

```yaml
---
- name: Update and Install Apache
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Ensure all packages are up to date
      dnf:
        name: "*"
        state: latest

    - name: Install Apache
      dnf:
        name: httpd
        state: present

    - name: Ensure Apache is running and enabled
      systemd:
        name: httpd
        state: started
        enabled: yes
```

### 4. Running Your Playbook

Execute the playbook using the ansible-playbook command:

```bash
ansible-playbook -i hosts.ini update_and_install_apache.yml
```

### Detailed Code Examples

#### Example 1: Configuring Users and Groups

The following playbook creates a user and a group on RHEL systems:

```yaml
---
- name: Configure Users and Groups
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Create a new group
      group:
        name: developers
        state: present

    - name: Create a new user
      user:
        name: jdoe
        group: developers
        createhome: yes
```

#### Example 2: Deploying and Configuring Firewalld

Set up firewalld to allow HTTP and HTTPS traffic:

```yaml
---
- name: Configure and Enable firewalld
  hosts: rhel-servers
  become: yes
  tasks:
    - name: Install firewalld
      dnf:
        name: firewalld
        state: present

    - name: Start and enable firewalld
      systemd:
        name: firewalld
        state: started
        enabled: yes

    - name: Open HTTP and HTTPS ports
      firewalld:
        service: "{{ item }}"
        permanent: true
        state: enabled
      loop:
        - http
        - https
```

### Conclusion

This tutorial provided a foundational guide on creating Ansible plays and playbooks specifically for managing RHEL systems. By following the examples provided, you can automate a wide range of administrative tasks, ensuring your systems are configured consistently and efficiently. As you prepare for the RHCE exam, practice by expanding these playbooks to include more complex tasks and configurations tailored to your specific needs.

Keep exploring and refining your Ansible skills to manage and automate your RHEL environment effectively. Happy automating!