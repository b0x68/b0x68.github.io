# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In this tutorial, we will explore how to utilize roles and Ansible Content Collections, focusing on the Red Hat Certified Engineer (RHCE) exam objectives. Ansible, a powerful IT automation tool, allows for complex deployments to be simplified into readable and manageable playbooks. One of Ansible's strengths lies in its ability to leverage roles and collections to organize and reuse code effectively.

Roles in Ansible are independent components that allow users to break down their playbook into reusable segments, each segment encapsulating its own variables, tasks, files, templates, and modules. Ansible Content Collections, introduced in Ansible 2.9, are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins.

This tutorial will guide you through obtaining a set of related roles and other content from collections, and demonstrate how to use them in a playbook specifically within a Red Hat Enterprise Linux (RHEL) environment.

## Step-by-Step Guide

### Prerequisites

- A Red Hat Enterprise Linux (RHEL) 8 server
- Ansible installed on the RHEL server (`sudo yum install ansible`)
- Access to Ansible Galaxy and internet connectivity

### Step 1: Understanding Ansible Galaxy and Collections

Ansible Galaxy is essentially a repository for sharing Ansible content, including roles and collections. You can use the command-line tool `ansible-galaxy` to search, install, and manage roles and collections.

### Step 2: Installing a Collection

Let's start by installing a popular collection from Ansible Galaxy. For this example, we'll use the `ansible.posix` collection, which includes a variety of POSIX-related roles and modules.

```bash
ansible-galaxy collection install ansible.posix
```

This command downloads and installs the `ansible.posix` collection into the default directory (`~/.ansible/collections`).

### Step 3: Exploring the Collection

After installation, you can explore the contents of the collection:

```bash
ansible-galaxy collection list
```

This will show you all installed collections along with their version.

### Step 4: Using a Role from a Collection in a Playbook

Now, let's create a playbook that uses a role from the `ansible.posix` collection. We will use the `tuned` role, which is responsible for managing the `tuned` daemon and profiles on RHEL.

Create a file named `tune_system.yml`:

```yaml
---
- name: Optimize system performance using tuned
  hosts: all
  become: yes

  tasks:
    - name: Import tuned role from ansible.posix collection
      include_role:
        name: ansible.posix.tuned

      vars:
        tuned_profile: throughput-performance
        tuned_service_state: started
        tuned_service_enabled: yes
```

### Step 5: Running the Playbook

Run the playbook against your RHEL hosts:

```bash
ansible-playbook -i hosts tune_system.yml
```

Replace `hosts` with your own inventory file or list of RHEL servers.

## Detailed Code Examples

Here's a breakdown of the key components in the playbook:

- **include_role:** This task imports the `tuned` role from the `ansible.posix` collection.
- **vars:** We specify variables directly in the task to configure the `tuned` daemon. `tuned_profile` sets the desired profile, and `tuned_service_state` ensures the service is started and enabled on boot.

## Conclusion

In this tutorial, we've covered how to leverage Ansible Content Collections and roles to organize and simplify your automation tasks. By using collections, you can easily reuse code and maintain your Ansible environment efficiently. Remember, the key to mastering Ansible for the RHCE exam and beyond is continual practice and exploration of the available roles and collections.