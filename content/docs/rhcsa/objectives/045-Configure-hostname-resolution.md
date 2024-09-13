# Tech Tutorial: Manage Basic Networking - Configure Hostname Resolution

## Introduction

The ability to configure hostname resolution is a fundamental skill for any systems administrator, especially for those preparing for the Red Hat Certified System Administrator (RHCSA) exam. Proper configuration of hostname resolution ensures that your systems can locate and communicate with other computers and services on a network. This tutorial focuses exclusively on Red Hat Enterprise Linux (RHEL), providing the necessary steps and commands to configure hostname resolution effectively.

## Step-by-Step Guide

### 1. Understanding Hostname Resolution

Hostname resolution is the process of mapping hostnames to IP addresses. This is typically handled in two ways on a Linux system:
- **Static resolution**: Using the `/etc/hosts` file.
- **Dynamic resolution**: Using DNS (Domain Name System).

### 2. Configuring the `/etc/hosts` File

The `/etc/hosts` file is one of the first resources consulted during hostname resolution. It contains static mappings of IP addresses to hostnames. This method is quick and does not rely on network availability, making it ideal for small networks or for providing overrides of DNS data.

#### Viewing the Current Hosts File
To view the current entries in your `/etc/hosts` file, use the `cat` command:

```bash
cat /etc/hosts
```

#### Editing the Hosts File
To add or modify entries, you'll need to edit this file using a text editor like `vi`:

```bash
sudo vi /etc/hosts
```

Add entries in the following format:

```
<IP-address> <hostname> <alias(optional)>
```

For example:

```
192.168.1.10    server1.example.com    server1
```

Save and exit the editor (`:wq` in `vi`).

### 3. Using DNS for Hostname Resolution

DNS provides dynamic hostname resolution and is configured by specifying DNS servers and search domains in the network configuration.

#### Configuring DNS Servers
To configure DNS servers on RHEL, you will typically edit the network configuration file for your connection. For systems using NetworkManager, this is often managed via the `nmcli` tool.

##### Listing Available Connections

```bash
nmcli con show
```

##### Modifying a Connection to Use Specific DNS Servers

```bash
sudo nmcli con mod "System eth0" ipv4.dns "8.8.8.8 8.8.4.4"
sudo nmcli con up "System eth0"  # Restart the connection to apply changes
```

Replace `"System eth0"` with your connection name and `"8.8.8.8 8.8.4.4"` with your preferred DNS servers.

#### Setting the Search Domain

The search domain is used to qualify short hostnames into fully qualified domain names (FQDNs).

```bash
sudo nmcli con mod "System eth0" ipv4.dns-search "example.com"
sudo nmcli con up "System eth0"  # Restart the connection to apply changes
```

### 4. Verifying Configuration

After configuring hostname resolution, it's important to verify that your settings are working correctly.

#### Testing with `ping`

Use `ping` to check if the hostname resolves and responds:

```bash
ping server1.example.com
```

#### Checking Resolution Mechanism

The `getent` command can be used to see how a hostname is resolved, whether via `/etc/hosts` or DNS:

```bash
getent hosts server1.example.com
```

## Conclusion

Properly configuring hostname resolution is essential for ensuring reliable network communication within your RHEL systems. By understanding and managing both static entries in the `/etc/hosts` file and dynamic DNS settings, you can maintain robust and flexible network configurations. Always remember to verify your settings to avoid any connectivity issues. This knowledge not only prepares you for the RHCSA exam but also equips you with practical skills essential for any Linux systems administrator.