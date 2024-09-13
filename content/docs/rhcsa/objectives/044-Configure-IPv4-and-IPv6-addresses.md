# Tech Tutorial: Manage Basic Networking

## Introduction

This tutorial is designed for individuals preparing for the Red Hat Certified System Administrator (RHCSA) exam, specifically focusing on the objective to configure IPv4 and IPv6 addresses. Efficient network management is crucial for system administrators, and understanding how to configure IP addresses is a fundamental skill. This guide will provide detailed instructions and examples using Red Hat Enterprise Linux (RHEL) commands and utilities.

## Step-by-Step Guide

### **Prerequisites**

- A system running RHEL 8 or later.
- Proper permissions (typically root access) to modify network configurations.

### **Understanding Network Configuration Files**

In RHEL, network settings are primarily managed through configuration files located in `/etc/sysconfig/network-scripts/`. For each network interface, there is a corresponding file named `ifcfg-<interface_name>`. 

### **1. Configuring IPv4 Address**

#### **Locating the Interface Configuration File**

First, determine the network interfaces available on your system with the `nmcli` command:

```bash
nmcli device status
```

Look for the `DEVICE` name that corresponds to the interface you want to configure, typically something like `ens33` or `eth0`.

#### **Editing the Interface Configuration File**

Using the `vi` editor, open the interface configuration file:

```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
```

Here is an example configuration for setting a static IPv4 address:

```plaintext
TYPE=Ethernet
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
NAME=ens33
UUID=your-uuid-here
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.100
PREFIX=24
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

In this file:
- `BOOTPROTO=none` disables DHCP.
- `IPADDR`, `PREFIX`, and `GATEWAY` set the static IP address, network mask, and gateway.
- `DNS1` defines the DNS server IP.

Save and exit the editor.

#### **Restarting the Network Service**

Apply the changes by restarting the network service:

```bash
sudo systemctl restart NetworkManager
```

### **2. Configuring IPv6 Address**

Configuring an IPv6 address is similar to IPv4 but with different parameters in the same configuration file.

#### **Editing the Interface Configuration File for IPv6**

Open the same configuration file:

```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
```

Add or modify the following lines to set a static IPv6 address:

```plaintext
IPV6INIT=yes
IPV6ADDR=2001:0db8:85a3:0000:0000:8a2e:0370:7334/64
IPV6_DEFAULTGW=fe80::1
```

- `IPV6ADDR` sets the static IPv6 address and prefix.
- `IPV6_DEFAULTGW` sets the default gateway for IPv6.

Save and close the file.

#### **Restarting the Network Service**

Restart the network service to apply the IPv6 configuration:

```bash
sudo systemctl restart NetworkManager
```

### **Verifying the Configuration**

After configuring the network, verify the settings with:

```bash
ip addr show ens33
```

This command shows both IPv4 and IPv6 addresses assigned to the interface `ens33`.

## Detailed Code Examples

Here are some additional commands that are useful for managing network configurations in RHEL:

- To view all network interface configurations:
  ```bash
  nmcli con show
  ```

- To bring an interface up or down:
  ```bash
  sudo nmcli con up ens33
  sudo nmcli con down ens33
  ```

- To add a new DNS server:
  ```bash
  sudo nmcli con mod ens33 +ipv4.dns 8.8.4.4
  ```

## Conclusion

Configuring IPv4 and IPv6 addresses in RHEL involves understanding and modifying interface configuration files and using system commands to apply and verify the settings. Mastery of these tasks is essential for any system administrator working in a Red Hat environment. Remember to always back up configuration files before making changes, and verify network functionality after applying new settings. This ensures reliable and predictable network operations.