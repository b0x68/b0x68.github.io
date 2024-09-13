# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In the world of automated configuration and deployment, Ansible stands out for its simplicity and versatility. For Red Hat Certified Engineer (RHCE) candidates, understanding how to effectively utilize Ansible is crucial. This tutorial will delve into creating and working with roles and leveraging Ansible Content Collections, focusing specifically on Red Hat Enterprise Linux (RHEL).

Roles in Ansible are units of organization that allow for reusable content, making playbook development and maintenance easier. Ansible Content Collections, on the other hand, are a format for packaging and distributing Ansible content, including roles, plugins, and modules.

## Step-by-Step Guide

### Setup Ansible on RHEL

Before diving into roles and collections, ensure Ansible is installed on your RHEL system. You can install Ansible through the Red Hat Subscription Management (RHSM):

```bash
sudo subscription-manager repos --enable ansible-2-for-rhel-8-x86_64-rpms
sudo dnf install ansible
```

### Creating a Role

Roles organize tasks, handlers, files, templates, and variables into a structured directory. We will create a role to configure a web server.

1. **Create Role Directory Structure**

   Use the `ansible-galaxy` command to initialize a new role:

   ```bash
   ansible-galaxy init web_server
   ```

   This command creates a directory structure under `web_server`:

   ```
   web_server/
   ├── defaults
   │   └── main.yml
   ├── files
   ├── handlers
   │   └── main.yml
   ├── meta
   │   └── main.yml
   ├── README.md
   ├── tasks
   │   └── main.yml
   ├── templates
   ├── tests
   │   ├── inventory
   │   └── test.yml
   └── vars
       └── main.yml
   ```

2. **Add Tasks**

   Edit `web_server/tasks/main.yml` to install and start Apache:

   ```yaml
   ---
   - name: Install httpd
     yum:
       name: httpd
       state: present

   - name: Start httpd service
     systemd:
       name: httpd
       state: started
       enabled: yes
   ```

### Using the Role in a Playbook

Create a playbook `deploy_web.yml` that uses the `web_server` role:

```yaml
---
- hosts: all
  become: yes

  roles:
    - web_server
```

### Ansible Content Collections

Ansible Collections allow you to organize, share, and use roles across different projects.

1. **Creating a Collection**

   Initialize a new collection using `ansible-galaxy`:

   ```bash
   ansible-galaxy collection init my_namespace.my_collection
   ```

   This command generates a collection structure:

   ```
   my_collection/
   ├── docs/
   ├── galaxy.yml
   ├── plugins/
   │   └── modules/
   ├── README.md
   ├── roles/
   └── tests/
   ```

2. **Add Role to Collection**

   Move or link the `web_server` role into `my_collection/roles/`.

3. **Using Collection in a Playbook**

   Update `deploy_web.yml` to use the role from the collection:

   ```yaml
   ---
   - hosts: all
     become: yes

     collections:
       - my_namespace.my_collection

     roles:
       - web_server
   ```

## Detailed Code Examples

Here’s a more complex task included in the `web_server` role to configure virtual hosts:

```yaml
- name: Configure virtual hosts
  template:
    src: vhosts.j2
    dest: /etc/httpd/conf.d/{{ item.vhost_name }}.conf
  loop:
    - { vhost_name: 'site1', server_admin: 'webmaster@site1.com', document_root: '/var/www/site1' }
    - { vhost_name: 'site2', server_admin: 'webmaster@site2.com', document_root: '/var/www/site2' }
  notify: restart httpd
```

This task uses the `template` module to create virtual host configurations from a Jinja2 template, iterating over a list of virtual hosts.

## Conclusion

Understanding and utilizing roles and collections in Ansible can significantly streamline the process of managing complex deployments across various environments. By encapsulating configuration logic into roles and organizing roles into collections, you can reuse code efficiently and maintain cleaner, more manageable playbooks. This tutorial has shown you how to establish these components in a RHEL environment, providing a strong foundation for further exploration and proficiency in Ansible automation.