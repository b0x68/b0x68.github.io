# Tech Tutorial: Automate Archiving Tasks for RHCSA using Ansible

## Introduction

Ansible is a powerful open-source automation tool that simplifies configuration management, application deployment, and task automation. In this tutorial, we will focus on using Ansible to automate archiving tasks, a common requirement for system administrators preparing for the Red Hat Certified System Administrator (RHCSA) exam. Archiving is essential for managing backups, reducing storage space, and improving data management.

In this tutorial, we will cover:
1. Setting up Ansible on your system.
2. Creating an Ansible playbook to automate archiving tasks.
3. Detailed code examples to demonstrate the process.

## Prerequisites

- A Linux system (CentOS, RHEL, or Fedora preferred) for the Ansible control node.
- One or more managed nodes (Linux systems) where archiving tasks will be performed.
- SSH access and privilege escalation (sudo) rights on all nodes.

## Step-by-Step Guide

### Step 1: Setting Up Ansible

Before automating tasks, you need to install Ansible on your control machine. For RHEL/CentOS systems, you can use the following commands:

```bash
sudo yum install epel-release
sudo yum install ansible
```

Verify the installation with:

```bash
ansible --version
```

### Step 2: Configuring Ansible

Create or edit the `/etc/ansible/hosts` file to add your managed nodes:

```ini
[managed_nodes]
192.168.1.50 ansible_user=your_user ansible_ssh_private_key_file=/path/to/key
192.168.1.51 ansible_user=your_user ansible_ssh_private_key_file=/path/to/key
```

Replace `192.168.1.50` and `192.168.1.51` with the IP addresses of your managed nodes, and update `your_user` and `/path/to/key` with appropriate user and SSH key path.

### Step 3: Creating the Ansible Playbook for Archiving

Create a new file named `archive_playbook.yml`:

```yaml
---
- name: Archiving Task Automation
  hosts: managed_nodes
  become: yes
  tasks:
    - name: Create an archive of /etc directory
      ansible.builtin.archive:
        path: /etc
        dest: /tmp/etc_backup.tar.gz
        format: gz
        owner: root
        group: root
        mode: '0644'
```

This playbook performs the following:
- Targets hosts under the `managed_nodes` group.
- Escalates privileges to become the root user.
- Uses the `ansible.builtin.archive` module to compress the `/etc` directory into a `.tar.gz` file located at `/tmp/etc_backup.tar.gz`.

### Step 4: Running the Playbook

Execute the playbook using the following command:

```bash
ansible-playbook archive_playbook.yml
```

## Detailed Code Examples

Let's delve deeper into the `ansible.builtin.archive` module used in our playbook:

```yaml
ansible.builtin.archive:
  path: /etc
  dest: /tmp/etc_backup.tar.gz
  format: gz
  owner: root
  group: root
  mode: '0644'
```

- **path**: Specifies the directory or file to archive.
- **dest**: Defines the destination file path for the archive.
- **format**: Sets the archive format (`gz`, `bz2`, `tar`, etc.).
- **owner**, **group**, **mode**: Set file permissions and ownership.

## Conclusion

In this tutorial, we have demonstrated how to automate archiving tasks using Ansible, which can greatly simplify the management of backups and data storage in a Linux environment. By leveraging Ansible's powerful modules like `ansible.builtin.archive`, system administrators can ensure consistent and error-free archiving operations across multiple systems, enhancing the overall efficiency and reliability of IT operations.

As you prepare for the RHCSA exam, incorporating such automation practices can not only save time but also provide a deeper understanding of both system administration and automation principles.