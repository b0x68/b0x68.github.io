# Tech Tutorial: Operate Running Systems

## Exam Objective: Securely Transfer Files Between Systems

When operating and managing running systems, one of the fundamental tasks is the secure transfer of files between systems. This ensures that sensitive data is protected from unauthorized access and data integrity is maintained during transit. In this tutorial, we will explore how to securely transfer files using SSH (Secure Shell), SCP (Secure Copy Protocol), and SFTP (Secure FTP).

### Introduction

Transferring files between systems is a common task for system administrators and developers alike. However, using insecure methods can expose sensitive information and compromise network security. We will focus on using SSH-based tools which provide encryption, ensuring that files are securely transferred between systems.

### Step-by-Step Guide

#### 1. Setup SSH Keys for Authentication

Before transferring files, it's essential to set up SSH keys for secure and password-less authentication. 

**Step 1.1: Generate SSH Key Pair**

On the source system (the system from which files will be sent), generate an SSH key pair:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Follow the prompts to specify the file path and passphrase (optional but recommended for additional security).

**Step 1.2: Copy the Public Key to the Destination System**

Copy the public key to the destination system using the `ssh-copy-id` command:

```bash
ssh-copy-id username@destination_host
```

This will add the public key to the destination's `~/.ssh/authorized_keys` file, allowing SSH access without a password.

#### 2. Transfer Files Using SCP

SCP uses SSH to transfer data, providing the same security level while allowing easy file copying.

**Step 2.1: Basic SCP Command**

To copy a file from the local system to a remote system:

```bash
scp /path/to/local/file username@destination_host:/path/to/remote/directory
```

**Step 2.2: Copying a Directory Recursively**

If you need to copy an entire directory, use the `-r` option:

```bash
scp -r /path/to/local/directory username@destination_host:/path/to/remote/directory
```

#### 3. Transfer Files Using SFTP

SFTP provides a secure way to access, transfer, and manage files over a fully encrypted SSH transport.

**Step 3.1: Connect to the SFTP Server**

Start an SFTP session with the remote system:

```bash
sftp username@destination_host
```

**Step 3.2: SFTP Commands**

Once connected, you can use SFTP commands to transfer files:

- `put localfile`: Uploads `localfile` to the remote system
- `get remotefile`: Downloads `remotefile` to the local system
- `ls`, `cd`, `mkdir`, `rm`: Manage files and directories

**Example: Uploading a File**

```bash
sftp> put /path/to/local/file
```

### Detailed Code Examples

Here’s a more detailed example using SFTP with batch commands to automate file transfers:

**Create a Batch File**

Create a text file named `sftp_batch.txt`:

```
put /path/to/local/file1
put /path/to/local/file2
bye
```

**Run SFTP with the Batch File**

```bash
sftp -b sftp_batch.txt username@destination_host
```

This will execute the commands in `sftp_batch.txt`, uploading `file1` and `file2` to the remote host.

### Conclusion

Securely transferring files between systems is crucial for maintaining data security and integrity. By using SSH, SCP, and SFTP, you can ensure that your file transfers are protected from eavesdropping and unauthorized access. Always ensure that your systems are using up-to-date SSH protocols and configurations to safeguard against potential vulnerabilities.