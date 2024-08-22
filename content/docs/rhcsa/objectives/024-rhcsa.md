# Tech Tutorial: Operate Running Systems

## Introduction

In the world of network administration, knowing how to manage services is crucial. Services, often referred to as daemons on Unix-like systems, are background processes that handle tasks such as web serving, file sharing, and data management. In this tutorial, we will cover how to start, stop, and check the status of network services on a Linux system using `systemctl`, a command-line tool for controlling the systemd system and service manager.

## Step-by-Step Guide

### Prerequisites

Before proceeding, ensure you have:
- A Linux system with systemd installed (most modern Linux distributions like Ubuntu, CentOS, and Debian use systemd).
- Sudo or root access to execute administrative commands.

### 1. Checking the Status of a Service

To manage network services effectively, you first need to know how to check their current status.

**Example: Checking the status of the Apache HTTP Server (httpd)**

```bash
sudo systemctl status httpd
```

This command will provide output similar to the following:

```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2023-01-17 12:00:00 UTC; 2min 43s ago
 Main PID: 1234 (httpd)
   Status: "Processing requests..."
    Tasks: 55 (limit: 4915)
   Memory: 100.3M
   CGroup: /system.slice/httpd.service
           ├─1234 /usr/sbin/httpd -DFOREGROUND
           ├─1235 /usr/sbin/httpd -DFOREGROUND
           └─1236 /usr/sbin/httpd -DFOREGROUND
```

This output shows that the Apache server is active and running.

### 2. Starting a Service

If the service is not running, you can start it using `systemctl`.

**Example: Starting the Apache HTTP Server**

```bash
sudo systemctl start httpd
```

You can verify that the service has started by checking its status again:

```bash
sudo systemctl status httpd
```

### 3. Stopping a Service

To stop a running service, use the `stop` command.

**Example: Stopping the Apache HTTP Server**

```bash
sudo systemctl stop httpd
```

Again, verify that the service has stopped:

```bash
sudo systemctl status httpd
```

### 4. Enabling and Disabling Services

Enabling a service configures it to start automatically on system boot, while disabling it does the opposite.

**Example: Enabling the Apache HTTP Server to start on boot**

```bash
sudo systemctl enable httpd
```

**Example: Disabling the Apache HTTP Server from starting on boot**

```bash
sudo systemctl disable httpd
```

## Detailed Code Examples

Here are a few more examples with different services and scenarios:

- **Checking the status of the SSH service:**

  ```bash
  sudo systemctl status sshd
  ```

- **Restarting the network service to apply configuration changes:**

  ```bash
  sudo systemctl restart network
  ```

- **Reloading the Apache service after configuration changes without dropping connections:**

  ```bash
  sudo systemctl reload httpd
  ```

## Conclusion

In this tutorial, you've learned how to start, stop, and check the status of network services on a Linux system using `systemctl`. These operations form the basis of managing services effectively in a Linux environment, making it essential for network administrators to be proficient with these commands. As you become more familiar with these commands, you'll find managing network services to be a straightforward task, crucial for maintaining a healthy and responsive network environment.