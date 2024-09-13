# Tech Tutorial: Manage Basic Networking

## Introduction

In this tutorial, we will focus on configuring network services to start automatically at boot on a Red Hat Enterprise Linux (RHEL) system. This is a crucial skill for system administrators, particularly for those preparing for the Red Hat Certified System Administrator (RHCSA) exam. Ensuring that network services start automatically enhances the reliability and availability of network-dependent applications and services.

## Step-by-Step Guide

### Step 1: Understanding Systemd

RHEL uses `systemd` as its init system, which manages the boot process and system services. Systemd introduces the concept of "units" to manage different resources. Services are one type of unit, handled by service files (with the `.service` extension).

### Step 2: Identify the Service

Before you enable a service to start at boot, you need to know its exact service name. You can list all services to find the one you're interested in:

```bash
systemctl list-units --type=service --all
```

For our tutorial, let's assume we want to enable the `NetworkManager` service, which is crucial for managing network connections.

### Step 3: Check the Current Status of the Service

To check whether the `NetworkManager` service is currently active and enabled, use:

```bash
systemctl status NetworkManager
```

This command provides detailed information about the service, including its current status, whether it's enabled, and recent log entries.

### Step 4: Enable the Service to Start at Boot

To ensure the `NetworkManager` service starts automatically at boot, use the following command:

```bash
sudo systemctl enable NetworkManager
```

This command creates a symbolic link from the system's `systemd` service directories to the `NetworkManager.service` file, which tells `systemd` to start this service at boot time.

### Step 5: Verify the Service is Enabled

After enabling the service, it's a good practice to check if it's correctly set to start at boot:

```bash
systemctl is-enabled NetworkManager
```

This command will return `enabled` if the service is set to start at boot successfully.

### Step 6: Reboot and Check

To fully verify that everything is set up correctly, reboot the system:

```bash
sudo reboot
```

After the system restarts, check the status of the `NetworkManager` service again to ensure it's active:

```bash
systemctl status NetworkManager
```

## Detailed Code Examples

Here’s a detailed breakdown of the commands used in this tutorial:

1. **Listing Services**:
   ```bash
   systemctl list-units --type=service --all
   ```
   Use this command to explore all services available on your system, both active and inactive.

2. **Checking Service Status**:
   ```bash
   systemctl status NetworkManager
   ```
   This command is used to inspect the current state of the `NetworkManager` service.

3. **Enabling a Service**:
   ```bash
   sudo systemctl enable NetworkManager
   ```
   This command sets the `NetworkManager` service to start automatically at boot.

4. **Checking if a Service is Enabled**:
   ```bash
   systemctl is-enabled NetworkManager
   ```
   This outputs the enable status of the `NetworkManager` service.

5. **Rebooting the System**:
   ```bash
   sudo reboot
   ```
   Reboots the system, which is useful for testing that changes persist after a restart.

## Conclusion

In this tutorial, we've covered how to configure network services to start automatically at boot on a Red Hat Enterprise Linux system, using `NetworkManager` as an example. This skill is essential for system administrators to ensure that network configurations are automatically applied and maintained across system reboots, thereby improving system reliability and network availability. By mastering these commands and understanding the principles behind `systemd`, you will enhance your capabilities as a Linux system administrator and be better prepared for the RHCSA exam.