# Tech Tutorial: Ensuring Persistent Configurations in Red Hat Enterprise Linux

## Introduction

In the Red Hat Certified System Administrator (RHCSA) exam, one of the key objectives is ensuring that system configurations persist after a reboot. This is crucial for maintaining the desired state of a system across restarts, which is a common scenario in real-world environments. This tutorial focuses on methods and best practices for making configuration changes permanent in Red Hat Enterprise Linux (RHEL).

## Step-by-Step Guide

Below, we will explore various scenarios and configurations that are commonly required to be persistent across reboots, such as network configurations, service management, and scheduled tasks.

### 1. Ensuring Network Configuration Persistence

In RHEL, network configurations are managed with the `nmcli` tool or by editing configuration files in `/etc/sysconfig/network-scripts/`.

#### Using `nmcli`

`nmcli` is a command-line tool for managing NetworkManager, which is the default tool for network configuration in RHEL.

**Example: Setting a static IP address**

```bash
nmcli con mod enp0s3 ipv4.addresses 192.168.122.100/24
nmcli con mod enp0s3 ipv4.gateway 192.168.122.1
nmcli con mod enp0s3 ipv4.dns 8.8.8.8
nmcli con mod enp0s3 ipv4.method manual
nmcli con up enp0s3
```

These commands configure a static IP, set the gateway, and specify the DNS server. The changes made with `nmcli` are automatically saved and will persist across reboots.

#### Editing Configuration Files

For those who prefer or require direct file manipulation, configurations can be manually edited.

**Example: Configure a static IP by editing interface script**

```bash
# Edit the network script for the interface
sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s3

# Add the following content:
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.122.100
PREFIX=24
GATEWAY=192.168.122.1
DNS1=8.8.8.8
```

After editing, restart the network service to apply changes:
```bash
sudo systemctl restart NetworkManager
```

### 2. Ensuring Service Persistence

To ensure that services start automatically on boot, use the `systemctl` command.

**Example: Enabling and starting the Apache HTTP Server**

```bash
sudo systemctl enable httpd
sudo systemctl start httpd
```

The `enable` command configures the service to start at boot time.

### 3. Persistent Scheduled Tasks with `cron`

Scheduled tasks in RHEL are managed with `cron`. To create a task that persists after a reboot, add it to the crontab.

**Example: Creating a backup script that runs daily**

First, create the script `/home/user/backup.sh`:

```bash
#!/bin/bash
tar -czf /home/user/backup.tar.gz /home/user/data
```

Make the script executable:
```bash
chmod +x /home/user/backup.sh
```

Edit the crontab:
```bash
crontab -e
```

Add the following line to schedule the script to run daily at midnight:
```
0 0 * * * /home/user/backup.sh
```

## Conclusion

In this tutorial, we've covered several fundamental techniques to ensure configuration persistence in Red Hat Enterprise Linux. By mastering these techniques, you can ensure that your system configurations—whether they're network settings, service configurations, or scheduled tasks—remain intact through reboots. This knowledge is essential for passing the RHCSA exam and for effective system administration in real-world environments. Remember, practicing these configurations will not only prepare you for the exam but also enhance your skills as a Linux administrator.