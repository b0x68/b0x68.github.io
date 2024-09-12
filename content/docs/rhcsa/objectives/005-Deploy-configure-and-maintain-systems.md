# Tech Tutorial: Perform Tasks Expected of a Red Hat Certified System Administrator (RHCSA)

## Introduction

This tutorial covers key aspects of deploying, configuring, and maintaining systems, which are crucial for the Red Hat Certified System Administrator (RHCSA) exam. We will focus on Red Hat Enterprise Linux (RHEL) commands and configurations, demonstrating practical examples and scenarios encountered in a real-world environment.

Our goal is to ensure you understand how to handle RHEL systems efficiently, focusing on installation, service management, and system maintenance. By the end of this tutorial, you should be able to set up a RHEL system, configure it for various roles, and perform regular maintenance tasks.

## Step-by-Step Guide

### 1. System Deployment
#### Installing RHEL
To install Red Hat Enterprise Linux, you need either a bootable USB drive or a DVD with the RHEL image. Here's how to start:

1. **Download the ISO Image**: Go to the Red Hat Customer Portal and download the latest RHEL ISO image.
2. **Create Bootable Media**: Use the `dd` command to create a bootable USB drive:
   ```bash
   dd if=/path/to/rhel.iso of=/dev/sdX bs=4M status=progress oflag=sync
   ```
   Replace `/dev/sdX` with your USB drive identifier.
3. **Boot from Media**: Insert the USB drive into the system and boot from it, initiating the installation process.
4. **Installation Setup**: Follow the on-screen instructions, selecting the appropriate timezone, software selection (e.g., Server with a GUI), and disk partitioning.

#### Setting the Hostname
After installation, set your machine’s hostname using the `hostnamectl` command:
```bash
hostnamectl set-hostname your-hostname.example.com
```

### 2. System Configuration
#### Network Configuration
Configure the network to ensure your system can communicate on your network:
1. **Find the Network Interface**
   ```bash
   nmcli device status
   ```
2. **Edit the Network Configuration** for the interface (e.g., `enp0s3`):
   ```bash
   nmcli con modify enp0s3 ipv4.addresses 192.168.1.100/24
   nmcli con modify enp0s3 ipv4.gateway 192.168.1.1
   nmcli con modify enp0s3 ipv4.dns 8.8.8.8
   nmcli con modify enp0s3 ipv4.method manual
   nmcli con up enp0s3
   ```

#### Managing Services with `systemctl`
To start, stop, enable, or disable services:
```bash
systemctl start httpd
systemctl enable httpd
systemctl status httpd
systemctl stop httpd
systemctl disable httpd
```

### 3. System Maintenance
#### Updating the System
Regular updates are crucial for security and stability:
```bash
yum update
```

#### Managing Users
Add a user and assign a password:
```bash
useradd johndoe
passwd johndoe
```
Add the user to the sudoers file using `visudo` or by editing `/etc/sudoers.d/johndoe`:
```bash
echo "johndoe ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/johndoe
```

#### Scheduled Tasks with `cron`
Edit the crontab file for scheduling tasks:
```bash
crontab -e
```
Add a line to run a script every day at midnight:
```
0 0 * * * /path/to/script.sh
```

## Conclusion

This tutorial covered essential tasks for deploying, configuring, and maintaining a Red Hat Enterprise Linux system as expected for a Red Hat Certified System Administrator. By learning these fundamentals, you'll be better prepared to handle RHEL systems in a production environment and succeed in the RHCSA exam. Remember, practice is key to mastering these skills, so set up your own RHEL environment to test out these commands and configurations.

Good luck with your RHCSA preparation!