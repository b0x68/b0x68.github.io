# Tech Tutorial: Understand Core Components of Ansible

## Introduction

Ansible is a powerful automation tool that simplifies the management of multiple servers. It is particularly favored for its minimalistic approach, requiring no agents on the managed nodes and using SSH for communication. This tutorial aims to provide a detailed understanding of how to use Ansible on Red Hat Enterprise Linux (RHEL), focusing on locating and utilizing documentation to uncover information about specific Ansible modules and commands, a key skill for the Red Hat Certified System Administrator (RHCSA) exam.

## Step-by-Step Guide

### Step 1: Setting Up Ansible on RHEL

Before diving into the documentation and specific commands, ensure your RHEL system has Ansible installed. If not, you can install it using the following command:

```bash
sudo yum install ansible
```

This command installs Ansible from the official RHEL repositories. After the installation, you can verify it by checking the version of Ansible:

```bash
ansible --version
```

### Step 2: Accessing Ansible Documentation

Ansible has a vast array of modules and commands, each suited for specific tasks. Knowing how to access and use the Ansible documentation is crucial.

#### Using the `ansible-doc` command

The `ansible-doc` command is a built-in utility to help you find documentation about modules and plugins. For example, if you need information about the `yum` module, you can run:

```bash
ansible-doc yum
```

This command will display detailed documentation about the `yum` module, including its purpose, parameters, and examples.

### Step 3: Searching Documentation for Specific Information

Sometimes, you may need to find specific options or usage patterns within the module documentation.

#### Example: Finding Options for the `user` Module

If you need to modify a user account, use the `user` module. To find out what options are available with this module, you can run:

```bash
ansible-doc user
```

This will display all the options for the `user` module. Look for options like `name` (to specify the username), `state` (to define whether the user should be present or absent), and `password` (to set the user's password).

### Step 4: Practical Example

Let's assume you need to automate the installation of httpd on a server and ensure it is running. Here’s how you can use Ansible modules and find the necessary information using `ansible-doc`.

1. **Find documentation on the `yum` module:**

    ```bash
    ansible-doc yum
    ```

2. **Create a playbook:**

    Create a file named `install_httpd.yml`.

    ```yaml
    ---
    - name: Install and start Apache
      hosts: all
      become: yes
      tasks:
        - name: Install httpd
          yum:
            name: httpd
            state: present

        - name: Ensure httpd is running
          service:
            name: httpd
            state: started
            enabled: yes
    ```

3. **Run the playbook:**

    ```bash
    ansible-playbook install_httpd.yml
    ```

This playbook uses the `yum` module to install httpd and the `service` module to start and enable the httpd service. Before writing the playbook, you can use `ansible-doc service` to explore more about the `service` module.

## Conclusion

Understanding how to navigate and use the Ansible documentation efficiently is crucial for automation tasks and essential for preparing for the RHCSA exam. By mastering `ansible-doc` and practical playbook creation, you can enhance your productivity and ensure your systems are managed consistently and correctly. This skill not only aids in exam preparation but also in real-world system administration tasks on RHEL systems.