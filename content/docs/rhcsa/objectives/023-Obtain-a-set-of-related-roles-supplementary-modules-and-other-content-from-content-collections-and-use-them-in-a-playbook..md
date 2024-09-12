# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In this tutorial, we will explore how to leverage Ansible Roles and Content Collections to simplify and enhance your automation tasks. Specifically tailored for the Red Hat Certified System Administrator (RHCSA) exam, this guide will focus entirely on methodologies and commands pertinent to Red Hat Enterprise Linux (RHEL).

Ansible, an open-source automation tool, is powerful for managing complex IT workflows and configurations. By using roles and content collections, you can organize your playbooks more efficiently and reuse code across different projects.

## Prerequisites

Before we begin, ensure you have the following setup:

- A working RHEL 8 installation.
- Ansible installed on your RHEL system. You can install Ansible using the following command:

  ```bash
  sudo dnf install ansible
  ```

- Access to the internet to download necessary content collections.

## Step-by-Step Guide

### Step 1: Understanding Ansible Roles

An Ansible Role is a way of bundling automation content and making it reusable. Each role can include variables, handlers, files, templates, and tasks.

#### Creating a Basic Role

Let’s create a simple role named `webserver` that installs and starts Nginx.

1. Create a directory structure for your Role:

   ```bash
   mkdir -p ~/ansible-roles/webserver/{tasks,handlers,files,templates,vars}
   ```

2. In the `tasks` directory, create a main.yml file:

   ```yaml
   # ~/ansible-roles/webserver/tasks/main.yml
   ---
   - name: Install Nginx
     yum:
       name: nginx
       state: present

   - name: Start Nginx
     service:
       name: nginx
       state: started
       enabled: yes
   ```

### Step 2: Using Ansible Content Collections

Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins.

#### Installing a Content Collection

For this example, we’ll use a community collection to manage SELinux policies.

1. Install the `ansible.posix` collection from Ansible Galaxy:

   ```bash
   ansible-galaxy collection install ansible.posix
   ```

#### Integrating Collection in a Playbook

1. Create a new playbook `setup.yml`:

   ```yaml
   # setup.yml
   ---
   - hosts: all
     become: yes
     tasks:
       - name: Ensure SELinux is enforcing
         ansible.posix.seboolean:
           name: httpd_can_network_connect
           state: yes
           persistent: yes
   ```

### Step 3: Combining Roles and Collections in a Playbook

Now, let’s create a playbook that uses both the `webserver` role and the `ansible.posix` collection.

1. Create a playbook `site.yml`:

   ```yaml
   # site.yml
   ---
   - hosts: all
     become: yes
     roles:
       - webserver
     collections:
       - ansible.posix

     tasks:
       - name: Ensure SELinux is permissive
         ansible.posix.seboolean:
           name: httpd_can_network_connect
           state: yes
           persistent: yes
   ```

## Detailed Code Examples

The example below demonstrates a more complex playbook integrating multiple roles and collections.

```yaml
# complex_site.yml
---
- hosts: all
  become: yes
  roles:
    - webserver
    - dbserver
  collections:
    - ansible.posix
    - community.mysql

  tasks:
    - name: Ensure SELinux is permissive for MySQL
      ansible.posix.seboolean:
        name: mysql_connect_any
        state: yes
        persistent: yes

    - name: Create a new MySQL database
      community.mysql.mysql_db:
        name: my_database
        state: present
```

## Conclusion

In this tutorial, we've seen how to effectively use Ansible roles and content collections. By structuring your automation tasks into reusable components, you can greatly simplify and expedite your workflow. Remember to explore more roles and collections available in Ansible Galaxy to further enhance your automation capabilities. This approach not only aligns with best practices but also prepares you for tasks you may encounter in the RHCSA exam.