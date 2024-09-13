# Tech Tutorial: Run Playbooks with Automation Content Navigator

In this tutorial, we will dive into how to use Automation Content Navigator to manage and run Ansible Playbooks effectively. By the end of this guide, you'll understand how to create inventories and configure the Ansible environment using Automation Content Navigator, specifically tailored for Red Hat Certified Engineer (RHCE) exam candidates.

## Introduction

Automation Content Navigator is a powerful tool within the Red Hat Ansible Automation Platform that allows users to manage their automation content efficiently. It provides a user-friendly interface to handle various tasks such as creating inventories, configuring environments, and running Ansible playbooks.

The primary focus of this tutorial is to guide you through the process of setting up your Ansible environment and managing inventories using Automation Content Navigator on a Red Hat Enterprise Linux system.

## Step-by-Step Guide

### Prerequisites

- A Red Hat Enterprise Linux (RHEL) system
- Ansible installed on your RHEL system (Ensure it is installed using the official RHEL repositories)
- Access to Automation Content Navigator through your Red Hat Ansible Automation Platform subscription

### Step 1: Accessing Automation Content Navigator

1. Open your web browser.
2. Navigate to the URL of your Automation Content Navigator. This URL is typically provided during the setup of your Ansible Automation Platform.

### Step 2: Configuring the Ansible Environment

Before running any playbooks, it's crucial to configure your Ansible environment properly.

1. **Create a Project:**
   - In Automation Content Navigator, go to the **Projects** tab.
   - Click on **Add Project**.
   - Provide a name and description for your project.
   - Specify the SCM (Source Code Management) type and SCM URL if your playbooks are stored in a version control system.
   - Save the project.

2. **Configure Credentials:**
   - Navigate to the **Credentials** tab.
   - Click on **Add Credential**.
   - Choose the credential type (e.g., Machine, SCM).
   - Fill in the necessary authentication details required to access your resources.
   - Save the credential.

### Step 3: Creating Inventories

Inventories are crucial in Ansible as they define the hosts and groups on which the playbooks will run.

1. Go to the **Inventories** tab in Automation Content Navigator.
2. Click on **Add Inventory**.
3. Provide a name and description for your inventory.
4. Save the inventory.
5. Add hosts or groups to your inventory:
   - Select your inventory and click on **Hosts** or **Groups**.
   - Use the **Add Host** or **Add Group** button to include your targets.
   - Specify the host details such as IP address and relevant variables.

### Step 4: Running Ansible Playbooks

1. **Create a Job Template:**
   - Navigate to the **Templates** tab.
   - Click on **Add Template**.
   - Select **Job Template**.
   - Provide a name and description for the template.
   - Choose the previously created project, inventory, and playbook.
   - Select the appropriate credentials.
   - Save the template.

2. **Launch the Job:**
   - Find the job template you created.
   - Click on the rocket icon to launch the job.
   - Monitor the job execution in the **Jobs** tab.

## Detailed Code Examples

Here’s a simple Ansible playbook example stored in your SCM that you can use to test running a playbook via Automation Content Navigator. This playbook installs nginx on all web servers defined in your inventory.

```yaml
---
- name: Install nginx
  hosts: webservers
  become: yes

  tasks:
  - name: Install nginx
    yum:
      name: nginx
      state: present
```

Ensure that your SCM repository URL is linked correctly in the project settings within Automation Content Navigator.

## Conclusion

You have successfully learned how to create inventories, configure the Ansible environment, and run playbooks using Automation Content Navigator. These skills are essential for managing automation tasks efficiently and are crucial for the Red Hat Certified Engineer exam.

Remember, practice is key to mastering these concepts. Try setting up different environments and running various playbooks to solidify your understanding. Happy automating!