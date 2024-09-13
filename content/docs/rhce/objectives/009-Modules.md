# Tech Tutorial: Understand Core Components of Ansible - Modules

## Introduction

In this tutorial, we are going to dive deep into one of the fundamental components of Ansible - **Modules**. Ansible is a powerful automation tool that simplifies complex configuration tasks and orchestration. At the heart of Ansible's power and flexibility are its modules, which are the building blocks that power the automation of a wide array of tasks on Red Hat Enterprise Linux (RHEL) systems. We will explore what modules are, how they work, and provide detailed examples of using some of the most common Ansible modules.

## What are Ansible Modules?

Modules in Ansible are essentially discrete units of code that can be used to automate specific tasks on managed nodes. Each module is designed to handle specific tasks and can be invoked from Ansible playbooks or directly from the command line using the `ansible` command.

Ansible comes with a wide range of modules that can manage system resources like packages, services, files, and much more. Moreover, Ansible’s modular nature allows you to write your custom modules.

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

Before you can start using Ansible modules, you need to have Ansible installed on your control node (the system from which you will manage your other systems). Here, we'll focus on a RHEL environment.

1. **Install Ansible on RHEL:**
   - First, enable the EPEL repository:
     ```bash
     sudo subscription-manager repos --enable rhel-7-server-optional-rpms
     sudo subscription-manager repos --enable rhel-7-server-extras-rpms
     ```
   - Install Ansible using `yum`:
     ```bash
     sudo yum install ansible -y
     ```

2. **Configure Hosts File:**
   - Edit `/etc/ansible/hosts` and add the managed nodes details. For example:
     ```ini
     [servers]
     192.168.1.50 ansible_user=your-user ansible_ssh_private_key_file=/path/to/key
     ```

### Step 2: Using Ansible Modules

Now that we have Ansible installed, let's explore how to use some fundamental modules.

#### Example 1: Using the `yum` Module

The `yum` module is used for managing packages on RHEL-based systems. Here's how you can ensure that the `httpd` package is installed.

- **Create a playbook `install_httpd.yml`:**
  ```yaml
  ---
  - name: Install Apache HTTP Server
    hosts: servers
    become: yes

    tasks:
      - name: Ensure Apache is installed
        yum:
          name: httpd
          state: present
  ```

- **Run the playbook:**
  ```bash
  ansible-playbook install_httpd.yml
  ```

#### Example 2: Using the `service` Module

After installing a service like Apache, you might want to ensure that it is enabled and running:

- **Modify the `install_httpd.yml` playbook:**
  ```yaml
  ---
  - name: Install and start Apache HTTP Server
    hosts: servers
    become: yes

    tasks:
      - name: Ensure Apache is installed
        yum:
          name: httpd
          state: present

      - name: Ensure Apache is enabled and running
        service:
          name: httpd
          state: started
          enabled: yes
  ```

- **Run the playbook again:**
  ```bash
  ansible-playbook install_httpd.yml
  ```

## Detailed Code Examples

### Using the `copy` Module

Let's create a playbook to copy a local file to a remote server:

- **Create a playbook `copy_file.yml`:**
  ```yaml
  ---
  - name: Copy a file to remote servers
    hosts: servers
    become: yes

    tasks:
      - name: Copy file to /tmp
        copy:
          src: /path/to/local/file
          dest: /tmp/remote_file
  ```

- **Run the playbook:**
  ```bash
  ansible-playbook copy_file.yml
  ```

## Conclusion

In this tutorial, we explored Ansible modules, which are crucial for automating tasks in a RHEL environment. By understanding and utilizing these modules effectively, you can automate almost any aspect of your system configuration and management. The examples provided should help you get started with using some of the most common modules in Ansible. As you progress, you can explore more modules that cater to specific needs of your infrastructure. Remember, the power of Ansible lies in its simplicity and flexibility, making it an indispensable tool in the toolbox of any system administrator or DevOps professional.

Happy automating!