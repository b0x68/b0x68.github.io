# Tech Tutorial: Run Playbooks with Automation Content Navigator

## Introduction

In this tutorial, we will explore how to utilize Automation Content Navigator, specifically focusing on creating inventories and configuring the Ansible environment to efficiently manage and execute Ansible playbooks. Automation Content Navigator is a powerful tool for managing automation content across various environments, making it crucial for those seeking to streamline their automation workflows.

## Prerequisites

Before we begin, ensure you have the following:

- Access to an Automation Content Navigator instance.
- Ansible installed on your local machine or on a server you have access to.
- Basic understanding of YAML and Ansible playbook structure.

## Step-by-Step Guide

### Step 1: Accessing Automation Content Navigator

First, you need to log in to your Automation Content Navigator interface. This is typically accessed through a web interface provided by your organization.

```plaintext
URL: http://your-automation-content-navigator-url
Username: your-username
Password: your-password
```

### Step 2: Creating an Inventory

An inventory is a collection of hosts against which you can run Ansible playbooks. Here's how to create one in Automation Content Navigator:

1. **Navigate to the Inventory Section**: Once logged in, find the "Inventories" section in the dashboard or sidebar.
2. **Create a New Inventory**: Click on "Add Inventory" or a similar button. You'll be prompted to enter details such as name and description.
3. **Add Hosts**: Enter the hosts' details. You can specify hosts individually by IP addresses or domain names, or use ranges or patterns.

```yaml
all:
  hosts:
    server1.example.com:
    server2.example.com:
  children:
    webservers:
      hosts:
        server1.example.com:
    dbserver:
      hosts:
        server2.example.com:
```

4. **Save the Inventory**: After adding all necessary hosts and organizing them as needed (e.g., by groups), save the inventory.

### Step 3: Configuring the Ansible Environment

To configure Ansible to use the inventory you just created:

1. **Set Up Ansible Configuration**: Create or edit an `ansible.cfg` file in your working directory or globally in `/etc/ansible/ansible.cfg`. Ensure it points to your newly created inventory.

```ini
[defaults]
inventory = /path/to/your/inventory/file
host_key_checking = False
remote_user = your-remote-user
```

2. **Environment Variables**: Set necessary environment variables, if any, such as credentials for accessing managed nodes.

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_REMOTE_USER=your-remote-user
```

### Step 4: Running an Ansible Playbook

With your inventory set and environment configured, you can now run an Ansible playbook.

1. **Create a Simple Playbook**: For demonstration, let's create a playbook that installs nginx on all webservers.

```yaml
---
- name: Install Nginx
  hosts: webservers
  become: yes
  tasks:
    - name: Ensure nginx is at the latest version
      apt:
        name: nginx
        state: latest
```

2. **Execute the Playbook**: Run the playbook using the `ansible-playbook` command.

```bash
ansible-playbook -i /path/to/your/inventory/file install-nginx.yml
```

## Detailed Code Examples

Here are additional examples to deepen your understanding:

### Advanced Inventory Setup

```yaml
all:
  vars:
    ansible_user: admin
  children:
    production:
      hosts:
        prod-server1.example.com:
        prod-server2.example.com:
    staging:
      hosts:
        stage-server1.example.com:
```

### Complex Playbook Example

```yaml
---
- name: Configure Web and DB Servers
  hosts: all
  become: true
  roles:
    - common
    - { role: webserver, when: "'webservers' in group_names" }
    - { role: dbserver, when: "'dbservers' in group_names" }
```

## Conclusion

Automation Content Navigator simplifies the process of managing and executing Ansible playbooks across various environments. By creating well-organized inventories and properly configuring the Ansible environment, you can enhance automation strategies and ensure more consistent, reliable deployments. With the foundational knowledge from this tutorial, you're now equipped to explore more complex scenarios and integrate them into your automation workflows.