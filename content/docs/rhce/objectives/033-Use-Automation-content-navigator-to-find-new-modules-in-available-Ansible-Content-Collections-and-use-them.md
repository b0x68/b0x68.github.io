# Tech Tutorial: Run Playbooks with Automation Content Navigator

## Introduction

In the realm of automation, staying updated with the latest tools and modules is crucial for enhancing efficiency and embracing best practices. Ansible, a popular open-source automation tool, continuously evolves, and its modules are frequently updated or newly introduced through Ansible Content Collections. This tutorial focuses on how you can leverage the Automation Content Navigator to discover new modules within these collections and effectively use them in your automation scripts. This skill is particularly vital for candidates preparing for the Red Hat Certified Engineer (RHCE) exam, focusing on RHEL-centric commands and practices.

## Prerequisites

Before proceeding with this tutorial, ensure you have the following:
- A Red Hat Enterprise Linux (RHEL) system, version 8 or later.
- Ansible installed on your RHEL system.
- Access to the internet to download necessary collections.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure that your Ansible environment is properly set up on your RHEL machine. Install Ansible using the following command:

```bash
sudo dnf install ansible
```

### Step 2: Discovering Ansible Collections

Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. To find new modules, you first need to explore available collections. You can search for collections from the command line using the following command:

```bash
ansible-galaxy collection search keyword
```

Replace `keyword` with a relevant term. For example, to search for collections related to Apache, you might use:

```bash
ansible-galaxy collection search apache
```

### Step 3: Installing a Collection

Once you identify a collection, you can install it using the following command:

```bash
ansible-galaxy collection install namespace.collection_name
```

For instance, to install the Apache content collection from the earlier search, you might use:

```bash
ansible-galaxy collection install apache.httpd
```

### Step 4: Exploring Modules in a Collection

After installing the collection, you can list all modules in that collection:

```bash
ansible-doc -l -t module namespace.collection_name.*
```

For example:

```bash
ansible-doc -l -t module apache.httpd.*
```

This command will list all modules within the `apache.httpd` collection.

### Step 5: Using a Module in a Playbook

Once you have the list of modules, you can start using them in your playbooks. Here's a simple example of using a module from the apache.httpd collection to ensure that the Apache service is running on your server:

```yaml
---
- name: Ensure Apache is Running
  hosts: all
  tasks:
    - name: Install Apache
      ansible.builtin.yum:
        name: httpd
        state: present

    - name: Start and enable Apache
      apache.httpd.httpd_service:
        state: started
        enabled: yes
```

Save this as `ensure_apache_running.yml` and run the playbook using:

```bash
ansible-playbook ensure_apache_running.yml
```

## Detailed Code Examples

Let’s consider a more complex scenario where you need to configure virtual hosts on your Apache server using the `apache.httpd` collection.

```yaml
---
- name: Configure Apache Virtual Hosts
  hosts: web_servers
  become: yes
  tasks:
    - name: Install Apache
      ansible.builtin.yum:
        name: httpd
        state: present

    - name: Configure Virtual Host
      apache.httpd.httpd_vhost:
        server_name: "example.com"
        document_root: "/var/www/html/example.com"
        state: present
```

Run this playbook as you did with the previous example.

## Conclusion

Using Automation Content Navigator to explore and utilize new modules in Ansible Collections can significantly streamline your automation tasks and ensure your systems are managed efficiently and in accordance with the latest standards. This practice not only prepares you for the RHCE exam but also enhances your capabilities as a system administrator or a DevOps engineer working within RHEL environments.

By staying updated with the latest collections and modules, you can ensure your automation scripts are robust, maintainable, and scalable.