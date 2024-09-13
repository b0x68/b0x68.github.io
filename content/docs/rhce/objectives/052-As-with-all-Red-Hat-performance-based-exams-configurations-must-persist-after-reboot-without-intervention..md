# Tech Tutorial: Manage Content and Ensure Configurations Persist After Reboot in RHEL

## Introduction

In the Red Hat Certified Engineer (RHCE) exam, a critical objective is to ensure that all configurations must persist after a system reboot. This is crucial as server environments need to maintain their state and settings to avoid service disruptions after maintenance periods, power failures, or routine reboots. This tutorial will guide you through various methods and best practices to manage content and make sure that your configurations remain intact after a reboot on a Red Hat Enterprise Linux (RHEL) system.

## Step-by-Step Guide

The following sections will cover different scenarios and configurations, demonstrating how to ensure they persist after a reboot.

### 1. Managing Service Configuration

Many system services are managed with `systemd`, the init system and system manager in RHEL. To ensure that a service starts automatically after a reboot, you must enable it via `systemctl`.

#### Example: Ensuring the `httpd` Service Persists After Reboot

```bash
# Install httpd if it's not already installed
sudo yum install httpd

# Start the httpd service
sudo systemctl start httpd

# Enable httpd service to start automatically on boot
sudo systemctl enable httpd

# Check the status to ensure it's active and enabled
sudo systemctl status httpd
```

Output should confirm that `httpd` is enabled and will start on boot.

### 2. Persistent Network Configuration

Network settings are crucial, and ensuring they persist after reboot is essential for remote access and connectivity.

#### Example: Setting a Static IP Address

Edit the interface configuration file using `vim` or your preferred editor. For instance, if your interface is `ens33`, you would edit `/etc/sysconfig/network-scripts/ifcfg-ens33`.

```bash
sudo vim /etc/sysconfig/network-scripts/ifcfg-ens33
```

Add or modify the following lines:

```plaintext
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

Save and exit the file. Restart the network service:

```bash
sudo systemctl restart network
```

### 3. Configuring and Persisting Firewall Rules

Firewall configurations are managed by `firewalld` on RHEL. To ensure your rules persist after reboot, you must save them permanently.

#### Example: Opening Port 80 for HTTP Traffic

```bash
# Add the rule
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent

# Reload firewalld to apply changes
sudo firewall-cmd --reload
```

### 4. Managing System Timezone

System timezone settings should also persist after reboots.

#### Example: Setting the Timezone

```bash
# Set the timezone to UTC
sudo timedatectl set-timezone UTC

# Check the timezone setting
timedatectl
```

### 5. Ensuring Custom Scripts Run at Boot

To run custom scripts at boot, you can utilize `cron` or `systemd`.

#### Example: Creating a systemd Service for a Custom Script

1. Create your script, e.g., `/usr/local/bin/myscript.sh`:

```bash
#!/bin/bash
echo "Hello, World!" > /var/tmp/myscript_output.txt
```

2. Make the script executable:

```bash
sudo chmod +x /usr/local/bin/myscript.sh
```

3. Create a systemd service file, e.g., `/etc/systemd/system/myscript.service`:

```bash
[Unit]
Description=My custom startup script

[Service]
Type=oneshot
ExecStart=/usr/local/bin/myscript.sh

[Install]
WantedBy=multi-user.target
```

4. Enable and start the service:

```bash
sudo systemctl enable myscript.service
sudo systemctl start myscript.service
```

## Conclusion

In this tutorial, we covered a variety of scenarios to manage content and ensure configurations persist after reboots in RHEL. By following these examples, you can ensure that your system maintains its intended state across reboots, which is crucial for maintaining reliability and availability in a production environment. Always test configurations after setting them to confirm they're applied and persist as expected.