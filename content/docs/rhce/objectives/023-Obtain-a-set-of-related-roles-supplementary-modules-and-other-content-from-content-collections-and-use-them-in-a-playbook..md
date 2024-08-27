# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and speeds up the deployment process. One of its strengths lies in the use of roles and Ansible Content Collections, which help in organizing and sharing reusable code. This tutorial focuses on how to effectively utilize roles and content collections within an Ansible playbook, following the specified exam objective.

## Objectives

- Understand what Ansible Roles and Content Collections are.
- Learn how to obtain and use these roles and content collections in a playbook.
- Implement a real-world example to solidify the concepts.

## What are Ansible Roles?

Ansible roles are independent blocks of Ansible automation that can be reused and shared. A role bundles related tasks, variables, files, and handlers together, making it easier to manage complex playbooks by breaking them down into simpler, reusable components.

## What are Ansible Content Collections?

Ansible Content Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Collections allow you to organize, share, and use Ansible content across different playbooks and roles in a seamless manner.

## Step-by-Step Guide

### Step 1: Installing Ansible

Before you can use Ansible roles and content collections, you need to have Ansible installed on your system. You can install Ansible with the following command:

```bash
pip install ansible
```

### Step 2: Finding and Using Ansible Collections

Collections can be found and installed from Ansible Galaxy, the official hub for sharing Ansible content. To find a collection, you can use the `ansible-galaxy` command. For instance, to find collections related to AWS:

```bash
ansible-galaxy collection search aws
```

To install a specific collection, use:

```bash
ansible-galaxy collection install amazon.aws
```

### Step 3: Creating a Playbook that Uses a Collection

Once the collection is installed, you can use the roles and modules provided by the collection in your playbooks. Here’s an example playbook that uses a role from the `amazon.aws` collection to manage EC2 instances:

```yaml
---
- name: Manage EC2 Instances
  hosts: localhost
  gather_facts: false
  collections:
    - amazon.aws

  tasks:
    - name: Launch new EC2 Instance
      ec2:
        key_name: mykey
        instance_type: t2.micro
        image: ami-123456
        wait: yes
        group: webserver
        count: 1
        vpc_subnet_id: subnet-123456
        assign_public_ip: yes
```

### Step 4: Using Roles in Your Playbook

Roles can be either created by you or you can use pre-existing roles from Ansible Galaxy. To use a role from Galaxy, you first need to install it:

```bash
ansible-galaxy install geerlingguy.apache
```

Then, include the role in your playbook:

```yaml
---
- name: Configure Web Servers
  hosts: webservers
  roles:
    - role: geerlingguy.apache
```

This playbook applies the `geerlingguy.apache` role to all hosts in the `webservers` group.

## Detailed Code Examples

### Real-World Application: Deploying a LAMP Stack

Let's consider deploying a LAMP (Linux, Apache, MySQL, PHP) stack on a server using roles and collections. For this example, we will use existing roles from Ansible Galaxy and a collection for MySQL tasks.

1. **Install Required Roles and Collections**

```bash
ansible-galaxy install geerlingguy.apache
ansible-galaxy install geerlingguy.mysql
ansible-galaxy collection install community.mysql
```

2. **Create the Playbook**

```yaml
---
- name: Deploy LAMP Stack
  hosts: lamp-servers
  become: yes

  roles:
    - role: geerlingguy.apache
    - role: geerlingguy.mysql

  tasks:
    - name: Create a MySQL Database
      community.mysql.mysql_db:
        name: my_database
        state: present

    - name: Add a MySQL User
      community.mysql.mysql_user:
        name: dbuser
        password: strongpassword123
        priv: '*.*:ALL'
        state: present
```

## Conclusion

Ansible roles and collections simplify the management of complex automation tasks by modularizing and reusing code. By leveraging roles and collections, you can streamline your automation processes, ensuring consistency and reducing errors in deployments. This tutorial provided the foundational steps to start using Ansible roles and collections effectively in real-world scenarios.