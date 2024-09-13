# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and consistent IT application environments. It is particularly popular for its simplicity and flexibility in managing various hosts through a central point. In this tutorial, we'll focus on how to deploy files to managed nodes using Ansible, specifically tailored for Red Hat Enterprise Linux (RHEL) environments, as per the requirements for the Red Hat Certified Engineer (RHCE) exam.

## Prerequisites

Before diving into the deployment process, ensure you have the following:
- A control node with Ansible installed. This is typically your workstation or a central server where Ansible will be run from.
- One or more managed nodes running RHEL.
- SSH access configured from the control node to each managed node.
- Sudo privileges on the managed nodes for the user Ansible will use to connect.

## Step-by-Step Guide

### Step 1: Install Ansible on Control Node

To install Ansible on your RHEL control node, you can use the following command:

```bash
sudo yum install ansible
```

### Step 2: Configure Inventory File

Ansible uses an inventory file to keep track of the servers it is managing. Here's how you can set up a basic inventory file:

1. Create a directory for your Ansible project:

   ```bash
   mkdir ~/ansible-deployment
   cd ~/ansible-deployment
   ```

2. Create an inventory file named `hosts` in this directory:

   ```bash
   touch hosts
   ```

3. Add your managed nodes to the `hosts` file. For example:

   ```ini
   [managed_nodes]
   node1.example.com
   node2.example.com
   ```

### Step 3: Create a Playbook to Deploy Files

Ansible uses playbooks written in YAML to define tasks for managing nodes. Here’s how to create a playbook to deploy a file:

1. Create a file named `deploy_file.yml` in the `ansible-deployment` directory:

   ```bash
   touch deploy_file.yml
   ```

2. Add the following content to `deploy_file.yml`:

   ```yaml
   ---
   - name: Deploy file to managed nodes
     hosts: managed_nodes
     become: yes  # Ensure you have sudo privileges
     tasks:
       - name: Copy file to managed node
         copy:
           src: /path/to/local/source/file.txt
           dest: /path/to/destination/on/managed/node/file.txt
           owner: root
           group: root
           mode: '0644'
   ```

   This playbook contains a single task that copies a file from the control node to the managed nodes.

### Step 4: Run the Playbook

To execute the playbook, use the `ansible-playbook` command:

```bash
ansible-playbook -i hosts deploy_file.yml
```

This command tells Ansible to use the `hosts` inventory file and execute the `deploy_file.yml` playbook.

## Detailed Code Examples

Let's delve deeper with another example where we deploy multiple files and ensure they contain specific content:

1. Modify the playbook `deploy_file.yml` to include additional tasks:

   ```yaml
   ---
   - name: Deploy multiple files with specific content to managed nodes
     hosts: managed_nodes
     become: yes
     tasks:
       - name: Ensure destination directory exists
         file:
           path: /path/to/destination/
           state: directory
           mode: '0755'
       
       - name: Deploy configuration file
         template:
           src: /path/to/template/myconfig.j2
           dest: /path/to/destination/myconfig.conf
           owner: root
           group: root
           mode: '0644'
   ```

   Here, `template` is used instead of `copy` to allow parameterization of the file's content.

2. Run the playbook again:

   ```bash
   ansible-playbook -i hosts deploy_file.yml
   ```

## Conclusion

This tutorial covered the essentials of deploying files to managed nodes using Ansible in a RHEL environment, suitable for the RHCE exam. We discussed setting up Ansible, creating inventory files and playbooks, and executing tasks to deploy files. With these skills, you can automate the deployment and management of files across your RHEL-based infrastructure, increasing efficiency and consistency across your environment.