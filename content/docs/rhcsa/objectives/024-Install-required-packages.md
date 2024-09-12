# Tech Tutorial: Install and Configure an Ansible Control Node on RHEL

## Introduction

Ansible is an open-source automation tool, or platform, used for IT tasks such as configuration management, application deployment, intraservice orchestration, and provisioning. Automation is crucial for consistent deployment and management of systems and applications, especially in large-scale environments. For those preparing for the Red Hat Certified System Administrator (RHCSA) exam, understanding how to set up Ansible on a Red Hat Enterprise Linux (RHEL) system is essential.

This tutorial will guide you through the process of installing and configuring an Ansible control node on a RHEL system. We'll cover the steps required to install the necessary packages and configure the system to manage other hosts through Ansible.

## Prerequisites

- A RHEL 8 system with root or sudo privileges
- Internet access for downloading packages

## Step-by-Step Guide

### Step 1: Subscription and Repository Configuration

Before installing any package on RHEL, ensure that your system is registered with Red Hat Subscription Management and that the required repositories are enabled.

1. **Register your system** (if not already done):
    ```bash
    sudo subscription-manager register --username YOUR-USERNAME --password YOUR-PASSWORD
    ```
    Replace `YOUR-USERNAME` and `YOUR-PASSWORD` with your Red Hat Customer Portal credentials.

2. **Attach the subscription**:
    ```bash
    sudo subscription-manager attach --auto
    ```

3. **Enable the Ansible repository**:
    ```bash
    sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
    ```

### Step 2: Installing Ansible

With the repository enabled, you can now install Ansible using the `dnf` package manager.

```bash
sudo dnf install ansible -y
```

### Step 3: Verify the Installation

After installation, verify that Ansible is correctly installed by checking the version.

```bash
ansible --version
```

This command should output the version of Ansible installed, along with some configuration file paths.

### Step 4: Configuring Ansible

Ansible uses a configuration file named `ansible.cfg` and an inventory file to manage and locate the hosts it will manage. Here’s how to set them up:

1. **Create a directory for your Ansible configuration** (optional but recommended for organization):
    ```bash
    mkdir ~/ansible-config && cd ~/ansible-config
    ```

2. **Create a new `ansible.cfg` file**:
    ```bash
    nano ansible.cfg
    ```
    Add the following contents:
    ```ini
    [defaults]
    inventory = ./hosts
    host_key_checking = False
    retry_files_enabled = False
    ```

3. **Create an inventory file**:
    ```bash
    nano hosts
    ```
    Add your managed hosts under a group, for example:
    ```ini
    [webservers]
    server1 ansible_host=192.168.1.101
    server2 ansible_host=192.168.1.102
    ```

4. **Test your configuration**:
    ```bash
    ansible all -m ping
    ```
    This command uses the `ping` module to check the connection to all hosts listed in your inventory.

## Conclusion

You have successfully installed and configured an Ansible control node on your RHEL system. This setup is crucial for automating tasks and managing configurations across multiple systems efficiently. By mastering these steps, you are well on your way to becoming proficient in Ansible and preparing effectively for the RHCSA exam.

Continue to explore more about Ansible modules and playbooks to automate complex IT tasks further. Happy automating!