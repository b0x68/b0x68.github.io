# Tech Tutorial: Create and Configure File Systems

## Introduction

Network File System (NFS) is a distributed file system protocol that allows a user on a client computer to access files over a network in a manner similar to how local storage is accessed. NFS, originally developed by Sun Microsystems in 1984, has evolved through the years and is widely used in various computing environments. In this tutorial, we will cover the basics of mounting and unmounting network file systems using NFS on Linux systems. 

## Prerequisites

Before proceeding, ensure you have the following:
- Two Linux-based systems (one as NFS server and the other as NFS client)
- Sudo or root privileges on both systems
- Network connectivity between both systems

## Step-by-Step Guide

### Step 1: Installing NFS

#### On the NFS Server:
1. Open a terminal.
2. Install the NFS kernel server package:
   ```bash
   sudo apt-get update
   sudo apt-get install nfs-kernel-server
   ```

#### On the NFS Client:
1. Open a terminal.
2. Install the NFS common package:
   ```bash
   sudo apt-get update
   sudo apt-get install nfs-common
   ```

### Step 2: Configuring the NFS Server

1. Create a directory to share with the NFS client:
   ```bash
   sudo mkdir /var/nfsshare
   sudo chown nobody:nogroup /var/nfsshare
   sudo chmod 777 /var/nfsshare
   ```

2. Edit the NFS export file to configure sharing:
   ```bash
   sudo nano /etc/exports
   ```
   Add the following line to allow the client full access:
   ```plaintext
   /var/nfsshare <client-ip>(rw,sync,no_subtree_check)
   ```
   Replace `<client-ip>` with the actual IP address of your NFS client.

3. Export the shared directory:
   ```bash
   sudo exportfs -a
   ```

4. Restart the NFS service to apply changes:
   ```bash
   sudo systemctl restart nfs-kernel-server
   ```

### Step 3: Mounting the NFS on the Client

1. On the client machine, create a mount point:
   ```bash
   sudo mkdir /mnt/nfs_clientshare
   ```

2. Mount the NFS share from the server:
   ```bash
   sudo mount <server-ip>:/var/nfsshare /mnt/nfs_clientshare
   ```
   Replace `<server-ip>` with the IP address of your NFS server.

3. Verify that the NFS mount was successful:
   ```bash
   df -h
   ```
   Look for an entry that shows the server’s share mounted on `/mnt/nfs_clientshare`.

### Step 4: Testing File Sharing

1. Create a test file on the server:
   ```bash
   echo "Hello from Server" | sudo tee /var/nfsshare/testfile.txt
   ```

2. Access this file from the client:
   ```bash
   cat /mnt/nfs_clientshare/testfile.txt
   ```
   This should display "Hello from Server".

### Step 5: Unmounting the NFS Share

When the shared resources are no longer needed, you can unmount the NFS share:
```bash
sudo umount /mnt/nfs_clientshare
```

## Conclusion

In this tutorial, we covered how to set up an NFS server and client, share a directory, mount it on a client system, and perform basic file operations. NFS is a powerful tool for managing files over a network and can be particularly useful in environments where files need to be accessed and shared across different systems. By following these steps, you can successfully deploy NFS in your network.