# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In Ansible, roles and collections are powerful components that enable reusable, shareable, and scalable automation practices. Roles allow you to organize your tasks, handlers, files, templates, and variables into a structured directory layout. Collections, introduced in Ansible 2.10, further extend this by bundling roles, modules, plugins, and documentation into a single package.

This tutorial aims to guide you through the process of installing roles, using them in playbooks, and leveraging Ansible Content Collections. By the end of this tutorial, you will have a clear understanding of how to structure your Ansible projects more effectively and maintain cleaner codebases.

## Step-by-Step Guide

### Pre-requisites

1. Ansible installed (version 2.9 or later is recommended).
2. Access to a command-line terminal.
3. Basic understanding of YAML and Ansible fundamentals.

### Step 1: Installing Roles

#### Using Ansible Galaxy

Ansible Galaxy is the official hub for sharing and finding Ansible content. To install a role from Ansible Galaxy, you can use the `ansible-galaxy` command:

```bash
ansible-galaxy install geerlingguy.apache
```

This command downloads the `apache` role by `geerlingguy` and installs it in your default roles directory (typically `~/.ansible/roles`).

#### Specifying a Version

To install a specific version of a role, use the `--version` parameter:

```bash
ansible-galaxy install geerlingguy.apache,2.0.1
```

### Step 2: Using Roles in Playbooks

Once a role is installed, you can incorporate it into your playbooks. Here’s a basic example:

```yaml
---
- name: Deploy Apache Web Server
  hosts: web_servers
  become: yes

  roles:
    - role: geerlingguy.apache
```

This playbook applies the `geerlingguy.apache` role to all hosts in the `web_servers` group.

#### Passing Parameters to Roles

Roles can be customized by passing parameters. For example, to change the document root:

```yaml
---
- name: Deploy Apache Web Server with custom docroot
  hosts: web_servers
  become: yes

  roles:
    - role: geerlingguy.apache
      apache_document_root: "/var/www/custom_docroot"
```

### Step 3: Using Ansible Content Collections

#### Installing Collections

You can install collections from Ansible Galaxy using the following command:

```bash
ansible-galaxy collection install community.general
```

#### Using Collections in Playbooks

To use elements from a collection in your playbook, you need to reference the collection. For instance, to use the `ping` module from the `community.general` collection:

```yaml
---
- name: Ping Test With Collection
  hosts: all
  tasks:
    - name: Ping test
      community.general.ping:
```

## Detailed Code Examples

### Example: Comprehensive Playbook Using Roles and Collections

```yaml
---
- name: Comprehensive Setup for Web Servers
  hosts: web_servers
  become: yes

  roles:
    - role: geerlingguy.apache
      apache_document_root: "/var/www/html"
    - role: geerlingguy.php
      php_webserver_daemon: "apache2"

  tasks:
    - name: Ensure nginx is not installed
      community.general.package:
        name: nginx
        state: absent

    - name: Fetch latest news
      community.general.git:
        repo: 'https://github.com/example/latest-news.git'
        dest: '/var/www/html/news'
```

## Conclusion

Roles and collections in Ansible offer a structured and efficient way to manage automation tasks. By encapsulating configuration and deployment logic, they facilitate code reuse and simplify playbook complexity. Whether you are managing simple web servers or complex multi-tier applications, roles and collections can help you achieve more with less code, enhancing maintainability and scalability of your Ansible projects.

Remember to explore Ansible Galaxy for roles and collections that can accelerate your automation goals. Happy automating!