# Tech Tutorial: Use Roles and Ansible Content Collections

## Introduction

In the domain of automation and configuration management, Ansible is a pivotal tool used extensively to deploy and manage applications in an efficient and scalable manner. In this tutorial, we will explore how to enhance your Ansible capabilities by leveraging **Ansible Content Collections** and **Roles**. These features allow for more modular, reusable, and maintainable code structures within your automation strategies. This is especially relevant for those preparing for the Red Hat Certified Engineer (RHCE) exam, where proficiency in these areas is essential.

## Step-by-Step Guide

### Prerequisites

Before we dive into the practical steps, ensure that your system is set up with:

- A RHEL 8 system
- Ansible installed (Ansible Core 2.9 or later is recommended for full support of Collections)

To install Ansible on RHEL 8, you can use the following command:

```bash
sudo dnf install ansible
```

### 1. Understanding Ansible Content Collections

Ansible Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. They are designed to help you organize and scale your Ansible content more effectively.

### 2. Installing Ansible Collections

To install an Ansible Collection from Ansible Galaxy, use the `ansible-galaxy` command. For instance, to install the `community.general` collection, you would use:

```bash
ansible-galaxy collection install community.general
```

To install a specific version or source it from a private Galaxy server, you can specify it in the command:

```bash
ansible-galaxy collection install community.general:1.3.0 --server http://myprivategalaxy.example.com
```

### 3. Using Collections in a Playbook

Once a collection is installed, you can use the modules, roles, and other content it includes in your playbooks. For example, here’s how you can use the `ping` module from the `community.general` collection:

```yaml
---
- name: Test connection
  hosts: all
  gather_facts: no

  tasks:
    - name: Ping test
      community.general.ping:
```

### 4. Understanding and Using Ansible Roles

Roles in Ansible allow you to automate the creation of reusable components. They can be used to encapsulate and organize your automation content.

#### Creating a Role

To create a role, use the `ansible-galaxy` command:

```bash
ansible-galaxy init role_name
```

This creates a role directory structure under a directory named `role_name`.

#### Example Role Structure

```
role_name/
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml
```

#### Using a Role in a Playbook

Here’s an example of how to use a created role in a playbook:

```yaml
---
- name: Apply the role
  hosts: all
  roles:
    - role_name
```

### 5. Putting It All Together

Now, let’s combine what we’ve learned about Collections and Roles in a practical example:

```yaml
---
- name: Web server setup
  hosts: web_servers
  gather_facts: yes

  collections:
    - community.general

  roles:
    - role_name

  tasks:
    - name: Ensure Apache is at the latest version
      community.general.yum:
        name: httpd
        state: latest
```

## Conclusion

Using Ansible Roles and Content Collections can significantly streamline and enhance your automation workflows. By modularizing your tasks and utilizing community-driven resources, you can achieve more maintainable and scalable infrastructure automation. This knowledge not only aids in real-world scenarios but is also essential for those preparing for the RHCE exam. Implement these strategies to develop more robust and effective automation solutions.