# Tech Tutorial: Manage Content Using Templates in RHEL

## Introduction

In this tutorial, we will focus on an important topic for the Red Hat Certified Engineer (RHCE) exam—creating and using templates to generate customized configuration files. This capability is crucial for system administrators who need to manage configurations efficiently across multiple systems or environments.

Templates help in standardizing the configuration setup, thus reducing errors and saving time. We will use Jinja2 templates, which are widely used in configuration management tools such as Ansible, which is also part of the Red Hat ecosystem.

## Pre-requisites

Before proceeding, ensure you have the following:
- A Red Hat Enterprise Linux system, version 7 or 8.
- Basic familiarity with Linux command line and text editors (e.g., vim or nano).
- Ansible installed on your machine. You can install Ansible on RHEL by enabling the Red Hat Subscription Management (RHSM) repository and installing the ansible package:
  ```
  sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
  sudo dnf install ansible
  ```

## Step-by-Step Guide

### Step 1: Set Up Your Environment

First, create a directory to work in:

```bash
mkdir ~/template_project
cd ~/template_project
```

### Step 2: Create a Jinja2 Template

Next, we'll create a Jinja2 template for an Apache HTTP server configuration. Open your text editor:

```bash
vim httpd.conf.j2
```

Insert the following content:

```jinja
ServerName {{ server_name }}
Listen {{ server_port }}
DocumentRoot "{{ document_root }}"
<Directory "{{ document_root }}">
    AllowOverride None
    Require all granted
</Directory>
```

This template allows us to customize the `ServerName`, `server_port`, and `document_root` directives.

### Step 3: Create a Playbook to Use the Template

Now, create an Ansible playbook that uses this template to generate a configuration file. Use your text editor again:

```bash
vim playbook.yml
```

Add the following Ansible playbook content:

```yaml
---
- name: Configure HTTPD Server
  hosts: localhost
  vars:
    server_name: "example.com"
    server_port: 80
    document_root: "/var/www/html"

  tasks:
    - name: Generate httpd.conf
      template:
        src: httpd.conf.j2
        dest: /etc/httpd/conf/httpd.conf
```

This playbook sets variables for `server_name`, `server_port`, and `document_root`, then applies those variables to the template to generate `/etc/httpd/conf/httpd.conf`.

### Step 4: Run the Playbook

Execute the playbook with the following command:

```bash
ansible-playbook playbook.yml
```

Ansible will connect to the localhost, apply the template with the specified variables, and write the output to `/etc/httpd/conf/httpd.conf`.

### Step 5: Verify the Configuration

Check that the configuration file was created correctly:

```bash
cat /etc/httpd/conf/httpd.conf
```

You should see the filled-out configuration file with the values you specified in the playbook.

## Conclusion

In this tutorial, we've covered how to use Jinja2 templates with Ansible to automate the creation of customized configuration files on RHEL systems. This approach not only ensures consistency across multiple setups but also significantly reduces the potential for human error in file configuration.

Utilizing templates is a scalable way to manage configurations and should be a part of every Red Hat Certified Engineer's toolkit. Remember, the power of templates lies in their reusability and flexibility, making them ideal for managing complex environments efficiently.