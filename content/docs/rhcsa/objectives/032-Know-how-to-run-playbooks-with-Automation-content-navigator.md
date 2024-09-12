# Tech Tutorial: Run Playbooks with Automation Content Navigator

## Introduction

In this tutorial, we will explore how to run Ansible Playbooks using the Automation Content Navigator, a tool that is highly relevant for Red Hat Certified System Administrator (RHCSA) exam candidates. This tutorial is tailored specifically for Red Hat Enterprise Linux (RHEL) systems. Ansible is a powerful automation tool used to automate various tasks on multiple systems. With the Automation Content Navigator, managing and executing Ansible Playbooks becomes more streamlined, enabling efficient automation workflows.

## Prerequisites

Before proceeding, ensure you have the following:
- A RHEL 8+ system installed and running.
- Ansible installed on your system.
- Sudo or root privileges on the system.

You can install Ansible on RHEL by using the following commands:

```bash
sudo dnf install ansible
```

## Step-by-Step Guide

### Step 1: Setting Up Your Environment

First, ensure your system is prepared with the necessary directories and user permissions. 

```bash
# Create a directory for your ansible projects
mkdir ~/ansible-projects
cd ~/ansible-projects

# Create a sample playbook
cat << EOF > sample-playbook.yml
---
- name: Test Ansible Playbook
  hosts: localhost
  tasks:
    - name: Echo a message
      command: echo "Hello from Automation Content Navigator!"
EOF
```

### Step 2: Understanding Automation Content Navigator

Automation Content Navigator is part of the larger Red Hat Ansible Automation Platform. It's designed to help users organize, manage, and run Ansible content across various environments. 

For the purpose of this tutorial, we will focus on running playbooks. However, in a real-world scenario, you would interact with Automation Content Navigator through its web interface, where you can manage not just playbooks but also roles, collections, and other resources.

### Step 3: Running Your Playbook

While the full capabilities of Automation Content Navigator include a web-based interface, for this example, we will execute the playbook directly from the command line, which is essential for understanding the foundations of playbook execution in a controlled environment.

Execute the Ansible playbook by running:

```bash
ansible-playbook sample-playbook.yml
```

You should see output similar to this:

```plaintext
PLAY [Test Ansible Playbook] *********************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [localhost]

TASK [Echo a message] ****************************************************************************
changed: [localhost]

PLAY RECAP ***************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

This output indicates that the playbook has successfully run, executing all tasks defined in it.

## Detailed Code Examples

Let's expand our playbook to include more complex examples, showcasing real-world utility:

```yaml
---
- name: Comprehensive Ansible Playbook
  hosts: localhost
  become: yes
  tasks:
    - name: Install httpd
      yum:
        name: httpd
        state: present

    - name: Start and enable httpd
      service:
        name: httpd
        state: started
        enabled: yes

    - name: Deploy a custom index page
      copy:
        content: "Welcome to our server, powered by Automation Content Navigator!"
        dest: /var/www/html/index.html
```

Run this playbook using the same command as before:

```bash
ansible-playbook comprehensive-playbook.yml
```

## Conclusion

In this tutorial, we've covered the basics of running Ansible playbooks on a Red Hat Enterprise Linux (RHEL) system, specifically tailored for the RHCSA exam. We explored how to set up your environment, create basic and more complex playbooks, and execute them successfully.

The Automation Content Navigator enhances these capabilities by providing a user-friendly interface to manage and execute your automation strategies effectively. As you prepare for your RHCSA exam, practicing these skills will not only help you in the exam but also in real-world system administration tasks.