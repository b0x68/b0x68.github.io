# Tech Tutorial: Manage Content Using Ansible Vault in Playbooks

## Introduction

In the world of automation and DevOps, managing sensitive data securely is crucial. Ansible, a popular automation tool, provides a feature called Ansible Vault that helps in securing sensitive data such as passwords, keys, and other secrets. This tutorial will guide you through the process of using Ansible Vault in your playbooks to protect sensitive data.

## What is Ansible Vault?

Ansible Vault is a feature of Ansible that allows you to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in your playbooks or roles. This is crucial for keeping your sensitive data secure both at rest and in transit.

## Prerequisites

Before you start, you need to have the following installed:

- Ansible (2.4 or later)
- A text editor of your choice
- Access to a command-line terminal

## Step-by-Step Guide

### Step 1: Installing Ansible

If you haven't already installed Ansible, you can install it by running:

```bash
$ sudo apt update
$ sudo apt install ansible
```

### Step 2: Creating an Encrypted Ansible Vault File

1. **Create a new encrypted file:**

   To create a new encrypted file using Ansible Vault, use the following command:

   ```bash
   $ ansible-vault create secrets.yml
   ```

   This command will prompt you to enter a password. After confirming the password, a file named `secrets.yml` will be opened in your default editor in encrypted form.

2. **Adding content to the encrypted file:**

   You can add some sensitive data to the `secrets.yml` file. For example:

   ```yaml
   secret_key: mysupersecretpassword
   ```

   Save and close the file.

### Step 3: Editing an Encrypted File

If you need to modify the `secrets.yml` file later, you can use the following command:

```bash
$ ansible-vault edit secrets.yml
```

This will again ask for the password, and upon successful authentication, open the file for editing.

### Step 4: Viewing Encrypted Files

To view the contents of an encrypted file without editing:

```bash
$ ansible-vault view secrets.yml
```

### Step 5: Using Encrypted Files in Playbooks

Now, let’s use the encrypted `secrets.yml` in an Ansible playbook:

1. **Create a playbook:**

   Create a file named `playbook.yml`:

   ```yaml
   ---
   - hosts: all
     vars_files:
       - secrets.yml
     tasks:
       - name: Print secret
         debug:
           msg: "The secret key is {{ secret_key }}"
   ```

2. **Running the playbook:**

   To run this playbook while decrypting the `secrets.yml` file, use the command:

   ```bash
   $ ansible-playbook playbook.yml --ask-vault-pass
   ```

   This command will prompt you for the password of the `secrets.yml` file. Once provided, it will execute the playbook and print the secret key.

## Detailed Code Examples

Here is a more complex example involving multiple variables and tasks:

```yaml
---
- hosts: all
  vars_files:
    - secrets.yml
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
      become: yes
    - name: Update index.html with secret data
      lineinfile:
        path: /var/www/html/index.html
        line: "Secret code is {{ secret_key }}"
      become: yes
```

## Conclusion

Using Ansible Vault in your playbooks allows you to manage your automation scripts while keeping sensitive data secure. Whether you’re managing passwords, API keys, or other secrets, Ansible Vault provides a robust mechanism to encrypt this data and use it securely in your playbooks. Remember to keep the Vault password secure and use best practices for password management. Happy automating!