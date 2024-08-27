# Tech Tutorial: Understand Core Components of Ansible - Variables

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and system administration activities. It leverages straightforward YAML syntax to define automation jobs, known as "playbooks". A crucial feature of Ansible that enhances its flexibility and power is the use of variables. Variables in Ansible allow you to manage differences between systems, environments, and users in a structured and scalable way.

In this tutorial, we will delve deep into the concept of variables in Ansible. We will explore different types of variables, how they can be defined and used, and some best practices for leveraging variables effectively in your Ansible playbooks.

## Step-by-Step Guide

### 1. Understanding Variable Types

Ansible supports several types of variables:

- **Global Scope Variables:** These are set by Ansible configuration settings or command line parameters.
- **Playbook Variables:** Defined at the playbook level.
- **Host Variables:** Specific to host machines.
- **Group Variables:** Applied to groups of hosts.
- **Role Variables:** Defined within roles.
- **Fact Variables:** Gathered from target machines via facts.

### 2. Defining Variables

Variables can be defined in multiple places:

- **In Playbooks:** Directly inside a playbook.
- **In Inventory Files:** Alongside hosts or groups in the inventory.
- **In Separate Files:** Typically under a `vars/` directory or `group_vars/` and `host_vars/` subdirectories.
- **In Roles:** Inside roles, typically under `defaults/` or `vars/`.

#### Example: Defining Variables in a Playbook

A simple playbook with variables might look like this:

```yaml
---
- hosts: all
  vars:
    http_port: 80
    max_clients: 200
  tasks:
  - name: Set up a web server
    ansible.builtin.yum:
      name: httpd
      state: present
    notify: restart apache

  handlers:
  - name: restart apache
    ansible.builtin.service:
      name: httpd
      state: restarted
```

### 3. Using Variables in Tasks

Variables can be referenced in tasks using Jinja2 templating system:

```yaml
---
- hosts: all
  tasks:
  - name: Echo a variable
    ansible.builtin.debug:
      msg: "The HTTP port is {{ http_port }}"
```

### 4. Variable Precedence

Ansible resolves variable precedence in a specific order, which affects which value is used when multiple definitions are available:

1. Role defaults
2. Inventory file or script group vars
3. Inventory group_vars/all
4. Playbook group_vars/all
5. Inventory group_vars/*
6. Playbook group_vars/*
7. Inventory file or script host vars
8. Inventory host_vars/*
9. Playbook host_vars/*
10. Host facts
11. Play vars
12. Play vars_prompt
13. Play vars_files
14. Role vars (defined in role/vars/main.yml)
15. Block vars (only for tasks in block)
16. Task vars (only for the task)
17. Include vars
18. Set_facts / registered vars
19. Extra vars (always win precedence)

### 5. Practical Examples

#### Example: Using Variables with Facts

```yaml
---
- hosts: all
  tasks:
  - name: Print OS family
    ansible.builtin.debug:
      msg: "The OS family is {{ ansible_os_family }}"
```

This task uses the fact variable `ansible_os_family`, which is automatically gathered by Ansible.

## Conclusion

Variables in Ansible provide a dynamic and flexible way to execute automation tasks across different environments and conditions. By understanding the different types of variables, how to define them, and their precedence, you can create robust and adaptable playbooks. Whether you are automating routine tasks or deploying complex applications, mastering variables in Ansible will significantly enhance your automation capabilities.