# Tech Tutorial: Understand Core Components of Ansible – Conditional Tasks

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration management, application deployment, and task automation. It uses a simple, yet powerful, declarative language to describe automation jobs in YAML format. One of the key features of Ansible that enhances its flexibility and control is the ability to use conditional tasks. Conditional tasks allow you to execute tasks based on specific conditions. This tutorial dives deep into conditional tasks, showcasing how to effectively utilize them to make your automation scripts smarter and more efficient.

## Step-by-Step Guide

In this section, we will explore how to implement conditional tasks in Ansible. We will start by setting up a simple Ansible environment, then move on to basic conditional executions, and progressively delve into more complex scenarios.

### Setting Up Your Ansible Environment

Before diving into conditional tasks, you need to have Ansible installed on your control machine (the machine that will run the automation scripts). Here's how you can install Ansible on a Linux-based system:

```bash
sudo apt update
sudo apt install ansible
```

Ensure that Ansible is installed correctly:

```bash
ansible --version
```

### Understanding Basic Conditional Tasks

Conditional tasks in Ansible are primarily handled using the `when` statement. This statement decides whether a task should execute based on the condition's truthiness.

#### Example 1: Checking for OS Family

Consider a scenario where you need to install a package only if the operating system is Ubuntu. Here's how you can do it:

```yaml
---
- hosts: all
  tasks:
    - name: Install a package on Ubuntu
      apt:
        name: git
        state: present
      when: ansible_facts['os_family'] == "Debian"
```

In this example, the task to install `git` will only run if the `os_family` is Debian (which includes Ubuntu).

### Using Multiple Conditions

You can also use multiple conditions combined with logical operators like `and`, `or`, and `not`.

#### Example 2: Checking for Multiple Conditions

Suppose you want to install a package only if the operating system is CentOS 7 or higher. Here’s how you can achieve this:

```yaml
---
- hosts: all
  tasks:
    - name: Install a package on CentOS 7 or higher
      yum:
        name: git
        state: present
      when: 
        - ansible_facts['os_family'] == "RedHat"
        - ansible_facts['distribution_major_version'] | int >= 7
```

### Conditional Execution in Loops

Ansible also allows conditional executions within loops. This is useful when you need to apply the same task under varying conditions for different items in a list.

#### Example 3: Conditional Execution in Loops

Let's say you have a list of packages, but some should only be installed based on certain conditions:

```yaml
---
- hosts: all
  tasks:
    - name: Install multiple packages conditionally
      yum:
        name: "{{ item.name }}"
        state: present
      loop:
        - { name: 'git', install_on: 'RedHat' }
        - { name: 'vim', install_on: 'Debian' }
      when: ansible_facts['os_family'] == item.install_on
```

## Detailed Code Examples

Let's create a more complex playbook that involves setting up a web server with conditions.

### Example 4: Complex Conditional Playbook

```yaml
---
- hosts: web_servers
  tasks:
    - name: Install nginx on Ubuntu
      apt:
        name: nginx
        state: present
      when: ansible_facts['distribution'] == 'Ubuntu'

    - name: Start nginx service
      service:
        name: nginx
        state: started
      when: ansible_facts['distribution'] == 'Ubuntu'

    - name: Copy the index.html file for Ubuntu Servers
      copy:
        src: /src/index-ubuntu.html
        dest: /var/www/html/index.html
      when: ansible_facts['distribution'] == 'Ubuntu'
```

## Conclusion

Conditional tasks in Ansible provide a powerful way to control the flow of execution in your playbooks. By understanding and utilizing conditions, you can create more dynamic, efficient, and adaptable automation scripts. Whether you're managing configurations across different environments or deploying applications conditionally, mastering conditional tasks is crucial for any Ansible user.