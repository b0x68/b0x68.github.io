# Tech Tutorial: Understand Core Components of Ansible - Focusing on Plays

## Introduction

Ansible is a powerful tool for configuration management, application deployment, and task automation. It enables system administrators and DevOps professionals to automate routine tasks efficiently. This tutorial focuses on one of the core components of Ansible known as "Plays." We will explore the concept of plays within the context of Ansible Playbooks, specifically tailored for Red Hat Enterprise Linux (RHEL) environments, adhering to the guidelines and requirements for the Red Hat Certified Systems Administrator (RHCSA) exam.

## What is a Play in Ansible?

In Ansible, a **play** is a set of tasks executed on a group of hosts. A play is defined inside a playbook, which is a YAML file containing one or more plays. Each play must specify the host or group of hosts and the tasks to be executed on those hosts.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

Before diving into the creation of Ansible plays, ensure your Ansible environment is set up correctly on your RHEL system.

1. **Install Ansible on RHEL:**

   Install the EPEL repository, then install Ansible using `yum`:
   ```bash
   sudo yum install epel-release -y
   sudo yum install ansible -y
   ```

2. **Verify Ansible Installation:**
   ```bash
   ansible --version
   ```

3. **Set Up Inventory File:**

   Create an inventory file `/etc/ansible/hosts` and add your managed nodes:
   ```ini
   [webservers]
   server1.example.com
   server2.example.com
   ```

### Step 2: Creating Your First Play

Let’s create a simple playbook called `example_playbook.yml` that includes a single play.

1. **Create the Playbook File:**
   
   Use your favorite text editor to create a file named `example_playbook.yml`:
   ```bash
   vim example_playbook.yml
   ```

2. **Define the Play:**

   Insert the following content into your playbook file:
   ```yaml
   ---
   - name: Ensure Apache is installed and running
     hosts: webservers
     become: yes
     tasks:
       - name: Install httpd
         yum:
           name: httpd
           state: present

       - name: Start httpd service
         service:
           name: httpd
           state: started
           enabled: yes
   ```

   Explanation:
   - **hosts:** Specifies the group of hosts (webservers) defined in your inventory.
   - **become:** Escalate privileges (similar to sudo).
   - **tasks:** List of tasks to execute; installing and starting Apache (`httpd`).

### Step 3: Running the Playbook

Execute the playbook using the `ansible-playbook` command:
```bash
ansible-playbook example_playbook.yml
```

### Step 4: Verifying the Play

Check the status of the Apache (`httpd`) service on the managed nodes to ensure it's installed and running:
```bash
ansible webservers -m service -a "name=httpd state=started" --become
```

## Detailed Code Examples

In this section, we will look at a more complex example involving multiple tasks within a play.

### Advanced Playbook Example

Create a file named `advanced_playbook.yml`:
```yaml
---
- name: Configure web and database servers
  hosts: all
  become: yes
  tasks:
    - name: Install and start Apache on webservers
      yum:
        name: httpd
        state: present
      when: "'webservers' in group_names"

    - name: Install and start MariaDB on db servers
      yum:
        name: mariadb-server
        state: present
      when: "'dbservers' in group_names"

    - name: Ensure httpd is enabled and running
      service:
        name: httpd
        state: started
        enabled: yes
      when: "'webservers' in group_names"

    - name: Ensure MariaDB is enabled and running
      service:
        name: mariadb
        state: started
        enabled: yes
      when: "'dbservers' in group_names"
```

## Conclusion

Understanding and utilizing plays in Ansible is fundamental for automating tasks across multiple systems efficiently. This tutorial provided a foundational guide to creating and running plays in a RHEL environment, suitable for preparation towards the RHCSA exam. As you progress, experiment with more complex plays and integrate Ansible into your system administration practices to achieve greater automation and consistency.