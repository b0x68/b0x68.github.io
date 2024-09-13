# Tech Tutorial: Install and Configure an Ansible Control Node

Ansible is a powerful automation tool that simplifies complex configuration management, application deployment, and task automation. It is particularly popular in the system administration, DevOps, and IT automation fields. This tutorial focuses on setting up an Ansible control node on a Red Hat Enterprise Linux (RHEL) system and creating a static host inventory file, which is an essential skill for the Red Hat Certified Engineer (RHCE) exam.

## Introduction

Before diving into the installation and configuration process, it's important to understand the role of the Ansible control node. The control node is a machine where Ansible is installed and from which all tasks and playbooks are run. It manages the inventory of your hosts, which can be defined in simple text files or dynamically sourced from other systems.

In this tutorial, we will cover:
1. Installing Ansible on a Red Hat Enterprise Linux system.
2. Configuring Ansible to manage a group of servers.
3. Creating and understanding a static host inventory file.

## Prerequisites

- A Red Hat Enterprise Linux 8 system.
- Sudo or root access on the machine.
- Basic familiarity with Linux command line and text editors.

## Step-by-Step Guide

### Step 1: Installing Ansible

First, ensure that your system is registered with Red Hat Subscription Management and that the repositories are enabled. Install Ansible using the following commands:

```bash
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
sudo dnf install ansible
```

This will install Ansible and its dependencies on your RHEL system.

### Step 2: Verify Ansible Installation

To verify that Ansible has been installed correctly, you can run:

```bash
ansible --version
```

This command will display the Ansible version along with some configuration details.

### Step 3: Setting Up the Inventory File

Ansible uses an inventory file to track all the machines it can communicate with. Here, we'll create a static inventory file. 

1. Create a directory for your Ansible project:

    ```bash
    mkdir ~/ansible_project
    cd ~/ansible_project
    ```

2. Create an inventory file named `hosts`:

    ```bash
    touch hosts
    ```

3. Open the `hosts` file with your preferred text editor, for example, `vi`:

    ```bash
    vi hosts
    ```

4. Add the following content to the `hosts` file:

    ```
    [web]
    webserver1.example.com

    [db]
    dbserver1.example.com

    [all:vars]
    ansible_user=my_ansible_user
    ansible_ssh_private_key_file=/path/to/private/key
    ```

    - `[web]` and `[db]` are group names that contain the hostnames or IP addresses of your web and database servers, respectively.
    - `ansible_user` is the common user for all hosts that Ansible will use for SSH connections.
    - `ansible_ssh_private_key_file` is the path to the SSH private key that Ansible will use for SSH connections.

### Step 4: Testing Connectivity

Test if Ansible can connect to the servers listed in your inventory file by using the `ansible` command:

```bash
ansible all -m ping -i hosts
```

This command uses the `ping` module to test SSH connectivity to all hosts in the inventory.

## Detailed Code Examples

Here’s a detailed breakdown of the inventory file:

- Groups are defined using square brackets `[]`. Any host under `[web]` will be part of the web group.
- You can specify variables for groups or individual hosts. In the `all:vars` section, variables defined are applicable to all hosts.

## Conclusion

In this tutorial, you have learned how to set up an Ansible control node on a RHEL system, configure it, and create a static host inventory file. This setup is fundamental for automating tasks across multiple servers efficiently. With the inventory file, you can group hosts and specify variables that can be used in your playbooks and commands. This knowledge forms a solid foundation for more advanced Ansible topics and prepares you for the RHCE exam.

Remember, practice is key to mastering Ansible, so continue experimenting with different configurations and scenarios to strengthen your skills.