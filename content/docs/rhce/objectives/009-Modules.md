# Understand Core Components of Ansible: Modules

In this tutorial, we will delve deep into one of the fundamental building blocks of Ansible: **Modules**. Modules in Ansible are essentially small programs that do the actual work in an Ansible playbook. Each module is tailored to support particular tasks, making it easier for IT professionals and developers to automate a wide range of operations in their IT environments.

## Introduction

Ansible is a popular open-source automation tool that simplifies cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs. At the heart of Ansible's power and simplicity are its modules, which can be used directly in playbooks or ad-hoc commands.

### What are Modules?

Modules are the units of work that Ansible ships to remote machines. Ansible executes each module, usually on a remote managed node, and collects return values. A module can be implemented in any language, including Perl, Bash, or Ruby, but the most common ones are written in Python.

## Step-by-Step Guide

In this guide, we will cover how to use some core modules, how to customize them, and how to create your own modules.

### 1. Using Core Modules

Ansible comes with a wide array of built-in modules that can be directly utilized to perform numerous tasks. Here's how to use some of the essential core modules:

#### Example: Managing Files with the `file` Module

The `file` module manages the file and its properties. Here's how you can ensure a directory is present and set its permissions.

```yaml
- name: Ensure a directory is present
  ansible.builtin.file:
    path: /path/to/directory
    state: directory
    mode: '0755'
```

#### Example: Installing Packages with the `yum` Module

The `yum` module manages packages with the Yum package manager, typical in CentOS and RHEL distributions.

```yaml
- name: Install the latest version of Apache
  ansible.builtin.yum:
    name: httpd
    state: latest
```

### 2. Customizing Modules

You can also customize existing modules according to your needs. Parameters play an essential role here. For instance, to create a custom user with the `user` module:

```yaml
- name: Add a new user
  ansible.builtin.user:
    name: john
    comment: "John Doe"
    uid: 1040
    group: admin
```

### 3. Writing Your Own Modules

If the existing modules don't meet your requirements, you can write your own. Here’s a simple custom module written in Python that checks if a file exists on the remote node.

#### `check_file.py`

```python
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        path=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']

    try:
        with open(path) as file:
            result['message'] = 'File exists.'
    except IOError:
        result['message'] = 'File does not exist.'
        module.fail_json(msg='File does not exist.', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
```

To use this module in a playbook:

```yaml
- name: Check if a file exists
  check_file:
    path: "/path/to/file"
```

## Conclusion

Ansible modules are powerful and flexible, allowing for efficient automation of tasks across a diverse range of systems. By understanding how to use, customize, and even create modules, you can leverage Ansible's full potential to automate your infrastructure effectively. Whether using built-in modules or writing your own, Ansible provides the tools necessary to streamline your operational tasks.

This deep dive into Ansible modules should equip you with the knowledge to start leveraging Ansible more effectively in your projects and prepare you for related exam topics. Happy automating!