# Tech Tutorial: Manage Basic Networking

## Introduction

In the realm of system administration, ensuring the reliability and availability of network services is crucial. One fundamental aspect of this is configuring network services to start automatically at boot. This capability ensures that critical network functionalities such as DHCP, DNS, or even custom application services are always up and running immediately after the system starts, without manual intervention. This tutorial will guide you through the steps to configure network services to start automatically on Linux systems using `systemd`, which has become the standard for system and service manager in most Linux distributions.

## Step-by-Step Guide

### Prerequisites

Before we start, ensure you have:
- A Linux system with `systemd` installed (most modern Linux distributions like Ubuntu, CentOS, Fedora, etc., come with `systemd`).
- Sudo or root access to the system to make changes to service configurations.

### 1. Checking the Status of a Service

Before enabling a service to start at boot, you first need to know its status and whether it is currently active, inactive, or enabled. Use the `systemctl` command to check the status:

```bash
sudo systemctl status network.service
```

Replace `network.service` with the name of the service you are interested in. This command will tell you whether the service is active and enabled.

### 2. Enabling a Service

To configure a service to start automatically at boot, use the `enable` command:

```bash
sudo systemctl enable network.service
```

This command creates a symbolic link from the service's scripts in `/etc/systemd/system/` to the appropriate directories under `/etc/systemd/system/*.wants/`. This action tells `systemd` to start the service during the boot process.

### 3. Starting a Service Immediately

If the service is not currently running and you want to start it without rebooting the system, use:

```bash
sudo systemctl start network.service
```

This command will start the service immediately.

### 4. Checking Changes

Verify that the service is set to start at boot:

```bash
sudo systemctl is-enabled network.service
```

This command should output `enabled`, indicating that the service is configured to start at boot.

### 5. Rebooting to Test

To fully test that your service starts automatically at boot:

```bash
sudo reboot
```

After rebooting, log in and check the status of the service again:

```bash
sudo systemctl status network.service
```

This should show that the service is active and running.

## Detailed Code Examples

Let’s consider a real-world example where you are managing a DHCP server on a network. The DHCP service is critical as it assigns IP addresses to devices on the network.

1. **Check the status of the DHCP server**:

    ```bash
    sudo systemctl status isc-dhcp-server
    ```

2. **Enable the DHCP server to start at boot**:

    ```bash
    sudo systemctl enable isc-dhcp-server
    ```

3. **Start the DHCP server immediately if it's not already running**:

    ```bash
    sudo systemctl start isc-dhcp-server
    ```

4. **Verify that the DHCP server is enabled**:

    ```bash
    sudo systemctl is-enabled isc-dhcp-server
    ```

5. **Reboot and check the service status post-boot**:

    ```bash
    sudo reboot
    # After reboot
    sudo systemctl status isc-dhcp-server
    ```

## Conclusion

Configuring network services to start automatically at boot is a best practice for maintaining the reliability and availability of network-dependent services and applications. Using `systemd` to manage these services ensures that they are managed consistently and efficiently. This tutorial has walked you through enabling and managing these services on a Linux system, ensuring that your network services are always ready when your system boots up. This skill is essential for any system administrator or IT professional managing Linux servers or workstations.