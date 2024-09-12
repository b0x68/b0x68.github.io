# Tech Tutorial: Configure Ansible Managed Nodes

## Introduction

In this tutorial, we will focus on deploying files to managed nodes using Ansible, a powerful IT automation tool that simplifies cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs.

Deploying files to managed nodes is a common task in the administration of systems, particularly in environments where consistency and automation of system setup are crucial. For the Red Hat Certified System Administrator (RHCSA) exam, understanding how to use Ansible for these tasks on Red Hat Enterprise Linux (RHEL) systems is essential.

## Prerequisites

Before we begin, ensure that you have the following set up:

- **Ansible Control Node**: A RHEL system where Ansible is installed and will run from.
- **Managed Nodes**: One or more RHEL systems that Ansible will manage. SSH access should be configured and working between the control node and these managed systems.
- **Proper permissions**: You need to have sudo or root access to the systems to install packages and modify configuration files.

## Step-by-Step Guide

### Step 1: Installing Ansible

First, install Ansible on your control node. Since we are using a RHEL system, we will use `yum` to install Ansible.

```bash
sudo yum install ansible -y
```

### Step 2: Configuring Ansible

Create or edit the `/etc/ansible/hosts` file to add your managed nodes. This file is known as the Inventory file and tells Ansible about the nodes it can interact with.

```ini
[managed_nodes]
192.168.1.101
192.168.1.102
```

### Step 3: Testing Connectivity

Before deploying files, it's a good practice to check if Ansible can communicate with your managed nodes:

```bash
ansible managed_nodes -m ping
```

You should receive a "pong" response from each managed node.

### Step 4: Deploying a File

To deploy files, we will use the `copy` module of Ansible. Create a simple text file on your control node named `testfile.txt`.

```bash
echo "This is a test file" > testfile.txt
```

Now, create an Ansible playbook called `deploy_file.yml`:

```yaml
---
- name: Deploy file to managed nodes
  hosts: managed_nodes
  tasks:
    - name: Copy file to managed nodes
      copy:
        src: /path/to/testfile.txt
        dest: /home/user/testfile.txt
        owner: user
        group: user
        mode: '0644'
```

### Step 5: Running the Playbook

Execute the playbook using the `ansible-playbook` command:

```bash
ansible-playbook deploy_file.yml
```

### Detailed Code Examples

The `copy` module is very flexible. Here are more examples of how you can use it:

#### Copying a directory:

```yaml
- name: Copy directory to managed nodes
  copy:
    src: /path/to/directory/
    dest: /home/user/directory/
    directory_mode: '0755'
```

#### Ensuring a file is absent:

```yaml
- name: Ensure file is absent
  file:
    path: /home/user/oldfile.txt
    state: absent
```

## Conclusion

In this tutorial, you've learned how to configure Ansible on a Red Hat Enterprise Linux system, and how to use it to deploy files to managed nodes. This skill is not only crucial for the RHCSA exam but also extremely useful in real-world system administration. Automation via Ansible can significantly improve the efficiency, consistency, and reliability of system configurations across multiple nodes.

Remember, practice is key to mastering Ansible. Consider setting up a test environment to try different configurations and explore more of what Ansible can offer.