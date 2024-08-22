# Tech Tutorial: Create and Configure File Systems

## Introduction

In this tutorial, we will delve into how to mount and unmount network file systems using NFS (Network File System). NFS is a distributed file system protocol that allows a user on a client computer to access files over a network in a manner similar to how local storage is accessed. This guide is crucial for system administrators and developers who need to manage file storage over a network efficiently.

## Prerequisites

Before proceeding, you should have the following:
- Two Linux machines (one as the NFS server and the other as the NFS client)
- Root or sudo privileges on both machines
- Basic understanding of Linux command line

## Step-by-Step Guide

### Step 1: Installing NFS

#### On the NFS Server:

1. Update your package repository.

   ```bash
   sudo apt update
   ```

2. Install the NFS kernel server package.

   ```bash
   sudo apt install nfs-kernel-server
   ```

#### On the NFS Client:

1. Update your package repository.

   ```bash
   sudo apt update
   ```

2. Install the NFS common package.

   ```bash
   sudo apt install nfs-common
   ```

### Step 2: Configuring the NFS Server

1. Create a directory to share with the client. This will be our mount point.

   ```bash
   sudo mkdir /var/nfs/general -p
   sudo chown nobody:nogroup /var/nfs/general
   ```

2. Grant the necessary permissions (read and write in this example).

   ```bash
   sudo chmod 777 /var/nfs/general
   ```

3. Edit the `/etc/exports` file to add the newly created directory.

   ```bash
   sudo nano /etc/exports
   ```

   Add the following line to the file:

   ```
   /var/nfs/general *(rw,sync,no_subtree_check)
   ```

   Explanation:
   - `*` means all hosts can access this directory.
   - `rw` specifies read and write permissions.
   - `sync` replies to requests only after the changes have been committed to stable storage.
   - `no_subtree_check` prevents subtree checking.

4. Export the shared directory.

   ```bash
   sudo exportfs -a
   ```

5. Restart the NFS service to apply changes.

   ```bash
   sudo systemctl restart nfs-kernel-server
   ```

### Step 3: Mounting the NFS on the Client

1. On the client machine, create a mount point.

   ```bash
   sudo mkdir /mnt/nfs_general
   ```

2. Mount the NFS shared directory.

   ```bash
   sudo mount server_ip:/var/nfs/general /mnt/nfs_general
   ```

   Replace `server_ip` with the IP address of your NFS server.

3. Verify the mount.

   ```bash
   df -h
   ```

   You should see an entry for the NFS mount in the output.

### Step 4: Unmounting the NFS

When you need to unmount the NFS, use the following command on the client machine:

```bash
sudo umount /mnt/nfs_general
```

If the device is busy, you might need to close all programs using the mount before unmounting.

## Detailed Code Examples

Here’s a script that automates the mounting of NFS on a client machine.

```bash
#!/bin/bash

# Define server IP and the shared directory
server_ip="192.168.1.10"
shared_dir="/var/nfs/general"
mount_point="/mnt/nfs_general"

# Create mount point
sudo mkdir -p $mount_point

# Mount NFS
sudo mount $server_ip:$shared_dir $mount_point

# Check the mounted NFS
df -h | grep nfs
```

## Conclusion

In this tutorial, we covered how to set up and manage a network file system using NFS. We installed necessary software, configured the NFS server, shared a directory, and mounted it on the NFS client. This setup is critical for managing data in distributed environments efficiently. Always ensure your network configurations and firewall settings allow proper communication between your NFS server and client.