# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In the realm of automation, efficiency and reusability of code are crucial. Ansible, a popular automation tool, allows users to scale their automation and manage complex deployments easily. In this tutorial, we will focus on two powerful features of Ansible: Roles and Content Collections. These features are essential for any Red Hat Certified System Administrator (RHCSA) looking to leverage Ansible for configuration management and application deployment on RHEL systems.

## What are Ansible Roles?

Ansible roles are discrete units of organization in Ansible, which allow you to segment your playbook into reusable components. Each role can include variables, tasks, files, templates, and modules that can be reused effectively in multiple playbooks.

## What are Ansible Content Collections?

Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Collections simplify the sharing and distribution of Ansible content and make it easier to manage playbook dependencies.

## Step-by-Step Guide

### Step 1: Installing Ansible on RHEL

Before you can use Ansible and its features like roles and collections, you need to install it on a RHEL system. You can install Ansible using the following command:

```bash
sudo dnf install ansible
```

### Step 2: Creating a Simple Role

Let’s create a simple role to understand how roles are structured and used in Ansible.

1. **Create Role Directory Structure**: You can manually create the directories or use the `ansible-galaxy` command to create a new role.

    ```bash
    ansible-galaxy init myrole
    ```

    This command creates a directory structure under `myrole` which includes directories like `tasks`, `handlers`, `templates`, `files`, `vars`, `defaults`, `meta`, etc.

2. **Add Tasks**: Edit the `myrole/tasks/main.yml` to include some tasks. Here, we will create a task to install and start nginx.

    ```yaml
    ---
    - name: Install nginx
      yum:
        name: nginx
        state: present

    - name: Start nginx
      systemd:
        name: nginx
        state: started
        enabled: Yes
    ```

### Step 3: Using the Role in a Playbook

Create a new playbook named `use_my_role.yml` and include the role that we just created:

```yaml
---
- hosts: all
  become: yes

  roles:
    - myrole
```

Run the playbook using:

```bash
ansible-playbook use_my_role.yml
```

### Step 4: Working with Ansible Content Collections

1. **Installing Collections**: You can install collections from Ansible Galaxy. For example, to install the nginx collection from `geerlingguy`, you would use:

    ```bash
    ansible-galaxy collection install geerlingguy.nginx
    ```

2. **Using Collections in Your Playbook**: Once you have the collection installed, you can use the roles or modules provided by the collection in your playbooks. Here’s an example playbook using the `geerlingguy.nginx` collection:

    ```yaml
    ---
    - hosts: all
      become: yes

      tasks:
        - name: Use nginx role from collection
          include_role:
            name: geerlingguy.nginx
    ```

## Detailed Code Examples

### Example 1: Using Variables in Roles

Roles can define default variables and also allow overriding them. Here’s how you can define and use variables in your role:

1. **Define Variables**: Inside your role, add default variables in `defaults/main.yml`.

    ```yaml
    nginx_version: "latest"
    ```

2. **Use Variables in Tasks**: Modify your tasks to use the variable.

    ```yaml
    - name: Install specific version of nginx
      yum:
        name: "nginx-{{ nginx_version }}"
        state: present
    ```

### Example 2: Templates in Roles

You can manage configuration files using templates in roles. Here’s a quick snippet:

1. **Create Template**: Create a template file in `templates/nginx.conf.j2`.

    ```jinja
    server {
        listen 80;
        server_name {{ ansible_hostname }};
        root /usr/share/nginx/html;
    }
    ```

2. **Use Template in Task**:

    ```yaml
    - name: Configure nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
    ```

## Conclusion

In this tutorial, we explored how to leverage Ansible roles and collections to modularize and reuse Ansible code effectively. By using roles, we can simplify the management of complex playbooks, and collections allow us to easily share and use Ansible content across different projects. As a Red Hat Certified System Administrator, mastering these tools will enable you to automate your RHEL systems efficiently and reliably.