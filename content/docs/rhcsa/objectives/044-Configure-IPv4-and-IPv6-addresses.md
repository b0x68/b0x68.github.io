# Tech Tutorial: Manage Basic Networking

## Introduction

In today's interconnected world, understanding how to configure IPv4 and IPv6 addresses on network devices is a crucial skill for any network administrator or IT professional. This tutorial will guide you through the basics of configuring IPv4 and IPv6 addresses, providing you with the necessary knowledge to manage network interfaces effectively. We will cover practical scenarios, and provide step-by-step instructions along with detailed code examples.

## What are IPv4 and IPv6?

- **IPv4 (Internet Protocol version 4)** is the fourth version of the Internet Protocol (IP). It is one of the core protocols of standards-based internetworking methods on the Internet and was the first version deployed for production in the ARPANET in 1983. It still routes most Internet traffic today, despite the ongoing deployment of a successor protocol, IPv6.
- **IPv6 (Internet Protocol version 6)** was developed to deal with the long-anticipated problem of IPv4 address exhaustion. It is intended to replace IPv4, providing an identification and location system for computers on networks and routing traffic across the Internet.

## Step-by-Step Guide

### 1. Configuring IPv4 Addresses

IPv4 addresses are 32-bit numbers that are typically displayed in dotted-decimal notation. A typical IPv4 address looks like `192.168.1.1`. Here’s how you can assign an IPv4 address to a network interface in various operating systems.

#### Windows

1. Open Command Prompt as Administrator.
2. Use the `netsh` command to set the IP address. Replace `Ethernet0` with your network interface name, and use your desired IP address and subnet mask:

```shell
netsh interface ip set address name="Ethernet0" static 192.168.1.100 255.255.255.0
```

#### Linux

1. Open Terminal.
2. Use the `ifconfig` or `ip` command. Here’s an example with `ip`:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

Ensure you replace `eth0` with your network interface name.

### 2. Configuring IPv6 Addresses

IPv6 addresses are 128-bit hexadecimal numbers and are separated by colons. An example of an IPv6 address is `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

#### Windows

1. Open Command Prompt as Administrator.
2. Use the `netsh` command to add an IPv6 address:

```shell
netsh interface ipv6 add address interface="Ethernet0" address=2001:db8::c001:1/64
```

#### Linux

1. Open Terminal.
2. Use the `ip` command to add an IPv6 address:

```bash
sudo ip -6 addr add 2001:db8::c001:1/64 dev eth0
```

Replace `eth0` with your network interface name.

## Detailed Code Examples

Let’s consider a scenario where we need to configure a static IP address for a server and then verify the network configuration.

### Example: Configuring a Static IP on a Linux Server

1. Set the IP address:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

2. Set the default gateway:

```bash
sudo ip route add default via 192.168.1.1
```

3. Verify the configuration:

```bash
ip addr show eth0
ip route show
```

### Conclusion

Configuring IPv4 and IPv6 addresses is a fundamental skill for managing and maintaining a reliable network. Whether you are setting up a small home network or managing enterprise infrastructure, understanding these configurations helps ensure proper network connectivity and security. This tutorial provided you with the basics of configuring static IP addresses across different operating systems, which should serve as a solid foundation for more advanced networking tasks.