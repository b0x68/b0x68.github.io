# Tech Tutorial: Manage Basic Networking - Restrict Network Access Using `firewall-cmd`

## Introduction

In this tutorial, we will focus on how to manage and restrict network access on a Red Hat Enterprise Linux (RHEL) system using `firewall-cmd`, the command-line interface for managing firewalld. Firewalld is the default firewall management tool in RHEL and offers a dynamic way to manage the network firewall with support for network/firewall zones that define the trust level of network connections or interfaces.

Understanding how to configure and manage firewalld using `firewall-cmd` is crucial for network security and is a key objective for the Red Hat Certified Systems Administrator (RHCSA) exam.

## Step-by-Step Guide

### Step 1: Checking the Status of firewalld

Before making any changes, it's important to check whether the firewalld service is running on your system. You can do this with the following command:

```bash
sudo systemctl status firewalld
```

If it's not running, you can start it with:

```bash
sudo systemctl start firewalld
```

### Step 2: Understanding Zones

Firewalld uses zones to define the trust level of network connections. To list all available zones and see which one is active, use:

```bash
firewall-cmd --get-active-zones
```

This will show you the zones and the interfaces that are associated with each zone.

### Step 3: Adding/Modifying Rules

To restrict network access, you can add rules to the zones. For instance, if you want to block all incoming HTTP traffic (port 80), you can add a rule to the public zone like this:

```bash
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" port port=80 protocol=tcp reject' --permanent
```

The `--permanent` flag saves the rule across reboots. You must reload the firewall for changes to take effect:

```bash
sudo firewall-cmd --reload
```

### Step 4: Removing Rules

If you need to remove a rule, you can do so by replacing `--add-port` with `--remove-port`:

```bash
sudo firewall-cmd --zone=public --remove-port=80/tcp --permanent
sudo firewall-cmd --reload
```

### Step 5: Checking Rules

To verify that your rules have been added or removed correctly, you can list all rules for a zone:

```bash
sudo firewall-cmd --zone=public --list-all
```

## Detailed Code Examples

Let's say you want to restrict SSH access (port 22) to your server from a specific IP address, e.g., `192.168.1.105`. Here's how you can achieve that:

1. **Adding a rule to allow SSH only from a specific IP:**

    ```bash
    sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.105" port port=22 protocol=tcp accept' --permanent
    sudo firewall-cmd --reload
    ```

2. **Blocking SSH from all other IPs:**

    ```bash
    sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" invert="true" port port=22 protocol=tcp reject' --permanent
    sudo firewall-cmd --reload
    ```

## Conclusion

Managing network access using `firewall-cmd` in RHEL is a powerful way to enhance your system's security. By understanding zones and how to add, modify, or remove rules, you can effectively control who can access your system and on what terms. This tutorial covers the essentials to get you started with `firewall-cmd` for the RHCSA exam, but practicing these commands and exploring further will help solidify your understanding and skills in managing RHEL's firewall.

Remember, always double-check your firewall rules to ensure they're working as expected and not inadvertently blocking legitimate traffic or leaving your system exposed.