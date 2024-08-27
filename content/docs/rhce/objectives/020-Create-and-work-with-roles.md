# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In this tutorial, we will dive deep into two powerful features of Ansible: Roles and Ansible Content Collections. These features help in organizing and reusing Ansible code, making automation more efficient and manageable. By the end of this tutorial, you will learn how to create, structure, and use roles within your playbooks. Additionally, we'll explore how to incorporate Ansible Content Collections, which package and distribute plugins, roles, modules, and playbooks.

## Prerequisites

Before we start, ensure you have the following installed:
- Ansible 2.9 or later
- Access to at least one managed node (Linux-based)
- SSH access set up for the managed node(s)

## Step-by-Step Guide

### Part 1: Creating and Using Roles

#### Step 1: Setting Up Your Environment

First, create a directory for your project:

```bash
mkdir -p ansible-project/roles
cd ansible-project
```

#### Step 2: Creating a Role

Let's create a role named `webserver`. This role will be responsible for setting up a Nginx web server.

```bash
ansible-galaxy init roles/webserver
```

This command creates a directory structure under `roles/webserver` with all the necessary subdirectories like `tasks`, `handlers`, `templates`, `files`, `vars`, `defaults`, `meta`, and `tests`.

#### Step 3: Defining Tasks

Edit the `roles/webserver/tasks/main.yml` to include tasks for installing Nginx and starting the service:

```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  become: yes

- name: Start Nginx
  service:
    name: nginx
    state: started
  become: yes
```

#### Step 4: Using the Role in a Playbook

Create a playbook named `setup-webserver.yml` in the root of your `ansible-project` directory:

```yaml
---
- hosts: all
  roles:
    - webserver
```

#### Step 5: Running Your Playbook

Run the playbook against your managed nodes:

```bash
ansible-playbook -i hosts setup-webserver.yml
```

### Part 2: Working with Ansible Content Collections

#### Step 6: Discovering Collections

Find a collection that suits your needs. For instance, the `community.general` collection provides a variety of general-purpose modules and plugins.

```bash
ansible-galaxy collection search community.general
```

#### Step 7: Installing a Collection

Install the `community.general` collection:

```bash
ansible-galaxy collection install community.general
```

#### Step 8: Using a Collection in a Playbook

Modify your playbook to use a module from the `community.general` collection. For example, use the `pip` module to install a Python package:

```yaml
---
- hosts: all
  tasks:
    - name: Install requests
      community.general.pip:
        name: requests
        state: present
```

## Detailed Code Examples

Here are more examples of using roles and collections to give you a better understanding:

### Example 1: Role with Variables

In `roles/webserver/vars/main.yml`, define:

```yaml
http_port: 8080
```

Modify `roles/webserver/tasks/main.yml` to use the variable:

```yaml
- name: Start Nginx on a specific port
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify:
    - restart nginx
```

### Example 2: Using Handlers

Add a handler in `roles/webserver/handlers/main.yml`:

```yaml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```

## Conclusion

Roles and Collections in Ansible provide a robust way to reuse automation logic and manage dependencies efficiently. By modularizing tasks and utilizing community resources, you can streamline your Ansible workflows and maintain cleaner, more scalable codebases. Keep exploring more collections and roles to see how they can fit into your automation strategies.