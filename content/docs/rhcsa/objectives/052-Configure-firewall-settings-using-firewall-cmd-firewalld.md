# Tech Tutorial: Manage Security with firewalld on RHEL

## Introduction

In this tutorial, we will cover how to manage firewall settings using `firewall-cmd`, the command-line interface for `firewalld`, which is the default firewall management tool on Red Hat Enterprise Linux (RHEL). Understanding and configuring firewall settings is a critical skill for system administrators to ensure the security and proper networking of Linux systems.

`firewalld` provides a dynamically managed firewall with support for network/firewall zones to define the trust level of network connections or interfaces. It uses the concepts of zones and services, which simplifies the management of firewall rules.

## Step-by-Step Guide

### Prerequisites

- A RHEL system (version 7 or later)
- Sudo or root access on the system

### Step 1: Checking the Status of firewalld

Before making any changes, it's important to check whether the `firewalld` service is running. Use the following command:

```bash
sudo firewall-cmd --state
```

If `firewalld` is not running, you can start it with:

```bash
sudo systemctl start firewalld
```

To enable `firewalld` to start at boot:

```bash
sudo systemctl enable firewalld
```

### Step 2: Understanding Zones

Firewalld uses zones to manage different levels of trust for network connections. To list all available zones and see which one is active, use:

```bash
sudo firewall-cmd --get-active-zones
```

This will show you the active zones and the interfaces that are part of these zones.

### Step 3: Adding and Removing Services

To allow specific services through the firewall, you first need to understand what services are currently allowed by your active zone. To list all services that are allowed:

```bash
sudo firewall-cmd --list-services --zone=public
```

To add a service to the zone, use:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

This command allows HTTP traffic in the public zone. The `--permanent` flag saves the change across system reboots.

To remove a service:

```bash
sudo firewall-cmd --zone=public --remove-service=http --permanent
```

### Step 4: Managing Ports

If a specific application uses custom ports, you can open these ports in the firewall:

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
```

This command opens TCP port 8080. To close the port again:

```bash
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent
```

### Step 5: Applying Changes

After making changes with the `--permanent` flag, you must reload `firewalld` to apply them:

```bash
sudo firewall-cmd --reload
```

### Step 6: Rich Rules

For more complex rules, `firewalld` supports "rich rules" which allow more detailed control. For example, to allow connections from a specific IP address to a particular service:

```bash
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.0.101" service name="http" accept' --permanent
```

## Detailed Code Examples

Let's consider a scenario where you need to configure a web server with both HTTP and HTTPS services, allowing access only from a specific network.

1. **Add HTTP and HTTPS services**:

    ```bash
    sudo firewall-cmd --zone=public --add-service=http --permanent
    sudo firewall-cmd --zone=public --add-service=https --permanent
    ```

2. **Allow access from a specific network**:

    ```bash
    sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.0.0/24" accept' --permanent
    ```

3. **Reload to apply changes**:

    ```bash
    sudo firewall-cmd --reload
    ```

## Conclusion

In this tutorial, we have explored how to manage firewall settings using `firewall-cmd` in RHEL. We've covered checking the status of `firewalld`, managing zones, services, ports, and using rich rules for more complex scenarios. Proper management of firewall settings is crucial for securing your systems and ensuring that only authorized traffic is allowed. By mastering these commands, you will enhance your system's security and meet critical administrative requirements.