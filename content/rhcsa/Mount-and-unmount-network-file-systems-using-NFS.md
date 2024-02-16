+++
title = "Mount and unmount network file systems using NFS"
date = "2024-02-16T10:34:02-05:00"
author = "root"
cover = ""
tags = ["command", "network,", "linux", "(network", "reboots", "unmount", "`umount`", "terminal"]
keywords = ["unmounting,", "unmounting?", "mounting", "network", "reboot", "configuration", "process", "commands:"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


## Introduction

Welcome to this comprehensive tutorial on how to mount and unmount network file systems using NFS. This tutorial is designed to help you prepare for the Red Hat Certified Systems Administrator (RHCSA) Exam 200 objective and gain a strong understanding of NFS file systems.

NFS (Network File System) is a distributed file system protocol that allows a client computer to access files over a network as if they were stored locally. With NFS, you can easily share files and resources between multiple computers within a network, making it a popular choice for enterprise environments. Being able to mount and unmount NFS file systems is a crucial skill for any system administrator, and this tutorial will guide you through the process step-by-step.

## Prerequisites

Before we dive into the tutorial, let’s first go through the prerequisites to ensure you have all the necessary tools and knowledge to follow along.

1. A basic understanding of Linux operating systems such as Red Hat Enterprise Linux or CentOS.
2. A terminal or command line interface on your system.
3. Access to a network that supports NFS.
4. Basic knowledge of networking and file systems.

## What is Mounting and Unmounting?

Before we get into the specifics of NFS, let's briefly understand the concepts of mounting and unmounting in Linux.

Mounting is the process of making a file system accessible to the system by attaching it to a specified directory (known as the mount point). This allows the system to access and read the files in the file system.

Unmounting, on the other hand, is the process of making a file system inaccessible to the system and detaching it from the mount point. This is important to ensure that all changes made to the files in the file system are properly saved and no data is lost.

## Setting Up NFS Server

Before we can start working with NFS, we need to set up an NFS server to share files with our client machine. For the purpose of this tutorial, we will use a CentOS machine as our NFS server. 

1. Install NFS server on your CentOS machine using the following command:

`sudo yum install nfs-utils`

2. Next, open the NFS configuration file located at `/etc/exports` using your preferred text editor.

`sudo vi /etc/exports`

3. In the exports file, specify the directory you want to share and the client machine that can access it. For example:

`/home/users 192.168.1.100(rw,sync)`

This exports the `/home/users` directory on your NFS server to the client with IP address `192.168.1.100` and allows it to read and write to the shared directory.

4. Once you have added all the necessary entries, save and close the file.

5. Finally, start the NFS server and enable it to start on boot using the following commands:

```
sudo systemctl start nfs-server
sudo systemctl enable nfs-server
```

## Mounting NFS File Systems

Now that our NFS server is set up, we can move on to the process of mounting NFS file systems on our client machine.

1. First, create a mount point on the client machine where we will attach the NFS file system. For example:

`sudo mkdir /mnt/nfs`

2. Next, we need to mount the NFS file system to the mount point using the following command:

`sudo mount -t nfs <NFS server IP>:/home/users /mnt/nfs`

The `-t` flag specifies the type of file system, in this case, NFS. Replace `<NFS server IP>` with the IP address of your NFS server.

3. If the mount command is successful, you can view the contents of the NFS file system by running the `ls` command on the mount point directory.

4. By default, NFS shares are mounted as read-only. If you want to mount the NFS file system as read-write, add the `rw` option in the mount command as follows:

`sudo mount -t nfs -o rw <NFS server IP>:/home/users /mnt/nfs`

## Unmounting NFS File Systems

Unmounting NFS file systems is just as crucial as mounting them. It's important to properly unmount NFS shares to ensure that all changes are saved and no data is lost.

1. To unmount an NFS share, first navigate to the mount point directory using the `cd` command.

2. Then, use the `umount` command followed by the mount point to unmount the NFS file system. For example:

`sudo umount /mnt/nfs`

3. If the command is successful, the NFS file system will be detached from the mount point and the directory will be empty.

## Mounting NFS File Systems Automatically on Boot

Manually mounting NFS file systems every time your client machine reboots can be time-consuming and inefficient. To avoid this, we can configure the client to automatically mount NFS file systems on boot.

1. To do this, open the `/etc/fstab` file on your client machine using a text editor.

`sudo vi /etc/fstab`

2. Add the entry for your NFS file system at the end of the file in the following format:

`<NFS server IP>:/home/users    /mnt/nfs    nfs    defaults    0  0` 

The first field specifies the NFS server and directory, the second field is the mount point, and the third field is the type of file system. The `defaults` option uses the default options for mounting the file system. The last two fields specify the dump and pass values, which are set to 0 in this case.

3. Save and close the file.

4. To test the configuration, reboot your client machine and verify that the NFS file system is automatically mounted on boot.

## Conclusion

Congratulations! You have successfully learned how to mount and unmount NFS file systems and configure them to be mounted automatically on boot. These are essential skills for any system administrator and will also help you in your preparation for the RHCSA Exam 200.

Remember to always properly unmount NFS file systems to avoid data loss and keep your system running smoothly. Also, double check the exports and fstab configuration to avoid any errors.

Thank you for following along with this tutorial. With practice and experience, you will become proficient in working with NFS file systems and ace your RHCSA exam. Good luck!