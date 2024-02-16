+++
title = "Configure IPv4 and IPv6 addresses"
date = "2024-02-16T11:51:12-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Introduction to Configuring IPv4 and IPv6 Addresses

In today's world, communication between devices over a network is essential for smooth functioning of various systems. The Internet Protocol (IP) is the backbone of this communication, and every device on a network requires a unique IP address to identify and communicate with each other.

A Red Hat Certified Systems Administrator (RHCSA) must have a thorough understanding of configuring both IPv4 and IPv6 addresses, as it is one of the critical objectives of the RHCSA Exam 200. In this tutorial, we will cover the basics of IPv4 and IPv6 addresses, and walk you through the steps to configure them on a Red Hat Enterprise Linux system.

## Understanding IPv4 and IPv6 Addresses

IPv4 is the most commonly used IP version and uses a 32-bit address scheme, which allows for approximately 4.3 billion unique addresses. While this may seem like a large number, it is not enough to accommodate the growing number of network devices, leading to the development of IPv6. IPv6 uses a 128-bit address scheme, allowing for trillions of unique addresses, thus ensuring the continuous growth of network devices.

However, the basic structure and format of both IPv4 and IPv6 addresses are similar. An IPv4 address is a string of four numbers separated by periods, while an IPv6 address is a combination of hexadecimal values and colons. An example of an IPv4 address is 192.168.1.1, and an IPv6 address is 2001:cdba:0000:0000:0000:0000:3257:9652.

Before we dive into the steps of configuring IPv4 and IPv6 addresses, we must understand some core concepts:

- **Network Address** - The first address in a network address range that identifies the network itself.
- **Host Address** - The last address in a network address range that identifies a specific network device.
- **Subnet Mask** - A 32-bit number used to divide an IP address into network and host addresses.
- **Default Gateway** - A network device that serves as a gateway for data to be sent to other networks.
- **DNS Server** - A network device that maintains a database of domain names and their corresponding IP addresses, enabling domain name resolution.

## Configuring IPv4 and IPv6 Addresses on a Red Hat Enterprise Linux System

To configure IPv4 and IPv6 addresses on a Red Hat Enterprise Linux system, follow the steps outlined below:

### Step 1: Identify Network Interfaces

The first step is to identify the network interfaces on your system. Network interfaces are used to connect a device to a network. To view the network interfaces, use the command `ip a`.

```
$ ip a
```

This command will display a list of all the network interfaces on your system, along with their IP addresses and other details. Note down the names of the interfaces you wish to configure.

### Step 2: Configure IPv4 Address

To configure an IPv4 address, we will use the `nmcli` command-line tool, which manages the NetworkManager services. Follow the steps below to configure an IPv4 address:

1. Use the `nmcli` command with the `con show` option to view the available connections.

```
$ nmcli con show
```

2. Identify the connection you wish to configure and make a note of its UUID.
3. Use the `nmcli` command with the `con mod` option to modify the connection. You will need to specify the name or UUID of the connection, the configuration option to modify, and the new value. For example, to set the IPv4 address of the eth0 interface to 192.168.1.100 with a subnet mask of 255.255.255.0, use the following command:

```
$ nmcli con mod eth0 ipv4.addresses 192.168.1.100/24
```

4. Finally, activate the connection with the `up` option.

```
$ nmcli con up eth0
```

### Step 3: Configure IPv6 Address

To configure an IPv6 address, follow the same steps as for configuring an IPv4 address, but use the `ipv6` option instead. For example, to set the IPv6 address of the eth0 interface to 2001:cdba:0000:0000:0000:0000:3257:9652 with a subnet mask of 64, use the following command:

```
$ nmcli con mod eth0 ipv6.addresses 2001:cdba:0000:0000:0000:0000:3257:9652/64
```

### Step 4: Configure Default Gateway

To configure a default gateway, use the `nmcli` command with the `con mod` option, and specify the default gateway IP address using the `ipv4.gateway` option. For example, to set the default gateway to 192.168.1.1, use the following command:

```
$ nmcli con mod eth0 ipv4.gateway 192.168.1.1
```

Note that you can configure multiple default gateways by adding additional IP addresses separated by a comma.

### Step 5: Configure DNS Server

To configure a DNS server, use the `nmcli` command with the `con mod` option, and specify the DNS server IP address using the `ipv4.dns` option. For example, to set the DNS server to 8.8.8.8, use the following command:

```
$ nmcli con mod eth0 ipv4.dns 8.8.8.8
```

Note that you can configure multiple DNS servers by adding additional IP addresses separated by a comma.

### Step 6: Verify Configuration

To verify the configuration, use the `nmcli` command with the `con show` option again. It should display the updated values for the corresponding connection.

```
$ nmcli con show
```

Additionally, you can also use the `ip a` command to check the IP addresses of the configured interfaces.

```
$ ip a
```

## Conclusion

In this tutorial, we covered the basics of IPv4 and IPv6 addresses and walked through the steps to configure them on a Red Hat Enterprise Linux system. As a RHCSA, it is crucial to have a thorough understanding of this topic to ensure efficient communication between devices on a network. By following the steps outlined in this tutorial, you will be well-equipped to configure IPv4 and IPv6 addresses on your system. Good luck on your RHCSA 200 exam!