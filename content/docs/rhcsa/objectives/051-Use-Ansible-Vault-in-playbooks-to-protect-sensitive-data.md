# Tech Tutorial: Manage Content using Ansible Vault

## Introduction

Ansible Vault is a feature of Ansible that allows you to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in your playbooks or roles. This tutorial will guide you through the process of using Ansible Vault in the context of managing content, specifically focusing on the Red Hat Certified System Administrator (RHCSA) exam objectives. We'll cover how to create, edit, and use encrypted files in your Ansible playbooks on a Red Hat Enterprise Linux (RHEL) system.

## Prerequisites

- A working RHEL installation (RHEL 7 or RHEL 8)
- Ansible installed on your RHEL system
- Basic familiarity with YAML syntax and Ansible playbooks

## Step-by-Step Guide

### Step 1: Install Ansible

If Ansible is not already installed on your RHEL system, you can install it using the following YUM command:

```bash
sudo yum install ansible
```

### Step 2: Create a Directory for Your Project

Organize your Ansible projects in directories. For this tutorial, create a directory named `ansible-vault-demo`:

```bash
mkdir ~/ansible-vault-demo
cd ~/ansible-vault-demo
```

### Step 3: Create an Encrypted File Using Ansible Vault

To create a new encrypted file to store sensitive data (e.g., passwords, secret keys), use the `ansible-vault create` command. Let's create a file named `secrets.yml`:

```bash
ansible-vault create secrets.yml
```

You will be prompted to enter a password. Remember this password as you'll need it to edit or decrypt the file later.

In the editor that opens, add some sensitive data:

```yaml
secret_password: mySecretPass123!
```

Save and close the file.

### Step 4: Use the Encrypted File in a Playbook

Create a playbook `site.yml` in the `ansible-vault-demo` directory:

```yaml
---
- hosts: localhost
  tasks:
    - name: Output the secret
      debug:
        msg: "The secret password is {{ secret_password }}"
      vars_files:
        - secrets.yml
```

### Step 5: Running the Playbook with the Encrypted File

To run the playbook while decrypting the `secrets.yml` file, use the `--ask-vault-pass` option:

```bash
ansible-playbook site.yml --ask-vault-pass
```

Enter the password you set when creating `secrets.yml`, and the playbook should execute, displaying the secret password in the output.

### Step 6: Editing the Encrypted File

If you need to edit the encrypted file, use the following command:

```bash
ansible-vault edit secrets.yml
```

Again, you will be prompted for the password. After authentication, the file will open in an editor where you can make changes.

## Detailed Code Examples

Let’s expand the previous playbook to make it more practical by including tasks that use the secret data for configuration purposes.

```yaml
---
- hosts: localhost
  tasks:
    - name: Create a file with a secret content
      copy:
        content: "Here is a very secret content: {{ secret_password }}"
        dest: /tmp/secret_file.txt
      vars_files:
        - secrets.yml
```

Run this playbook as before:

```bash
ansible-playbook site.yml --ask-vault-pass
```

This task will create a file on the localhost in `/tmp/secret_file.txt` containing the secret content.

## Conclusion

In this tutorial, you've learned how to use Ansible Vault to securely manage sensitive data within your Ansible playbooks. By encrypting your sensitive data, you enhance the security of your systems and comply with best practices for configuration management. Remember, keeping your vault password safe and managing access to it is as important as the encryption itself. Happy automating!

This approach ensures that your sensitive data is securely handled and implemented in a controlled manner across your infrastructure, aligning with RHCSA exam objectives and real-world system administration tasks on RHEL systems.