# Tech Tutorial: Manage Content with Templates in RHEL

## Introduction

In the context of system administration, particularly for those preparing for the Red Hat Certified System Administrator (RHCSA) exam, understanding how to create and use templates for generating customized configuration files is crucial. This capability simplifies the management of system configurations across multiple machines and improves consistency and efficiency.

This tutorial will guide you through the process of creating templates and using them to generate configuration files in Red Hat Enterprise Linux (RHEL). We'll specifically focus on using `Jinja2` templates in conjunction with `Ansible`, a powerful automation tool that integrates seamlessly with RHEL.

## Prerequisites

- A working RHEL 8 installation.
- `Ansible` installed on your RHEL system.
- Basic understanding of YAML (Yet Another Markup Language) and Jinja2 templating syntax.

## Step-by-Step Guide

### Step 1: Install Ansible on RHEL

First, ensure that Ansible is installed on your RHEL system. If not, you can install it using the following command:

```bash
sudo dnf install ansible -y
```

### Step 2: Create a Simple Jinja2 Template

A Jinja2 template allows you to define placeholders that will be replaced with actual values when the template is processed. Let's create a simple template for an SSH configuration file.

1. Create a directory for your Ansible project:

    ```bash
    mkdir ~/ansible-templates
    cd ~/ansible-templates
    ```

2. Create a template file named `sshd_config.j2`:

    ```jinja
    # SSHD Configuration Template
    Port {{ ssh_port }}
    PermitRootLogin {{ permit_root_login }}
    ```

### Step 3: Define Variables in Ansible

Variables in Ansible can be defined in several places. For simplicity, we’ll define them directly in an inventory file:

1. Create an inventory file:

    ```bash
    echo -e "[servers]\nlocalhost ansible_connection=local" > hosts
    ```

2. Define variables:

    ```yaml
    echo -e "all:\n  vars:\n    ssh_port: 22\n    permit_root_login: no" > group_vars/all.yml
    ```

### Step 4: Write an Ansible Playbook to Use the Template

Create a playbook named `apply_template.yml`:

```yaml
---
- name: Apply SSHD Config Template
  hosts: servers
  tasks:
    - name: Configure SSHD
      template:
        src: sshd_config.j2
        dest: /etc/ssh/sshd_config_test
      become: yes
```

### Step 5: Run the Ansible Playbook

Execute the playbook to apply your template:

```bash
ansible-playbook -i hosts apply_template.yml
```

This command will generate a new SSH configuration file `/etc/ssh/sshd_config_test` on the localhost with the values specified in your `group_vars/all.yml`.

## Detailed Code Examples

In this section, let’s explore more complex templating with conditionals:

`sshd_config.j2`:

```jinja
# Advanced SSHD Configuration Template
Port {{ ssh_port }}
{% if permit_root_login %}
PermitRootLogin yes
{% else %}
PermitRootLogin no
{% endif %}
```

This template uses a Jinja2 conditional to decide whether to allow root login based on the variable `permit_root_login`.

## Conclusion

In this tutorial, you've learned how to leverage Jinja2 templates in Ansible to manage configuration files efficiently on RHEL systems. This method not only simplifies configuration management across multiple systems but also ensures consistency and reduces the potential for human error. As you prepare for the RHCSA exam, practicing these techniques will enhance your proficiency in managing RHEL systems using automation tools like Ansible.