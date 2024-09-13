# Tech Tutorial: Managing Sensitive Data with Ansible Vault in Red Hat Enterprise Linux

## Introduction

In this tutorial, we are going to explore how to use Ansible Vault, a feature of Ansible that allows users to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in your playbooks or roles. This is particularly crucial in a production environment or any scenario where security is a priority. 

This tutorial aligns with the Red Hat Certified Engineer (RHCE) exam objectives and focuses exclusively on using Ansible within a Red Hat Enterprise Linux (RHEL) environment. We'll walk through how to create, edit, and use encrypted files with Ansible Vault in your playbooks.

## Prerequisites

- A working RHEL system (version 7 or higher).
- Ansible installed on your RHEL system. You can install Ansible on RHEL with `sudo yum install ansible`.
- Basic understanding of YAML and Ansible playbooks.

## Step-by-Step Guide

### Step 1: Installing Ansible

If Ansible is not yet installed on your RHEL system, you can install it using the following command:

```bash
sudo yum install ansible
```

### Step 2: Creating an Encrypted File with Ansible Vault

To create a new encrypted file, use the `ansible-vault create` command. Let’s create a file named `secrets.yml`:

```bash
ansible-vault create secrets.yml
```

Upon executing the command, you will be prompted to enter a password. This password will be required to edit, view, or decrypt the file later.

Enter the following content when the editor opens:

```yaml
secret_key: mysupersecretpassword
```

Save and close the file. The content is now encrypted.

### Step 3: Viewing and Editing an Encrypted File

To view the contents of the encrypted file:

```bash
ansible-vault view secrets.yml
```

To edit the contents of the encrypted file:

```bash
ansible-vault edit secrets.yml
```

Both commands will ask for the password you set when you created the file.

### Step 4: Using Encrypted Files in Playbooks

You can easily use the variables stored in your encrypted file within your Ansible playbooks. Here is an example playbook that uses the `secrets.yml`:

```yaml
---
- hosts: all
  vars_files:
    - secrets.yml
  tasks:
    - name: Print a secret
      debug:
        msg: "The secret key is {{ secret_key }}"
```

### Step 5: Running Playbooks with Encrypted Files

To run a playbook that includes an encrypted file, you must provide the vault password. You can do this in several ways:

#### Option 1: Interactive Prompt

Use the `--ask-vault-pass` flag to be prompted for the password:

```bash
ansible-playbook playbook.yml --ask-vault-pass
```

#### Option 2: Password File

For automation purposes, you might want to store the vault password in a file (ensure this file is secured with appropriate permissions). Let’s assume the password is stored in a file named `.vault_pass.txt`:

```bash
ansible-playbook playbook.yml --vault-password-file .vault_pass.txt
```

## Conclusion

In this tutorial, we have covered how to manage sensitive data securely using Ansible Vault in a RHEL environment. We've learned how to create, edit, view, and use encrypted files in our Ansible playbooks. Implementing Ansible Vault in your Ansible projects is a best practice that enhances security by protecting sensitive data, making it a crucial skill for systems administrators and engineers preparing for the RHCE exam.

Remember, always handle encryption keys and sensitive data with care, ensuring they are protected and accessible only to authorized personnel. Happy automating!