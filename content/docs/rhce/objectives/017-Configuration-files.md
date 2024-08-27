# Tech Tutorial: Understand Core Components of Ansible - Configuration Files

## Introduction

In the world of automated configuration management, deployment, and orchestration, Ansible stands out for its simplicity and ease of use. At the core of Ansible's architecture are its configuration files, which are pivotal in defining how Ansible connects to nodes, the behavior of Ansible tasks, and setting default values for variables and other parameters.

This tutorial aims to give you a comprehensive understanding of Ansible configuration files, specifically focusing on the primary configuration file `ansible.cfg`. We'll cover how to customize this file to tailor Ansible to your environment and needs.

## Step-by-Step Guide

### 1. Understanding the `ansible.cfg` File

Ansible typically looks for configuration file data in the following order:

1. `ANSIBLE_CONFIG` (an environment variable pointing to a configuration file)
2. `ansible.cfg` in the current directory
3. `.ansible.cfg` in the home directory
4. `/etc/ansible/ansible.cfg`

The first file found is used. Let's explore how to locate and understand the default settings in `ansible.cfg`.

### 2. Locating the Default Configuration File

The default configuration file usually resides in `/etc/ansible/ansible.cfg`. You can view this file to understand the default settings.

```bash
cat /etc/ansible/ansible.cfg
```

### 3. Key Parameters in the Configuration File

Here are some important parameters you'll often need to configure:

- **`inventory`**: Specifies the location of the inventory file that Ansible uses.
- **`remote_user`**: Default ssh user name to use.
- **`ask_pass`**: Whether to prompt for a password by default.
- **`private_key_file`**: File to use for ssh key-based authentication.
- **`host_key_checking`**: Enables/disables checking SSH host keys.
- **`retry_files_enabled`**: Enables/disables the creation of retry files.
- **`roles_path`**: Specifies the location of roles.
- **`log_path`**: Defines the path for log files.

### 4. Customizing the `ansible.cfg` File

#### Example: Setting a Custom Inventory and Disabling Host Key Checking

Suppose you have your inventory file not at the default location but at `/custom/path/inventory`. Here's how you could configure this along with disabling host key checking:

```ini
[defaults]
inventory = /custom/path/inventory
host_key_checking = False
```

#### Example: Setting Multiple Roles Paths

If you have roles spread across different directories, you can configure them like this:

```ini
[defaults]
roles_path = /etc/ansible/roles:/usr/share/ansible/roles:/custom/roles
```

### 5. Using Environment Variables

For a temporary change or for specific runtime environments, you can use environment variables. For example, to change the inventory file temporarily, you can use:

```bash
export ANSIBLE_INVENTORY=/path/to/new/inventory
```

## Detailed Code Examples

### Example Configuration for a Production Environment

Here’s a more detailed example of an `ansible.cfg` for a production environment:

```ini
[defaults]
inventory = /etc/ansible/prod_inventory
remote_user = admin
private_key_file = /home/admin/.ssh/id_rsa
host_key_checking = False
retry_files_enabled = False
log_path = /var/log/ansible.log

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False
```

This configuration sets up Ansible for a production environment with specific user and logging settings, disables retry files, and configures privilege escalation settings.

## Conclusion

Mastering the `ansible.cfg` file is essential for effectively managing and customizing Ansible's behavior in your environment. By understanding and tweaking the configuration options, you can ensure that Ansible runs efficiently and securely according to your operational standards. Always remember to test changes in a development environment before applying them in production to avoid any disruptions.

Happy automating with Ansible!