# Tech Tutorial: Create and Configure File Systems

## Introduction
In this tutorial, we will explore how to mount and unmount network file systems using NFS (Network File System) on Red Hat Enterprise Linux (RHEL). NFS is a protocol that allows a user on a client machine to access files over a network in a manner similar to how local storage is accessed. This guide will specifically help in preparing for the Red Hat Certified System Administrator (RHCSA) exam, focusing only on applicable RHEL commands and configurations.

## Prerequisites
- Two RHEL systems (one as NFS server and the other as NFS client)
- Proper network connectivity between the two systems
- Root privileges on both systems

## Step-by-Step Guide

### 1. Setting Up the NFS Server

Before you can mount a file system through NFS on a client, you need to configure an NFS server that will serve the files.

#### Step 1.1: Install the NFS Package
On the server, you need to install the `nfs-utils` package, which provides NFS functionality.

```bash
sudo yum install nfs-utils
```

#### Step 1.2: Configure the NFS Exports
Decide which directory you want to share with the client machines. For this example, let’s share `/var/nfsshare`.

First, create the directory if it doesn't already exist:

```bash
sudo mkdir /var/nfsshare
```

Give it the appropriate permissions:

```bash
sudo chmod 755 /var/nfsshare
```

Next, configure the export by editing the `/etc/exports` file:

```bash
sudo nano /etc/exports
```

Add the following line to specify that the directory should be accessible by a client (replace `client_ip` with the actual IP address of your client):

```
/var/nfsshare client_ip(rw,sync,no_subtree_check)
```

#### Step 1.3: Start and Enable NFS Services
Enable and start the NFS server services:

```bash
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
```

Export the shared directory:

```bash
sudo exportfs -rav
```

### 2. Mounting NFS on the Client

#### Step 2.1: Install NFS Utilities
On the client system, install the `nfs-utils` package if it's not already installed.

```bash
sudo yum install nfs-utils
```

#### Step 2.2: Create a Mount Point
Create a directory to serve as the mount point for the NFS share:

```bash
sudo mkdir /mnt/nfs
```

#### Step 2.3: Mount the NFS Share
Mount the NFS share from the server:

```bash
sudo mount server_ip:/var/nfsshare /mnt/nfs
```

Replace `server_ip` with the IP address of your NFS server.

#### Step 2.4: Verify the Mount
Check the mounted NFS share:

```bash
mount | grep nfs
```

### 3. Making the NFS Mount Persistent

To ensure the NFS mount persists across reboots, add it to the `/etc/fstab` file on the client:

```bash
sudo nano /etc/fstab
```

Add the following line:

```
server_ip:/var/nfsshare /mnt/nfs nfs defaults 0 0
```

## Detailed Code Examples
The above configurations and commands are crucial for setting up and managing NFS in a RHEL environment. Ensure that each step is followed carefully, and replace placeholder values (such as IP addresses) with actual values from your network setup.

## Conclusion
Mounting and unmounting NFS file systems are essential skills for any system administrator, especially those preparing for the RHCSA exam on RHEL. This tutorial has covered how to set up an NFS server and client, mount and persistently mount NFS shares, and verify the mounts. By practicing these steps, you can ensure efficient management of network file systems in a RHEL environment.