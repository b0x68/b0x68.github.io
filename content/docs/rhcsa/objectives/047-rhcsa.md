# Tech Tutorial: Manage Basic Networking

## Introduction

In this tutorial, we will delve into how to restrict network access using `firewalld`, a dynamic daemon to manage firewall with support for networks zones. `firewalld` uses `firewall-cmd` as its command-line interface. The ability to restrict network access on servers is crucial for protecting resources and managing which services are exposed to the public internet or internal networks.

Understanding how to configure and manage firewalls is a key skill for any system administrator or anyone looking to secure their network-enabled Linux systems. By the end of this tutorial, you will have a solid understanding of how to use `firewall-cmd` to manage `firewalld` and set up basic firewall rules to control network traffic.

## Prerequisites

- A Linux system with `firewalld` installed.
- Sudo or root access on the system.

## Step-by-Step Guide

### Step 1: Checking the Status of `firewalld`

Before making any changes, it's important to check whether `firewalld` is running on your system. You can do this with the following command:

```bash
sudo firewall-cmd --state
```

If `firewalld` is not running, you can start it with:

```bash
sudo systemctl start firewalld
```

And enable it at boot with:

```bash
sudo systemctl enable firewalld
```

### Step 2: Understanding Zones

`firewalld` organizes rules into zones, which are groups of rules specifying what traffic should be allowed depending on the level of trust you have in the networks your computer is connected to. To list all available zones, use:

```bash
sudo firewall-cmd --get-zones
```

To find out which zone is currently active, you can use:

```bash
sudo firewall-cmd --get-active-zones
```

### Step 3: Adding and Removing Services

To allow specific services through the firewall, `firewalld` uses the concept of services, which are predefined rules that apply to particular ports and protocols. To list all available services, use:

```bash
sudo firewall-cmd --get-services
```

To allow a service, such as HTTP, use the following command:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

To reload `firewalld` and apply the changes, use:

```bash
sudo firewall-cmd --reload
```

To remove a service, simply replace `--add-service` with `--remove-service`:

```bash
sudo firewall-cmd --zone=public --remove-service=http --permanent
```

### Step 4: Adding Custom Ports

If you need to allow traffic on a specific port, you can add a custom rule. For example, to allow TCP traffic on port 8080, use:

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
```

And again, don't forget to reload the firewall:

```bash
sudo firewall-cmd --reload
```

### Step 5: Blocking and Unblocking IPs

To block a specific IP address:

```bash
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.100" reject' --permanent
```

To unblock the IP, remove the rule:

```bash
sudo firewall-cmd --zone=public --remove-rich-rule='rule family="ipv4" source address="192.168.1.100" reject' --permanent
```

## Conclusion

In this tutorial, you have learned how to manage network access using `firewalld` and `firewall-cmd`. We covered how to check the status of the firewall, understand and use zones, add and remove services, manage custom ports, and block IP addresses. These skills are fundamental for securing a network and should be tailored according to the specific needs of your environment. Remember that maintaining a secure network is an ongoing process that involves regular reviews and updates to the firewall rules as the network environment and security landscapes evolve.