# Tech Tutorial: Operate Running Systems

## Introduction

Operating running systems effectively involves managing various network services that are crucial for the system's functionality and connectivity. For Red Hat Certified System Administrator (RHCSA) exam takers, understanding how to start, stop, and check the status of these services is essential. This tutorial will focus exclusively on Red Hat Enterprise Linux (RHEL) commands and tools to manage network services, ensuring that learners are well-prepared for the exam and real-world system administration.

## Step-by-Step Guide

In RHEL, network services are typically managed through `systemctl` commands, part of the `systemd` suite, which is the init system and service manager from RHEL 7 onward. We will cover how to use `systemctl` to start, stop, and check the status of services. Additionally, we will briefly discuss the use of `service` and `chkconfig` commands for RHEL 6 compatibility.

### 1. Checking the Status of Network Services

To check the status of a service in RHEL, you use the `systemctl status` command. This command provides detailed information about a service, including whether it is active, the start-up type, and recent log entries.

**Example:**

```bash
sudo systemctl status httpd
```

This command checks the status of the Apache HTTP Server (`httpd`). It will show whether `httpd` is running, stopped, or in any error state.

### 2. Starting Network Services

To start a service in RHEL, use the `systemctl start` command. This command is used when you want to manually start a service that is not running.

**Example:**

```bash
sudo systemctl start httpd
```

This command will start the Apache HTTP Server if it is not already running.

### 3. Stopping Network Services

To stop a running service, use the `systemctl stop` command. This is useful when you need to perform maintenance or configuration changes that require the service to be stopped.

**Example:**

```bash
sudo systemctl stop httpd
```

This command stops the Apache HTTP Server if it is currently running.

### 4. Enabling and Disabling Services

Enabling a service sets it to start automatically at boot, while disabling it does the opposite. This is controlled with `systemctl enable` and `systemctl disable`.

**Example to enable a service:**

```bash
sudo systemctl enable httpd
```

**Example to disable a service:**

```bash
sudo systemctl disable httpd
```

### 5. Restarting and Reloading Services

If you need to apply configuration changes or update a service without stopping it completely, you can use `systemctl restart` to restart the service or `systemctl reload` to reload its configuration.

**Example to restart a service:**

```bash
sudo systemctl restart httpd
```

**Example to reload a service:**

```bash
sudo systemctl reload httpd
```

## Detailed Code Examples

Let's consider a scenario where we need to set up a LAMP stack on a RHEL server.

1. **Install Apache HTTP Server:**

```bash
sudo yum install httpd
```

2. **Start and enable Apache to run at boot:**

```bash
sudo systemctl start httpd
sudo systemctl enable httpd
```

3. **Check the status to ensure it's running:**

```bash
sudo systemctl status httpd
```

4. **Install MariaDB:**

```bash
sudo yum install mariadb-server
```

5. **Start and enable MariaDB:**

```bash
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

6. **Secure MariaDB installation:**

```bash
sudo mysql_secure_installation
```

7. **Install PHP:**

```bash
sudo yum install php php-mysql
```

8. **Restart Apache to apply PHP integration:**

```bash
sudo systemctl restart httpd
```

## Conclusion

Mastering the use of `systemctl` commands is crucial for managing network services on a RHEL system. This tutorial provides a foundation for starting, stopping, checking status, and managing the automatic start of services with `systemctl`. For those preparing for the RHCSA exam, proficiency in these tasks is essential, as they form the backbone of effective system administration in RHEL environments.