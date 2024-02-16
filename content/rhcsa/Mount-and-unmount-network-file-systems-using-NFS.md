+++
title = "Mount and unmount network file systems using NFS"
date = "2024-02-16T11:48:56-05:00"
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
In this tutorial, we will be covering how to mount and unmount network file systems using NFS (Network File System) for the Red Hat Certified Systems Administrator Exam 200 Objective. NFS is a commonly used protocol for sharing files over a network. We will go through the step-by-step process of configuring NFS on both the server and client side, as well as how to mount and unmount NFS file systems.

## Prerequisites
- Red Hat Enterprise Linux operating system installed on both the server and client machines
- Basic understanding of networking and file systems
- Root privileges on the server and client machines

## Step 1: Install NFS
First, we need to make sure that the NFS package is installed on both the server and client machines. To do this, we will use the following command in the terminal:

`yum install nfs-utils`

This command will install all the necessary packages and dependencies for NFS to work.

## Step 2: Configure the NFS Server
Once the NFS package is installed, we can start configuring the NFS server. The server will be the machine where we want to share files from. We will need to make some changes to the `/etc/exports` file to specify which directories we want to share and with whom. To edit the file, use the following command:

`vi /etc/exports`

In this file, we will add a line for each directory we want to share. The basic syntax is as follows:

`/directory/to/share <client-ip>(options)`

For example, if we want to share the `/home` directory with a client with the IP address 192.168.1.100, we would add the following line to the `/etc/exports` file:

`/home 192.168.1.100(rw,sync)`

This means that the `/home` directory will be shared with the client with read-write access and any changes made by the client will be synchronized with the server. There are many more options that can be used, but we will cover the basics in this tutorial.

Once all the necessary directories are added, save and exit the file.

## Step 3: Start the NFS Service
Before we can start using NFS, we need to start the NFS service. To do this, we will use the following command:

`systemctl start nfs`

We can also make sure that the service starts automatically upon boot by using the following command:

`systemctl enable nfs`

## Step 4: Configure the Firewall
If you are running a firewall on either the server or client machines, you will need to make sure that NFS traffic is allowed. To do this, we will need to add some rules to the firewall. The commands may vary depending on the type of firewall you are using. Here are some examples for the `firewalld` and `iptables` firewalls:

### firewalld
To allow NFS traffic through the `firewalld` firewall, we will need to add the appropriate service to the allowed services list. To do this, use the following command:

`firewall-cmd --add-service=nfs –permanent`

This will allow NFS traffic through port 2049. If you want to specify a port, you can use the following command:

`firewall-cmd --add-port=<port number>/tcp`

Once the appropriate rules are added, we need to reload the firewall for the changes to take effect by running the following command:

`firewall-cmd --reload`

### iptables
To allow NFS traffic through the `iptables` firewall, we will need to add some rules to the firewall. Here are the basic commands needed to allow the necessary ports:

`iptables -A INPUT -p tcp --dport 2049 -j ACCEPT`

`iptables -A INPUT -p udp --dport 2049 -j ACCEPT`

`service iptables save`

These commands will allow NFS traffic to go through ports 2049 for both TCP and UDP protocols.

## Step 5: Configure the NFS Client
Now that the server is configured and the necessary rules are in place, we can move on to configuring the client machine. The client is the machine that will be accessing the shared files from the NFS server. We will need to make some changes to the `/etc/fstab` file to mount the NFS file system. To edit the file, use the following command:

`vi /etc/fstab`

At the bottom of the file, we will add a line to mount the NFS file system. The basic syntax is as follows:

`<server-ip>:/directory/on/server /local/directory nfs <options> 0 0`

For example, if the server's IP address is 192.168.1.200 and we want to mount the `/home` directory, we will add the following line:

`192.168.1.200:/home /mnt/nfs nfs rw,sync 0 0`

This means that the `/home` directory from the server will be mounted into the `/mnt/nfs` directory on the client with read-write access and any changes made by the client will be synchronized with the server. Save and exit the file.

## Step 6: Mount the NFS File System
Now that the necessary configurations have been made on both the server and client sides, we can proceed to mount the NFS file system. To do this, use the following command on the client machine:

`mount -a`

This will mount all the file systems specified in the `/etc/fstab` file. If everything is configured correctly, the NFS file system should now be mounted on the client machine.

## Step 7: Verify the NFS File System
To verify that the NFS file system was mounted successfully, we can use the `df` command to display all the currently mounted file systems. The output should include the NFS file system that we just mounted.

## Unmounting the NFS File System
To unmount the NFS file system, use the following command on the client machine:

`umount /mnt/nfs` (or whichever local directory you chose for mounting)

This will unmount the NFS file system from the client machine.

## Conclusion
In this tutorial, we covered how to configure and use NFS to mount and unmount network file systems. We went through the necessary steps of configuring both the server and client machines, as well as how to start the NFS service and make sure that the necessary firewall rules are in place. Remember to always check for any errors and make sure that the configurations are correct before proceeding with the exam. Good luck on your Red Hat Certified Systems Administrator Exam!