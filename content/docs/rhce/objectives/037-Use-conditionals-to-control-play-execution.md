# Tech Tutorial: Create Ansible Plays and Playbooks with Conditionals

## Introduction

Ansible is a powerful automation tool that can manage the state of your servers. It uses simple YAML syntax in its playbooks to define the tasks to be executed. One of the key features of Ansible is the ability to control the flow of execution using conditionals. This tutorial will guide you through the process of using conditionals to control play execution in Ansible, ensuring that certain tasks are only run when specific conditions are met.

## Prerequisites

Before we begin, ensure you have the following:
- Ansible installed on your control machine. 
- At least one managed node (or more), which are the servers where Ansible will execute tasks.
- SSH access from your control machine to your managed nodes.

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

First, you need to define your hosts in Ansible’s inventory. This is typically done in a file named `hosts.ini`. Here’s a simple example:

```ini
[webserver]
192.168.1.100

[database]
192.168.1.101
```

### Step 2: Understanding Ansible Conditionals

Ansible uses the `when` statement to include conditionals. These can be based on the facts gathered about the hosts or variables you define.

### Step 3: Writing Your First Conditional Playbook

Let’s create a playbook that installs Apache on a webserver only if it isn’t already installed.

Create a file named `install_apache.yml`:

```yaml
---
- name: Install Apache on webservers
  hosts: webserver
  become: yes
  tasks:
    - name: Check if Apache is installed
      command: which httpd
      ignore_errors: true
      register: apache_installed

    - name: Install Apache
      yum:
        name: httpd
        state: present
      when: apache_installed.rc != 0
```

**Explanation:**
- The `which httpd` command checks if Apache is installed. The `ignore_errors: true` ensures the playbook doesn’t fail if the command finds that Apache is not installed.
- The result of the command is registered under the variable `apache_installed`.
- The installation task for Apache runs only if the return code (`rc`) of the previous command is not 0 (which means Apache wasn’t found).

### Step 4: Running Your Playbook

To run your playbook, use the following command:

```bash
ansible-playbook -i hosts.ini install_apache.yml
```

### Step 5: Extending Use of Conditionals

You can also use Ansible facts and more complex expressions in your conditionals. Here’s an example that only runs tasks on Ubuntu servers:

```yaml
---
- name: Conditional tasks based on OS type
  hosts: all
  become: yes
  tasks:
    - name: Install Apache on Ubuntu
      apt:
        name: apache2
        state: present
      when: ansible_os_family == "Debian"

    - name: Install Apache on CentOS
      yum:
        name: httpd
        state: present
      when: ansible_os_family == "RedHat"
```

**Explanation:**
- `ansible_os_family` is a fact gathered by Ansible about the host’s operating system. This playbook uses it to determine which package manager to use.

## Detailed Code Examples

### Implementing Loops with Conditionals

You can combine loops with conditionals. Here’s an example where multiple packages are conditionally installed based on whether they are already on the system:

```yaml
---
- name: Install multiple packages conditionally
  hosts: all
  become: yes
  vars:
    packages:
      - httpd
      - vim
      - git
  tasks:
    - name: Check if packages are installed
      command: "which {{ item }}"
      loop: "{{ packages }}"
      register: package_check
      ignore_errors: true

    - name: Install packages if not present
      yum:
        name: "{{ item.item }}"
        state: present
      loop: "{{ package_check.results }}"
      when: item.rc != 0
```

## Conclusion

Using conditionals in Ansible plays and playbooks allows you to create more flexible and intelligent automation scripts. By controlling task execution based on the state of your hosts or defined variables, you can ensure that your automation is both efficient and effective. Continue exploring Ansible’s capabilities to enhance your infrastructure management strategies.