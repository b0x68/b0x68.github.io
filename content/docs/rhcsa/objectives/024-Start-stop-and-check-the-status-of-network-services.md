# Tech Tutorial: Operate Running Systems

## Introduction

In this tutorial, we will learn how to manage network services on a Linux system. This is a fundamental skill for system administrators, as services are the backbone of a network’s functionality. We will focus on starting, stopping, and checking the status of these services. Understanding these operations is crucial for maintaining the health and performance of a server.

We will use `systemd`, a system and service manager for Linux, which has become the standard for newer distributions. It replaces older init systems like SysVinit and Upstart. Commands like `systemctl` and `service` are at the core of service management in Linux.

## Prerequisites

- A Linux system with `systemd` installed (Most modern Linux distributions like CentOS 7/8, Ubuntu 16.04 and newer, Debian 8 and newer)
- Access to a terminal or command line
- Sudo or root access

## Step-by-Step Guide

### 1. Checking the Status of Services

To manage services, it's essential first to understand how to check their status. This information tells you if a service is running, stopped, or in a failed state.

#### Using `systemctl`

```bash
sudo systemctl status nginx
```

Replace `nginx` with the name of the service you want to check. This command provides a detailed output that includes the service's status (active, inactive, failed), configuration, and recent log entries.

#### Output Example

```plaintext
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2023-03-21 15:00:00 UTC; 10min ago
 Main PID: 1234 (nginx)
    Tasks: 2 (limit: 4915)
   Memory: 1.8M
   CGroup: /system.slice/nginx.service
           ├─1234 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─1235 nginx: worker process
```

### 2. Starting a Service

To start a service which is not currently running:

```bash
sudo systemctl start nginx
```

Again, replace `nginx` with the desired service. This command will initiate the service without any output. To confirm the service has started, use the status command covered earlier.

### 3. Stopping a Service

If you need to stop a running service, use:

```bash
sudo systemctl stop nginx
```

This command halts the chosen service. It's crucial in scenarios where you need to perform maintenance or update configurations that cannot be done while the service is running.

### 4. Enabling and Disabling Services

Enabling a service configures it to start automatically at boot:

```bash
sudo systemctl enable nginx
```

Disabling the service does the opposite:

```bash
sudo systemctl disable nginx
```

These commands are useful for setting up services that should always be available, like database servers, or disabling services that are not needed to conserve system resources.

## Detailed Code Examples

Let's consider a real-world scenario: managing an Apache HTTP Server on a Ubuntu system.

### Checking Apache's Status

```bash
sudo systemctl status apache2
```

### Starting Apache Server

```bash
sudo systemctl start apache2
```

### Stopping Apache Server

```bash
sudo systemctl stop apache2
```

### Enabling Apache to Start at Boot

```bash
sudo systemctl enable apache2
```

### Disabling Apache from Starting at Boot

```bash
sudo systemctl disable apache2
```

## Conclusion

Mastering the start, stop, and status check of network services using `systemctl` is essential for system administration. These commands help ensure that your services are running as expected and are properly managed across reboots and maintenance windows. With `systemd`, these tasks are standardized across different Linux distributions, simplifying the management of services on any system. Equip yourself with these skills to enhance your capabilities as a proficient Linux administrator.