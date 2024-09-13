# Tech Tutorial: Operate Running Systems

## Exam Objective: Securely Transfer Files Between Systems

This tutorial is designed specifically for aspiring Red Hat Certified System Administrators (RHCSA) who need to master the skills of securely transferring files between systems. We'll focus on using secure methods appropriate for Red Hat Enterprise Linux (RHEL) distributions.

### Introduction

In the realm of system administration, securely transferring files between systems is a fundamental skill. Whether you're updating configurations, deploying applications, or backing up data, ensuring the integrity and security of your data during transit is crucial. For RHEL systems, several tools and protocols can be utilized to achieve secure file transfers, including `scp`, `rsync`, and `sftp`. This tutorial will cover these tools, providing real-world examples that you might encounter in your day-to-day operations as a systems administrator.

### Step-by-Step Guide

#### 1. Secure Copy Protocol (SCP)

`scp` is a simple tool built over SSH (Secure Shell) that allows for the secure transfer of files between computers. It uses the same authentication and provides the same security as SSH.

**Example: Copying a File from a Local Computer to a Remote Server**

```bash
# Syntax: scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2
scp /path/to/local/file.txt username@192.168.1.5:/path/to/remote/directory/
```
This command will copy `file.txt` from the local system to the specified directory on the remote server with the IP address `192.168.1.5`.

**Options to Note:**
- `-P port`: Specifies the SSH port if it is not the default port (22).
- `-i identity_file`: Specifies the private key to use.
- `-r`: Recursively copy entire directories.

**Example: Copying a Directory from a Local Computer to a Remote Server**

```bash
scp -r /path/to/local/directory username@192.168.1.5:/path/to/remote/directory/
```

#### 2. Rsync

`rsync` is another powerful tool used for efficiently transferring and synchronizing files across computer systems, using the delta encoding when appropriate. `rsync` can compress and decompress data on the fly, saving bandwidth.

**Example: Syncing a Local Directory with a Remote Directory**

```bash
# Syntax: rsync options source destination
rsync -avz /path/to/local/directory username@192.168.1.5:/path/to/remote/directory/
```
**Key Options:**
- `-a`: Archive mode, which preserves permissions, symlinks, etc.
- `-v`: Verbose mode.
- `-z`: Compress data during the transfer.

#### 3. Secure File Transfer Protocol (SFTP)

`sftp` is a secure file transfer protocol that provides a secure encrypted method for transferring files over a network.

**Example: Transferring Files Using SFTP**

1. Start an SFTP session:
```bash
sftp username@192.168.1.5
```

2. Navigate and transfer files within the SFTP shell:
```sftp
cd remote_directory
lcd local_directory
put local_file.txt
get remote_file.txt
```

3. Exit the SFTP shell:
```sftp
exit
```

### Detailed Code Examples

Let's consider a scenario where you need to backup a local directory `/var/www/html` to a remote backup server `backup.mydomain.com`.

Using `scp`:
```bash
scp -r -i ~/.ssh/id_rsa_backup /var/www/html username@backup.mydomain.com:/backups/
```

Using `rsync`:
```bash
rsync -avz -e "ssh -i ~/.ssh/id_rsa_backup" /var/www/html username@backup.mydomain.com:/backups/
```

### Conclusion

Mastering secure file transfer techniques is essential for anyone managing RHEL systems. By using `scp`, `rsync`, and `sftp`, you can ensure your data is securely moved or synchronized between systems, protecting your infrastructure against data breaches and leaks. Practice these commands, understand the options, and apply them in different scenarios to become proficient in securely managing files in RHEL environments.