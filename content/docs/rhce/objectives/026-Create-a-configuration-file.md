# Tech Tutorial: Install and Configure an Ansible Control Node on RHEL

## Introduction

Ansible is a powerful automation tool that simplifies complex configuration tasks and consistency across large infrastructures. It is agentless and uses SSH to execute tasks on different nodes. In this tutorial, we will focus on setting up an Ansible control node on a Red Hat Enterprise Linux (RHEL) system. We will also create a basic configuration file, essential for tailoring Ansible's behavior to meet our needs.

## Prerequisites

- A RHEL 8 system with root or sudo privileges.
- Access to a terminal/command line interface.
- Basic familiarity with YAML (YAML Ain't Markup Language) syntax.

## Step-by-Step Guide

### Step 1: Installing Ansible on RHEL

Before installing Ansible, ensure that the system is updated:

```bash
sudo dnf update
```

Next, enable the EPEL (Extra Packages for Enterprise Linux) repository, which contains additional packages, including Ansible:

```bash
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
```

Now, install Ansible using the following command:

```bash
sudo dnf install ansible
```

To verify the installation, check the Ansible version:

```bash
ansible --version
```

### Step 2: Configuring SSH Access

Ansible communicates with nodes using SSH. It is recommended to set up SSH key-based authentication for secure and seamless operation.

Generate an SSH key pair on the control node:

```bash
ssh-keygen -t rsa -b 4096
```

Copy the public key to the target node(s) where you intend to manage configurations:

```bash
ssh-copy-id user@target-node-ip
```

### Step 3: Creating the Ansible Configuration File

Ansible looks for its configuration settings in several potential files on the control node. The default location is `/etc/ansible/ansible.cfg`. For more customized user-specific configurations, you can create an `ansible.cfg` in your home directory or within a project. We'll create one in the home directory for this example.

Navigate to your home directory:

```bash
cd ~
```

Create the configuration file:

```bash
touch ansible.cfg
```

Open this file using a text editor, such as vi or nano:

```bash
vi ansible.cfg
```

Paste the following basic configurations into the file:

```ini
[defaults]
inventory      = ./hosts
remote_user    = ansible_user
private_key_file = /path/to/private/key
host_key_checking = False
retry_files_enabled = False
```

Here’s what each setting means:
- **inventory**: Path to the inventory file that lists your nodes.
- **remote_user**: Default SSH user for Ansible to log in as.
- **private_key_file**: Path to SSH private key file.
- **host_key_checking**: Disables SSH host key checking. Useful in automated environments.
- **retry_files_enabled**: Prevents creation of *.retry files on failed attempts.

Save and exit the file.

### Step 4: Testing the Configuration

Create a simple inventory file in your home directory:

```bash
echo 'test-server ansible_host=192.168.1.100' > hosts
```

Run a basic Ansible command to check connectivity:

```bash
ansible all -m ping
```

You should receive a success message from all specified hosts.

## Conclusion

Setting up an Ansible control node on RHEL is straightforward but crucial for automating and managing your infrastructure efficiently. By following this guide, you have installed Ansible, set up SSH key-based authentication, and configured the basic settings necessary for Ansible operations. From here, you can begin defining playbooks to automate various tasks across your environments. Always ensure to tailor the configuration settings as per your organizational policies and infrastructure requirements.