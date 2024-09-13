# Tech Tutorial: Use Roles and Ansible Content Collections

In this tutorial, we'll delve into how to manage and utilize Ansible roles and content collections, essential tools for any Red Hat Certified Engineer (RHCE) looking to streamline their automation strategies using Ansible. We'll specifically focus on how to install and use these roles within playbooks on a system running Red Hat Enterprise Linux (RHEL).

## Introduction

### What are Ansible Roles?
Ansible roles are units of organization in Ansible, which allow you to abstract and encapsulate configurations for reuse and simplification. They make playbook writing easier and more manageable by grouping related tasks, handlers, files, templates, and variables into a standalone, reusable structure.

### What are Ansible Content Collections?
Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Collections allow you to package and distribute all your automation jobs, making it easier to share and reuse Ansible content across projects and teams.

## Step-by-Step Guide

### 1. Setting Up Your Environment
Before you begin, ensure you have Ansible installed on your RHEL system. You can install Ansible using the following command with the RHEL package manager:

```bash
sudo dnf install ansible
```

### 2. Installing Ansible Roles
Ansible Galaxy is a hub for finding and sharing Ansible content. To install a role from Ansible Galaxy, you can use the `ansible-galaxy` command. For instance, to install a role called `nginx`, run:

```bash
ansible-galaxy install nginx
```

This command downloads the `nginx` role to your default roles directory (typically `~/.ansible/roles`).

### 3. Using Roles in Playbooks
To utilize an installed role in your playbook, you need to incorporate it within your playbook YAML file. Here is an example of how to include the `nginx` role in a playbook:

```yaml
---
- hosts: web_servers
  become: yes
  roles:
    - nginx
```

This playbook applies the `nginx` role to hosts in the `web_servers` group.

### 4. Installing Ansible Collections
You can also install collections from Ansible Galaxy. For example, to install a collection named `ansible.builtin`, you would use:

```bash
ansible-galaxy collection install ansible.builtin
```

### 5. Using Collections in Playbooks
After installing a collection, you can use the modules contained within it in your playbooks. Here’s how you might use a module from the `ansible.builtin` collection:

```yaml
---
- hosts: all
  tasks:
    - name: Ensure a file is present using the 'file' module from the 'ansible.builtin' collection
      ansible.builtin.file:
        path: /tmp/testfile
        state: touch
```

This task uses the `file` module from the `ansible.builtin` collection to ensure a file exists.

## Detailed Code Examples

Let’s create a more complex playbook that uses both a role and a collection. Suppose we want to deploy a WordPress site on a RHEL server using the `nginx` role from Galaxy and the `mysql` module from the `community.mysql` collection.

First, install the necessary role and collection:

```bash
ansible-galaxy install nginx
ansible-galaxy collection install community.mysql
```

Next, create a playbook like this:

```yaml
---
- hosts: web_servers
  become: yes
  roles:
    - role: nginx
  tasks:
    - name: Create a database for WordPress
      community.mysql.mysql_db:
        name: wordpress
        state: present
```

This playbook first applies the `nginx` role to set up Nginx and then creates a MySQL database named `wordpress` using a module from the `community.mysql` collection.

## Conclusion

Using Ansible roles and collections can significantly simplify the management and deployment of configurations across your infrastructure. By encapsulating configurations into roles and organizing various modules and plugins into collections, you can create cleaner, more maintainable Ansible playbooks. Whether you're automating tasks for a few servers or an entire data center, mastering roles and collections is a crucial skill for any RHCE.

Hopefully, this tutorial provides you with a solid foundation for using Ansible roles and collections effectively in your RHEL environment. Remember, practice is key to mastering these tools, so continue experimenting with different configurations and scenarios to enhance your automation skills.