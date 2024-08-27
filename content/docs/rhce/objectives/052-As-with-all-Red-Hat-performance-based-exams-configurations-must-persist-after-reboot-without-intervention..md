# Tech Tutorial: Ensure Persistent System Configuration Across Reboots

## Introduction

In Red Hat and other Linux-based systems, ensuring that configurations persist after a reboot is crucial for maintaining the desired state of a system in production environments. This tutorial focuses on essential techniques and best practices to manage content and configurations to survive system reboots, which is a common objective in Red Hat performance-based exams.

## Step-by-Step Guide

### 1. Understanding System Initialization

Before diving into configuration, it's important to understand how Linux systems initialize. Linux uses different init systems to manage the startup process, with `systemd` being the most common in recent distributions like RHEL (Red Hat Enterprise Linux) 7 and above.

### 2. Using `systemd` for Persistent Services

**Example: Creating a Custom Service**

Suppose you want to ensure a custom script runs at boot time. Here’s how you can create a systemd service to accomplish this:

a. **Create a Bash Script**: First, write your script. For example, create `/usr/local/bin/mycustomscript.sh`:

```bash
#!/bin/bash
echo "This is a custom script running at boot" >> /var/log/customscript.log
```

Make sure the script is executable:

```bash
chmod +x /usr/local/bin/mycustomscript.sh
```

b. **Create a Systemd Service File**: Place this file in `/etc/systemd/system/` as `customscript.service`:

```ini
[Unit]
Description=My Custom Script

[Service]
ExecStart=/usr/local/bin/mycustomscript.sh

[Install]
WantedBy=multi-user.target
```

c. **Enable and Start the Service**:

```bash
systemctl enable customscript.service
systemctl start customscript.service
```

This service will now execute at each boot.

### 3. Managing Network Configurations

Network configurations are a common aspect that needs persistence. Here’s how to configure a static IP that persists across reboots:

a. **Edit the Network Interface Configuration File**: For a RHEL-based system, edit `/etc/sysconfig/network-scripts/ifcfg-<interface-name>`, for example, `ifcfg-eth0`:

```ini
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=8.8.4.4
```

b. **Restart the Network Service**:

```bash
systemctl restart network
```

### 4. Ensuring Firewall Rules Persist

Using `firewalld`, which is the default firewall management tool on RHEL, you can make sure your firewall rules are saved and restored on reboot:

a. **Add a Firewall Rule**:

```bash
firewall-cmd --permanent --add-port=8080/tcp
```

b. **Reload to Apply**:

```bash
firewall-cmd --reload
```

This rule will persist after reboot.

### 5. Persistent Storage Mounting

To ensure file systems are mounted at boot, update `/etc/fstab`:

**Example Entry for mounting a disk:**

```bash
UUID=your-uuid /mount/point ext4 defaults 0 2
```

Replace `your-uuid` with the UUID of the disk, and `/mount/point` with your desired mount point.

## Detailed Code Examples

- **systemd service**: The detailed steps in Section 2 provide a complete example of creating a persistent systemd service.
- **Network configuration**: Section 3 provides an example of setting a static IP configuration that persists through reboots.

## Conclusion

Ensuring that system configurations persist after reboots is essential for server administration and is a critical skill for Red Hat system administrators. By mastering services like `systemd`, network configurations, and `firewalld`, you can ensure that your systems maintain their desired state across reboots, which is not only a requirement in performance-based exams but also a best practice in real-world deployments.

This tutorial has covered fundamental concepts and provided detailed examples to help you succeed in managing persistent configurations in a Red Hat environment.