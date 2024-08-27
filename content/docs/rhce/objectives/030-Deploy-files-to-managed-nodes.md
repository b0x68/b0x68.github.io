# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will focus on deploying files to managed nodes using Ansible, a powerful IT automation tool that can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

Our goal is to ensure that you can deploy files across multiple managed nodes efficiently and reliably. This is a critical skill in managing environments where configuration and consistency are vital for the application's performance and security.

## Prerequisites

Before proceeding, ensure you have the following:
- An Ansible control node, typically your workstation or a central server where Ansible is installed and from which you will run all commands.
- One or more managed nodes (servers) that are accessible via SSH from the control node.
- Proper SSH keys or username/password authentication set up for accessing the managed nodes.
- Python installed on all nodes (Python 2.7 or Python 3.5 and higher).

## Step-by-Step Guide

### Step 1: Setting Up Your Inventory

An inventory file defines the hosts and groups of hosts upon which commands, modules, and tasks in a playbook operate. The default location for an inventory file is `/etc/ansible/hosts`, but you can create it anywhere and use the `-i` option to point to the inventory file.

Here’s a simple example of an inventory file:

```ini
[webserver]
192.168.1.50
192.168.1.51

[databaseserver]
192.168.1.60
```

### Step 2: Writing Your First Playbook

A playbook is where you define what you want to happen on your remote systems. Here, we'll create a playbook to deploy a configuration file to all the nodes in the `webserver` group.

Create a file named `deploy_files.yml`:

```yaml
---
- name: Deploy configuration file to webservers
  hosts: webserver
  become: yes
  tasks:
    - name: Copy configuration file to remote nodes
      copy:
        src: /path/to/local/source/file.conf
        dest: /path/on/remote/file.conf
        owner: root
        group: root
        mode: '0644'
```

### Step 3: Running the Playbook

To run the playbook, use the `ansible-playbook` command:

```bash
ansible-playbook -i /path/to/your/inventory deploy_files.yml
```

This command will start executing the playbook on the hosts defined under the `webserver` group in your inventory.

## Detailed Code Examples

### Example 1: Deploying Multiple Files

To deploy multiple files, you can use the `with_fileglob` pattern to specify multiple files in a single task:

```yaml
---
- name: Deploy multiple configuration files to webservers
  hosts: webserver
  become: yes
  tasks:
    - name: Copy multiple configuration files
      copy:
        src: "{{ item }}"
        dest: "/path/on/remote/{{ item | basename }}"
      with_fileglob:
        - /path/to/local/source/*.conf
```

### Example 2: Using Variables for Dynamic File Deployment

You can also use variables in your playbook to make the file source and destination dynamic:

```yaml
---
- name: Deploy a configuration file using variables
  hosts: webserver
  become: yes
  vars:
    local_path: /path/to/local/source/file.conf
    remote_path: /path/on/remote/file.conf
  tasks:
    - name: Copy configuration file to remote nodes using variables
      copy:
        src: "{{ local_path }}"
        dest: "{{ remote_path }}"
        owner: root
        group: root
        mode: '0644'
```

## Conclusion

In this tutorial, we've covered how to set up an inventory, write a playbook, and deploy files to managed nodes using Ansible. These steps are fundamental in ensuring that your servers are configured consistently and automatically. As you grow more comfortable with Ansible's capabilities, you can expand your playbooks to handle more complex deployment scenarios and manage your infrastructure more effectively.