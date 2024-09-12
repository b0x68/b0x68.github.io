# Tech Tutorial: Create Ansible Plays and Playbooks

## Introduction

Ansible is an incredibly powerful tool for automating IT tasks such as configuration management, application deployment, and task automation. It works by connecting to your nodes and pushing out small programs, called "Ansible modules". These modules are designed to be resource models of the desired state of the system. Ansible then executes these modules and removes them when finished.

In this tutorial, we will focus on how to create Ansible plays and playbooks while working with some of the most commonly used Ansible modules. This tutorial is tailored specifically for the Red Hat Certified System Administrator (RHCSA) exam, and all commands and examples will be relevant to Red Hat Enterprise Linux (RHEL) distributions.

## Step-by-Step Guide

### Setup

Before diving into writing plays and playbooks, ensure that Ansible is installed on your control node (the machine that manages other nodes) which should be a RHEL system. You can install Ansible using the following command:

```bash
sudo yum install ansible
```

### Understanding Ansible Playbooks

An Ansible playbook is essentially a script written in YAML format. It contains one or more plays, each of which targets a set of hosts and tasks that should be applied to them.

### Creating Your First Playbook

Let's create a simple playbook that ensures that the HTTPD service is installed and running on a target RHEL server.

1. **Create the Playbook File**

   Create a new file called `httpd.yml`:

   ```bash
   vim httpd.yml
   ```

2. **Define the Play**

   Write the following content into `httpd.yml`:

   ```yaml
   ---
   - name: Ensure HTTPD is installed and running
     hosts: webservers
     become: yes
     tasks:
     - name: Install HTTPD
       yum:
         name: httpd
         state: present

     - name: Start HTTPD Service
       service:
         name: httpd
         state: started
         enabled: yes
   ```

   Here’s what each part does:
   - `hosts: webservers` tells Ansible to run this play on hosts that belong to the 'webservers' group.
   - `become: yes` escalates privileges (similar to sudo).
   - `tasks:` lists the tasks to be performed on the hosts.
   - `yum:` this module manages packages with the `yum` package manager, ensuring 'httpd' is installed.
   - `service:` this module ensures that the 'httpd' service is started and enabled to start at boot.

3. **Run the Playbook**

   Execute the playbook using:

   ```bash
   ansible-playbook httpd.yml
   ```

### Expanding Your Playbook

Now let's add a task to create a simple index.html for our HTTPD server.

1. **Add a Task to the Playbook**

   Edit `httpd.yml` to add a task that creates a file:

   ```yaml
   - name: Create index.html
     copy:
       content: "Hello, RHCSA!"
       dest: /var/www/html/index.html
   ```

2. **Re-run the Playbook**

   Apply the changes by running:

   ```bash
   ansible-playbook httpd.yml
   ```

### Detailed Code Examples

Here’s how you might ensure SELinux is enforcing on your target hosts using the `selinux` module:

```yaml
---
- name: Ensure SELinux is enforcing
  hosts: all
  become: yes
  tasks:
  - name: Set SELinux to enforcing
    selinux:
      state: enforcing
```

## Conclusion

In this tutorial, we covered the basics of creating Ansible plays and playbooks, focusing on some frequently used modules like `yum`, `service`, and `copy`. As you prepare for the RHCSA exam, practice creating more complex playbooks that incorporate various other modules and span multiple systems. Remember, the key to mastering Ansible is both understanding and practice.