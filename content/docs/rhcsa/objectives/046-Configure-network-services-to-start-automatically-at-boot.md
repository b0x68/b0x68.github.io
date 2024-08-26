# Tech Tutorial: Manage Basic Networking

## Introduction

In this tutorial, we will delve into configuring network services to start automatically at boot. This is a fundamental task for system administrators and network engineers who need to ensure that network functionalities such as internet connectivity, remote access, and file sharing are immediately available after a system starts. This capability is crucial for maintaining uptime and ensuring that services are consistently available without manual intervention each time the system restarts.

## Configure Network Services to Start Automatically at Boot

### Step-by-Step Guide

#### Step 1: Understanding Systemd and Network Services
Most modern Linux distributions use `systemd` as their init system and service manager, which includes handling how network services start during the boot process.

#### Step 2: Check the Status of Network Services
Before we enable any service to start at boot, first, we need to check its current status.

```bash
# Check the status of the NetworkManager service
sudo systemctl status NetworkManager
```

Output might look something like this:
```
● NetworkManager.service - Network Manager
   Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2023-09-19 14:58:19 UTC; 10min ago
 Main PID: 875 (NetworkManager)
    Tasks: 3 (limit: 4915)
   Memory: 5.4M
   CGroup: /system.slice/NetworkManager.service
           └─875 /usr/sbin/NetworkManager --no-daemon
```
If the service is not running, you can start it with:
```bash
sudo systemctl start NetworkManager
```

#### Step 3: Enable the Service to Start at Boot
To ensure that the network service starts automatically at boot, use the `enable` command:

```bash
sudo systemctl enable NetworkManager
```

This command creates a symbolic link from the system's `systemd` directories to the service's configuration file, ensuring it gets triggered at boot.

#### Step 4: Reboot and Verify
After enabling the service, reboot your system to ensure that the changes take effect:

```bash
sudo reboot
```

Once the system is back online, verify that the service started automatically:

```bash
systemctl status NetworkManager
```

### Detailed Code Examples

**Example 1: Enabling SSH Service**

SSH (Secure Shell) is a common network service used for secure remote management. Here's how to ensure it starts at boot:

1. **Check SSH Service Status**
   ```bash
   sudo systemctl status ssh
   ```

2. **Enable SSH Service**
   ```bash
   sudo systemctl enable ssh
   ```

3. **Restart and Verify**
   ```bash
   sudo reboot
   # After reboot
   systemctl status ssh
   ```

**Example 2: Setting up a Static IP**

Network configurations can also be managed to ensure consistent network settings. Here’s how to set a static IP that persists on reboot:

1. **Edit Netplan Configuration**
   ```yaml
   # /etc/netplan/01-netcfg.yaml
   network:
     version: 2
     ethernets:
       eth0:
         dhcp4: no
         addresses:
           - 192.168.1.100/24
         gateway4: 192.168.1.1
         nameservers:
           addresses:
             - 8.8.8.8
             - 8.8.4.4
   ```

2. **Apply Netplan Configuration**
   ```bash
   sudo netplan apply
   ```

3. **Check IP Address**
   ```bash
   ip addr show eth0
   ```

### Conclusion

Automating the startup of network services is a critical skill for maintaining reliable and efficient network operations. By using `systemd` and its commands, administrators can ensure that essential services like NetworkManager and SSH are always ready immediately after a system boots, reducing downtime and improving service availability. This guide has covered the basic steps and provided practical examples to help you manage network services effectively.