# Tech Tutorial: Manage Basic Networking with `firewall-cmd`/`firewalld`

## Introduction

In the realm of system administration, network security is paramount. One of the most effective tools to manage network security on Linux systems is `firewalld`, which interfaces with the system's kernel through `iptables`. `firewalld` uses the command-line tool `firewall-cmd` for its management. This tutorial will delve into how to use `firewall-cmd` to restrict network access, ensuring your systems are safeguarded against unauthorized access.

## What is `firewalld`?

`firewalld` is a firewall management tool available by default in many Linux distributions like Fedora, CentOS, and Red Hat Enterprise Linux. It provides a dynamically managed firewall with support for network/firewall zones to define the trust level of network connections or interfaces. It uses concepts of zones and services, which simplifies the process of managing your firewall rules.

## Prerequisites

- A Linux system with `firewalld` installed.
- Sudo or root access on the system.
- Basic understanding of network concepts such as IP addresses, ports, and protocols (TCP/UDP).

## Step-by-Step Guide

### Step 1: Checking the Status of `firewalld`

Before making any changes, it's essential to ensure that `firewalld` is running on your system. Use the following command to check the status:

```bash
sudo firewall-cmd --state
```

If it's not running, you can start it with:

```bash
sudo systemctl start firewalld
```

And to enable it at boot:

```bash
sudo systemctl enable firewalld
```

### Step 2: Understanding Zones

`firewalld` uses zones to categorize traffic based on the level of trust. Common zones include:
- **public**: For untrusted public areas
- **home**: For home networks
- **internal**: For internal networks
- **dmz**: For demilitarized zones

You can list all available zones and their settings with:

```bash
sudo firewall-cmd --list-all-zones
```

To find out which zone is active, use:

```bash
sudo firewall-cmd --get-active-zones
```

### Step 3: Adding and Removing Services

Services are predefined rules that apply to certain common applications. For example, if you want to allow HTTP traffic, you can enable the HTTP service. Here’s how to add the HTTP service to the public zone:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

To reload `firewalld` and apply changes:

```bash
sudo firewall-cmd --reload
```

To remove a service, use:

```bash
sudo firewall-cmd --zone=public --remove-service=http --permanent
```

### Step 4: Working with Ports

If a service is not predefined, you can manually open or close ports. For instance, to allow traffic on port 8080:

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
```

To remove the port:

```bash
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent
```

### Step 5: Rich Rules

For more complex scenarios, `firewalld` supports rich rules that allow more detailed firewall rules. For example, to allow access from a specific IP address to a certain port:

```bash
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port port="8080" protocol="tcp" accept' --permanent
```

## Conclusion

Managing network access on a Linux system using `firewalld` and `firewall-cmd` is a robust and flexible way to enhance your system's security. By understanding and utilizing zones, services, ports, and rich rules, you can tailor your firewall to meet the unique needs of your environment. Regularly updating and auditing your firewall rules is crucial in maintaining a secure and functional network. This tutorial should serve as a foundation for managing basic network security through `firewalld`.