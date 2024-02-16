+++
title = "Configure key-based authentication for SSH"
date = "2024-02-16T11:52:58-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


## Introduction

In this tutorial, we will explain in great depth the objective of "Configure key-based authentication for SSH" for the Red Hat Certified Systems Administrator Exam 200. SSH (Secure Shell) is a widely used protocol for remotely accessing and managing systems. By configuring key-based authentication for SSH, we can enhance the security of remote access to our systems by using public and private keys instead of traditional password authentication.

## Prerequisites

Before we begin, you should have a basic understanding of SSH and its configuration. You should also have a Red Hat Enterprise Linux (RHEL) system with SSH installed, as well as a user with root privileges to perform the necessary configurations.

## Step 1: Generating the public and private keys

The first step in configuring key-based authentication for SSH is to generate the necessary public and private keys. These keys will be used instead of passwords to authenticate remote users.

1.1. Log into your RHEL system with root privileges.

1.2. Navigate to the `.ssh` directory in the home directory of the user you want to use for SSH access.

1.3. If the `.ssh` directory does not exist, create it by using the `mkdir` command:

```
mkdir .ssh
```

1.4. Change the permissions of the `.ssh` directory to be accessible only by the user:

```
chmod 700 .ssh
```

1.5. Navigate to the `.ssh` directory and generate the key pair using the `ssh-keygen` command:

```
cd .ssh
ssh-keygen
```

1.6. The `ssh-keygen` command will prompt you for the location to save the keys and ask you to enter a passphrase (optional). Press Enter to use the default location and leave the passphrase blank if you don't want to use one.

1.7. Once the keys have been generated, you will see two files: `id_rsa` (private key) and `id_rsa.pub` (public key).

## Step 2: Configuring the server for key-based authentication

The next step is to configure the server to accept the public key for remote authentication.

2.1. Navigate to the `/etc/ssh` directory and open the `sshd_config` file in a text editor:

```
cd /etc/ssh
vi sshd_config
```

2.2. Look for the following line in the `sshd_config` file and make sure it is uncommented:

```
PubkeyAuthentication yes
```

2.3. If the line is commented out, remove the `#` symbol at the beginning of the line.

2.4. Save and close the `sshd_config` file.

2.5. Restart the SSH service for the changes to take effect:

```
systemctl restart sshd
```

## Step 3: Configuring the client for key-based authentication

Now, we need to configure the client system to use the private key for remote authentication.

3.1. Log into the client system with the user you want to use for remote SSH access.

3.2. Navigate to the `.ssh` directory in the user's home directory.

3.3. Create a file called `config` using a text editor and add the following lines:

```
Host <server_hostname>
User <remote_username>
IdentityFile ~/.ssh/id_rsa
```

3.4. Replace `<server_hostname>` with the hostname or IP address of the server, and `<remote_username>` with the username used on the server for remote access.

3.5. Save the `config` file and close the text editor.

## Step 4: Testing the configuration

To test our configuration, we will try to log into the server using SSH with the configured user:

```
ssh <server_hostname>
```

If everything is configured correctly, SSH will use the private key to authenticate the user and allow remote access without requiring a password. If you have set a passphrase for the private key, you will be prompted to enter it.

## Conclusion

In this tutorial, we have explained in depth how to configure key-based authentication for SSH, which is a critical security measure for remote access to systems. By using public and private keys instead of passwords, we can enhance the security of our systems and protect them from potential attacks. Remember to always keep your private key secure and do not share it with anyone. 