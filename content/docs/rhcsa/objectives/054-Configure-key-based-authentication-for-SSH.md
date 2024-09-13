# Tech Tutorial: Manage Security Through Key-Based Authentication for SSH

## Introduction

Secure Shell (SSH) is an essential service that provides a secure channel for remote administration of systems. By default, SSH uses password-based authentication which can be prone to brute-force attacks. Key-based authentication offers a more secure alternative by requiring a private key to authenticate to a server, which significantly reduces the risk of unauthorized access.

In this tutorial, tailored specifically for the Red Hat Certified System Administrator (RHCSA) exam, we will explore how to configure key-based authentication for SSH on a Red Hat Enterprise Linux (RHEL) system. By the end of this guide, you will be able to set up and manage SSH keys to secure access to your RHEL servers.

## Prerequisites

- Two RHEL 8 or RHEL 9 systems (one to act as the server and the other as the client)
- Sudo privileges on both systems

## Step-by-Step Guide

### Step 1: Install OpenSSH Packages

First, ensure that the `openssh-server` and `openssh-clients` packages are installed on both your server and client machines.

```bash
sudo dnf install openssh-server openssh-clients -y
```

### Step 2: Configure SSH Service

On the server, start and enable the SSH service:

```bash
sudo systemctl start sshd
sudo systemctl enable sshd
sudo systemctl status sshd
```

### Step 3: Create SSH Key Pair on the Client

On the client machine, generate an RSA key pair:

```bash
ssh-keygen -t rsa -b 2048
```

When prompted, you can specify a file in which to save the key. Press Enter to accept the default location (`~/.ssh/id_rsa`). Optionally, enter a passphrase for added security or press Enter to leave it empty.

### Step 4: Copy the Public Key to the Server

Use the `ssh-copy-id` command to copy the public key to the server. Replace `username` with your actual user on the server and `server_ip` with the server's IP address:

```bash
ssh-copy-id username@server_ip
```

Enter your password when prompted. This command appends the public key to the `~/.ssh/authorized_keys` file on the server.

### Step 5: Test SSH Key-Based Authentication

Now, try logging into the server from the client using SSH:

```bash
ssh username@server_ip
```

If everything is set up correctly, you should log in to the server without being prompted for a password (unless you set a passphrase for your key).

### Step 6: Disable Password Authentication (Optional)

For increased security, consider disabling password authentication on the server. Edit the SSH configuration file:

```bash
sudo vi /etc/ssh/sshd_config
```

Find the following line and change it if necessary:

```plaintext
PasswordAuthentication no
```

Restart the SSH service to apply changes:

```bash
sudo systemctl restart sshd
```

## Conclusion

Key-based authentication for SSH enhances the security of your RHEL systems by leveraging cryptographic keys which are more resistant to brute-force attacks compared to traditional passwords. By following the steps in this tutorial, you have successfully configured and tested key-based SSH authentication on your RHEL system. This setup not only meets the security standards but also aligns with the best practices recommended for the RHCSA exam.

Remember, managing keys responsibly is crucial. Keep private keys secure and rotate them periodically to maintain the integrity of your system's security.