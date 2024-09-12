# Tech Tutorial: Create Ansible Plays and Playbooks with Conditionals

## Introduction

In this tutorial, we will explore how to use conditionals to control play execution in Ansible, which is a crucial skill for the Red Hat Certified System Administrator (RHCSA) exam. Ansible is an open-source automation tool that allows you to automate tasks across multiple systems. This tutorial is tailored specifically for Red Hat Enterprise Linux (RHEL) environments.

Conditionals in Ansible are used to execute different tasks based on specified conditions. This feature is particularly useful in managing complex environments with diverse configurations and requirements.

## Prerequisites

To follow this tutorial, you should have:

- A working RHEL system.
- Ansible installed on your RHEL system. You can install Ansible with `yum install ansible` on RHEL.
- Basic familiarity with YAML syntax and Ansible basics.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

Before writing our playbook, let's set up a simple inventory file. Create a file named `hosts` in your working directory:

```ini
[webserver]
192.168.1.101

[database]
192.168.1.102
```

### Step 2: Understanding Ansible Conditionals

Ansible uses the `when` statement to apply conditionals. These conditionals decide whether a particular task should be executed or skipped based on the evaluation of a condition.

### Step 3: Writing a Basic Playbook with Conditionals

Let's create a playbook named `conditional_playbook.yml`. This playbook will check whether certain packages are installed on the server and install them if they are not present.

```yaml
---
- name: Conditional Play Execution
  hosts: all
  become: yes
  tasks:
    - name: Check if 'httpd' is installed on web servers
      yum:
        list: httpd
      register: httpd_installed
      when: inventory_hostname in groups['webserver']

    - name: Install 'httpd' if it is not installed
      yum:
        name: httpd
        state: present
      when: httpd_installed.results|length == 0 and inventory_hostname in groups['webserver']

    - name: Check if 'postgresql' is installed on database servers
      yum:
        list: postgresql-server
      register: postgresql_installed
      when: inventory_hostname in groups['database']

    - name: Install 'postgresql-server' if it is not installed
      yum:
        name: postgresql-server
        state: present
      when: postgresql_installed.results|length == 0 and inventory_hostname in groups['database']
```

### Explanation of the Playbook

1. **Tasks to Check Installation**: The first and third tasks check if 'httpd' and 'postgresql-server' are installed on the respective groups of servers. The result of the check is registered in a variable.

2. **Conditional Installation Tasks**: The second and fourth tasks install 'httpd' and 'postgresql-server' only if they are not installed. This is determined by checking the length of the results list in the registered variables.

### Step 4: Running the Playbook

To run the playbook, use the following command:

```bash
ansible-playbook -i hosts conditional_playbook.yml
```

## Detailed Code Examples

Let's delve deeper with another example involving multiple conditions:

### Advanced Conditional Playbook

Suppose we need to apply security updates only if they are available and if the server is a production server. In such cases, we can use complex conditionals:

```yaml
---
- name: Conditional Security Updates
  hosts: all
  become: yes
  vars:
    is_production: false  # This should be set based on your environment

  tasks:
    - name: Check for security updates
      yum:
        list: security
      register: security_updates
      when: is_production

    - name: Apply security updates
      yum:
        name: '*'
        state: latest
        security: yes
      when: 
        - security_updates.results|length > 0
        - is_production
```

## Conclusion

Using conditionals in Ansible allows you to build more flexible and powerful automation scripts tailored to the specific needs of your environment. By incorporating conditionals based on the characteristics of your systems and requirements, you can ensure that tasks are only executed when necessary, improving efficiency and reducing the risk of errors. Whether you are preparing for the RHCSA exam or looking to enhance your Ansible skills, mastering conditionals is a vital step in becoming an effective Ansible user.