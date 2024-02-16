+++
title = "Securely transfer files between systems"
date = "2024-02-16T11:47:31-05:00"
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


# Tutorial: Securely Transfer Files Between Systems

In this tutorial, we will cover the Red Hat Certified Systems Administrator Exam 200 Objective: "Securely Transfer Files Between Systems". This objective aims to test your ability to securely transfer files between systems in a Red Hat environment. In today's digital world, the ability to safely and efficiently transfer files between systems is a crucial skill for any system administrator. So, let's get started.

## Requirements

To complete this objective, you will need:
- Two Red Hat systems (could be virtual machines or physical machines)
- Basic knowledge of command line operations
- Basic knowledge of file permissions and ownership
- Basic understanding of networking and IP addresses

## Step 1: Understanding the Different Methods of File Transfer

Before we dive into the actual transfer process, let's take a moment to understand the different methods of file transfer. There are two main ways to transfer files between systems: Secure Copy (SCP) and File Transfer Protocol (FTP).

**Secure Copy (SCP)** is a secure method of transferring files between systems using the Secure Shell (SSH) protocol. It uses encryption to protect the transferred files, making it a more secure option compared to FTP. SCP also has the advantage of being able to transfer files and folders recursively, meaning it can transfer entire directories with their subdirectories and files.

**File Transfer Protocol (FTP)** is a standard network protocol used for transferring files between a client and a server. FTP doesn't provide encryption by default, making it less secure than SCP. However, it does have the advantage of being a widely supported protocol and offers more advanced features like resume download and file compression.

In this tutorial, we will focus on using SCP for securely transferring files between systems.

## Step 2: Setting Up SSH on Both Systems

As we will be using SCP, we need to ensure that both systems have SSH installed and configured. You can check if your system already has SSH installed by running the following command in the terminal:

```
ssh -V
```

If SSH is not installed, you can install it by using the package manager for your respective system.

For Red Hat Enterprise Linux (RHEL), you can use the following command to install SSH:

```
yum install openssh-server openssh-clients
```

Once SSH is installed, you will need to start the SSH service and ensure it gets started automatically on boot. To do this, run the following commands:

```
systemctl start sshd
systemctl enable sshd
```

Note: In cases where the server does not use systemd, you can start and enable SSH by running the following commands:

```
service sshd start
chkconfig sshd on
```

Repeat these steps on both systems.

## Step 3: Generating SSH Keys

To improve security and efficiency, we will now generate SSH keys on the system from which we will transfer the files (i.e. the client system). Generating SSH keys involves creating a public and private key pair. The public key will be stored on the receiving system (i.e. the server system), and the private key will be kept on the client system.

On the client system, run the following command to generate the keys:

```
ssh-keygen -t rsa
```

This will prompt you to choose a location to save the keys and to optionally provide a passphrase for added security. For this tutorial, let's keep the default location and leave the passphrase blank.

Once the keys are generated, you can view the public key by running the following command:

```
cat ~/.ssh/id_rsa.pub
```

Copy the output of this command as we will need it in the next step.

## Step 4: Adding the Public Key to the Server System

On the server system, we need to add the public key to the authorized_keys file. This file contains a list of public keys that are allowed to connect to the server via SSH. To do this, we will use the SSH-copy-id command.

Run the following command on the server system, replacing <public_key> with the key you copied in the previous step:

```
ssh-copy-id -i <public_key> <remote_username>@<server_ip_address>
```

This will prompt you for the password of the remote user. Enter the password and press enter to add the key to the authorized_keys file.

## Step 5: Securely Transferring Files

Now that SSH is set up and the keys have been exchanged, we can securely transfer files between the two systems. We will use the scp command to do this.

The basic syntax for scp is as follows:

```
scp <source_file> <remote_username>@<server_ip_address>:<destination_file>
```

For example, to transfer a file named "test.txt" from the client system to the home directory of the remote user on the server, we would run the following command on the client system:

```
scp test.txt <remote_username>@<server_ip_address>:~
```

Similarly, we can transfer a file from the server to the client system by using the following command on the client system:

```
scp <remote_username>@<server_ip_address>:<source_file> <destination_file>
```

SCP also allows us to recursively transfer directories and their contents by using the -r flag. For example, to transfer a directory named "documents" from the client system to the server, we would use the following command:

```
scp -r documents <remote_username>@<server_ip_address>:~
```

## Step 6: Ensuring Proper File Permissions and Ownership

It's essential to ensure that the files transferred between systems have the correct permissions and ownership. To view the permissions and ownership of a file, we can use the ls command with the -l flag.

For example, to view the permissions and ownership of a file named "test.txt", we would use the following command:

```
ls -l test.txt
```

To change the permissions, we can use the chmod command. For example, to give read, write, and execute permissions to the owner of the file, we would run the following command:

```
chmod u+rwx test.txt
```

To change the ownership of a file, we can use the chown command. For example, to change the ownership of "test.txt" to the user "admin", we would run the following command:

```
chown admin test.txt
```

It's recommended to review and adjust the permissions and ownership of any transferred files to maintain proper security.

## Conclusion

Congratulations! You have now learned how to securely transfer files between systems in a Red Hat environment. By setting up SSH, exchanging keys, and using the SCP command, you can safely and efficiently transfer files between systems without worrying about security risks. Make sure to review the permissions and ownership of the transferred files to ensure proper security. Thank you for following this tutorial, and we hope it has been helpful in preparing you for the Red Hat Certified Systems Administrator Exam 200 Objective: "Securely Transfer Files Between Systems".
