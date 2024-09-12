# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

Ansible, a powerful IT automation tool, simplifies complex configuration tasks, deployment, and orchestration. In this tutorial, we will focus on two significant aspects of Ansible: Content Collections and Roles. These features help in organizing and reusing Ansible content more efficiently, which is crucial for maintaining large environments or multiple projects.

Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Roles, on the other hand, are units of organization that allow users to group resources that belong together logically, making the playbook more manageable and reusable.

This tutorial aligns with the Red Hat Certified Systems Administrator (RHCSA) exam requirements and focuses on RHEL (Red Hat Enterprise Linux) commands and configurations.

## Prerequisites

- A Red Hat Enterprise Linux 8 system.
- Ansible installed on your RHEL system. You can install Ansible using the following command:
  ```bash
  sudo dnf install ansible
  ```

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure that your system is ready and Ansible is installed. You can check the version of Ansible to confirm the installation:
```bash
ansible --version
```

### Step 2: Discovering Ansible Collections

Ansible Collections can be found and installed from Ansible Galaxy, the official hub for sharing Ansible content. To search for a specific collection, use:
```bash
ansible-galaxy collection search <collection_name>
```

For example, to search for collections related to nginx, you would run:
```bash
ansible-galaxy collection search nginx
```

### Step 3: Installing an Ansible Collection

Once you've identified the collection you want, you can install it using:
```bash
ansible-galaxy collection install <namespace.collection_name>
```

For instance, to install the nginx collection from the community:
```bash
ansible-galaxy collection install community.nginx
```

This command installs the collection in your default Collections path, which is `~/.ansible/collections`.

### Step 4: Using a Collection in a Playbook

After installing the collection, you can use the modules provided by the collection in your playbooks. Here’s a basic example of using the `community.nginx.nginx_status_facts` module in a playbook:

```yaml
---
- name: Retrieve nginx status facts
  hosts: all
  tasks:
    - name: Get nginx status facts
      community.nginx.nginx_status_facts:
```

This playbook gathers nginx status facts from your hosts using the nginx module from the `community.nginx` collection.

### Step 5: Understanding and Creating Roles

Roles are a way to organize tasks and other files needed to complete those tasks. To create a role, use:
```bash
ansible-galaxy init role_name
```

For example, to create a role named `nginx_setup`:
```bash
ansible-galaxy init nginx_setup
```

This command creates a directory structure for the role under the current directory.

### Step 6: Using Roles in a Playbook

Here’s how you can use the `nginx_setup` role in a playbook:

```yaml
---
- name: Setup nginx
  hosts: all
  roles:
    - nginx_setup
```

This playbook applies the `nginx_setup` role to all hosts, executing the tasks defined within that role.

## Detailed Code Examples

Below is a more comprehensive playbook example that uses both a role and a collection:

```yaml
---
- name: Complete Web Server Setup
  hosts: web_servers
  roles:
    - nginx_setup
  tasks:
    - name: Install and configure PHP
      community.nginx.php_fpm:
        state: present
        max_children: 50
        start_servers: 5
        max_requests: 500
```

This playbook is targeted at a group of hosts labeled `web_servers`. It applies the `nginx_setup` role and also configures PHP using a module from the `community.nginx` collection.

## Conclusion

In this tutorial, we've covered how to find, install, and use Ansible Collections and how to create and use roles within your Ansible playbooks. These tools not only help in organizing your Ansible environment but also simplify the reuse of code, making your automation tasks more efficient and manageable. With these skills, you'll be well-prepared to tackle real-world automation challenges in your Red Hat Enterprise Linux environments.