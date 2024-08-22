# Tech Tutorial: Manage Security with firewalld

## Introduction

In the realm of Linux system administration, managing security settings is crucial to protect data and resources. `firewalld` is a dynamic firewall management tool that more and more Linux distributions are adopting due to its flexibility and support for network/firewall zones. It uses `firewall-cmd` as its command-line utility to manage the firewall rules. In this tutorial, we will delve into how to configure firewall settings using `firewall-cmd`/`firewalld`.

## What is firewalld?

`firewalld` provides a dynamically managed firewall with support for network/firewall zones to define the trust level of network connections or interfaces. It has support for IPv4, IPv6 firewall settings, and for ethernet bridges and has a separation of runtime and permanent configuration options. Changes can be done immediately in the runtime environment and can be made permanent if needed.

## Step-by-Step Guide

### Step 1: Installing firewalld

If `firewalld` is not already installed on your system, you can install it using your distribution's package manager. For Red Hat-based systems like CentOS or Fedora, you can use:

```bash
sudo yum install firewalld
```

For Debian-based systems like Ubuntu, use:

```bash
sudo apt install firewalld
```

### Step 2: Starting and Enabling firewalld

To start the `firewalld` service and enable it to start at boot, use:

```bash
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

To check the status of the service:

```bash
sudo systemctl status firewalld
```

### Step 3: Getting to Know firewall-cmd

`firewall-cmd` is the front-end tool for managing `firewalld`. To get started, first check the default zone. The default zone determines the behavior of how incoming connections are handled when no specific zone is set.

```bash
firewall-cmd --get-default-zone
```

### Step 4: Managing Zones

Firewall zones are predefined sets of rules that dictate what traffic should be allowed depending on the level of trust you have in the networks your computer is connected to. To list all available zones, use:

```bash
firewall-cmd --get-zones
```

To see which zones are actively being used:

```bash
firewall-cmd --get-active-zones
```

### Step 5: Adding Services to a Zone

For instance, if you want to allow HTTP and HTTPS traffic, you need to add services to your active zone. You can permanently add the `http` and `https` services to the default zone by:

```bash
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
```

Then reload `firewalld` to apply the changes:

```bash
firewall-cmd --reload
```

### Step 6: Opening Ports

If you need to open a specific port, say TCP port 9090:

```bash
firewall-cmd --zone=public --add-port=9090/tcp --permanent
```

And reload the firewall settings:

```bash
firewall-cmd --reload
```

### Step 7: Removing Services or Ports

To remove a service or a port from a zone:

```bash
firewall-cmd --zone=public --remove-service=http --permanent
firewall-cmd --zone=public --remove-port=9090/tcp --permanent
```

Don't forget to reload the configuration after making changes:

```bash
firewall-cmd --reload
```

## Conclusion

`firewalld` offers a robust and flexible framework for managing firewall rules in a Linux environment. By using `firewall-cmd`, system administrators can easily configure and apply firewall rules based on zones, enhancing the security layers of the system. Remember to test firewall settings in a controlled environment before applying them in a production scenario to ensure they work as expected. With `firewalld`, you can maintain a strong security posture with the ability to adapt as your network environment changes.