# Tech Tutorial: Run Playbooks with Automation Content Navigator

## Introduction

In this tutorial, we will explore the Automation Content Navigator, particularly focusing on its application within the Red Hat Certified System Administrator (RHCSA) exam environment. The Automation Content Navigator is a pivotal tool in managing and running Ansible playbooks, especially when it comes to creating inventories and configuring the Ansible environment within a Red Hat Enterprise Linux (RHEL) system.

The goal is to provide you with a practical understanding and hands-on experience needed to use the Automation Content Navigator effectively for automation tasks, aligning with the RHCSA exam objectives.

## Prerequisites

- A running Red Hat Enterprise Linux (RHEL) 8 or later system.
- Ansible installed on your RHEL system.
- Basic familiarity with YAML syntax and Ansible fundamentals.

## Step-by-Step Guide

### Step 1: Installing Automation Content Navigator

Before we begin, ensure that your system is updated and has the necessary repositories enabled. Automation Content Navigator can be installed via a package that we need to confirm is available in our enabled repos.

1. **Update your system:**

    ```bash
    sudo dnf update
    ```

2. **Install Automation Content Navigator:**

    ```bash
    sudo dnf install automation-content-navigator
    ```

### Step 2: Creating an Inventory

Ansible uses inventories to manage and group hosts where tasks should be executed. With Automation Content Navigator, you can create and manage these inventories through a user-friendly interface.

1. **Launch Automation Content Navigator:**

    Open the Automation Content Navigator from your applications menu or initiate it from the command line:

    ```bash
    automation-content-navigator
    ```

2. **Create a New Inventory:**

    - In the navigator interface, go to the "Inventories" section.
    - Click on "Create Inventory".
    - Name your inventory and add necessary descriptions.
    - Save the inventory.

### Step 3: Configuring the Ansible Environment

Configuring your Ansible environment correctly is crucial for the successful execution of playbooks.

1. **Set Up Ansible Configuration:**

    Use the Automation Content Navigator to adjust Ansible configurations.

    - Navigate to the "Settings" or "Configuration" tab.
    - Configure necessary parameters such as `ansible_host`, `ansible_user`, and other relevant settings.
    - Save your configurations.

### Step 4: Writing and Running an Ansible Playbook

Now, let's create a simple playbook to test our setup.

1. **Create a Playbook:**

    Create a new file named `test_playbook.yml` in your preferred directory.

    ```yaml
    ---
    - name: Test Playbook
      hosts: all
      tasks:
        - name: Ensure Apache is installed
          yum:
            name: httpd
            state: present
    ```

2. **Run the Playbook:**

    Use the command line to run the playbook against the inventory you created.

    ```bash
    ansible-playbook -i /path/to/your/inventory test_playbook.yml
    ```

## Detailed Code Examples

Below is a detailed example of a more complex playbook that not only installs Apache but also ensures it is enabled and started.

```yaml
---
- name: Comprehensive Apache Setup
  hosts: all
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

    - name: Start and enable Apache
      systemd:
        name: httpd
        enabled: yes
        state: started
```

## Conclusion

In this tutorial, we've covered how to use the Automation Content Navigator to create inventories and configure the Ansible environment on a Red Hat Enterprise Linux system. We also explored how to write and run simple Ansible playbooks. This knowledge is essential for anyone preparing for the RHCSA exam and aims to use Ansible for system automation tasks effectively. The practical experience gained through these exercises will help in understanding and mastering the use of Automation Content Navigator in real-world scenarios.