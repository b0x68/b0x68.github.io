# Automate Standard RHCSA Tasks Using Ansible for File Content Management

## Introduction

In this tutorial, we will explore how to automate various Red Hat Certified System Administrator (RHCSA) tasks related to file content management using Ansible. Ansible is an open-source automation tool that simplifies configuration management, application deployment, and task automation. It uses a straightforward YAML syntax, making it easy for sysadmins and developers to orchestrate complex setups.

## Prerequisites

Before we dive into the specifics, ensure you have the following:

- A control node with Ansible installed. This can be any machine from which you will manage other nodes.
- One or more managed nodes, which are the systems you want to configure and manage through Ansible.
- SSH access configured from the control node to each managed node.
- Python installed on all nodes (usually comes by default on most Linux distributions).

## Step-by-Step Guide

We will cover the following tasks in this guide:

1. Creating a file with specific content.
2. Editing an existing file to ensure it contains specific lines.
3. Deleting files.

### Task 1: Creating a File with Specific Content

We'll start by writing an Ansible playbook that creates a new file and inserts specified text into it.

#### Playbook: create_file.yml

```yaml
---
- name: Create a file with specific content
  hosts: all
  become: yes  # Ensures you have the necessary privileges

  tasks:
    - name: Ensure the file /etc/ansible_example.txt exists and has specific content
      copy:
        content: |
          Hello, this is a test file.
          This file is managed by Ansible.
        dest: /etc/ansible_example.txt
        owner: root
        group: root
        mode: '0644'
```

**Explanation:**
- `copy`: The module used to copy content to a file on remote nodes.
- `content`: Text that will be written to the file.
- `dest`: Destination path of the file on the managed node.
- `owner`, `group`, `mode`: File permissions settings.

### Task 2: Ensuring Specific Lines in a File

Next, we'll ensure that a specific line is present in a configuration file using the `lineinfile` module.

#### Playbook: edit_file.yml

```yaml
---
- name: Ensure specific lines are present in a configuration file
  hosts: all
  become: yes

  tasks:
    - name: Ensure the line is present in /etc/sysconfig/network-scripts/ifcfg-eth0
      lineinfile:
        path: /etc/sysconfig/network-scripts/ifcfg-eth0
        line: 'DNS1=8.8.8.8'
        create: yes  # Create the file if it does not exist
```

**Explanation:**
- `lineinfile`: The module used to manage lines in a file.
- `path`: The file to modify.
- `line`: The line to add or ensure exists.
- `create`: Whether to create the file if it does not exist.

### Task 3: Deleting Files

Lastly, we'll use Ansible to delete a file.

#### Playbook: delete_file.yml

```yaml
---
- name: Delete a specific file
  hosts: all
  become: yes

  tasks:
    - name: Ensure the file /etc/unnecessary_file.txt is absent
      file:
        path: /etc/unnecessary_file.txt
        state: absent
```

**Explanation:**
- `file`: The module used for file management.
- `path`: The location of the file to manage.
- `state`: Defines the state of the file, `absent` which ensures the file is deleted.

## Running Your Playbooks

To run any of these playbooks, save the code to a file on your control node and execute the following command:

```bash
ansible-playbook -i hosts_file create_file.yml
```

Here, `hosts_file` is your inventory file containing the managed nodes' addresses.

## Conclusion

In this tutorial, we've covered how to automate three common file management tasks on RHCSA using Ansible. These examples serve as a foundation for automating more complex system administration tasks, reducing manual effort, and increasing reliability through consistent configurations across your infrastructure.