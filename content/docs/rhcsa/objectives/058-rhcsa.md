# Tech Tutorial: Manage SELinux Port Labels

## Introduction

Security-Enhanced Linux (SELinux) is a security architecture integrated into various Linux distributions. It provides a mechanism for supporting access control security policies, including United States Department of Defense-style mandatory access controls (MAC). One of the crucial aspects of SELinux is managing port labels, which is essential for maintaining the security integrity of services that depend on network communication.

In this tutorial, we will explore how to manage SELinux port labels effectively. Understanding and configuring these labels can help in ensuring that only allowed services can bind to specific ports, enhancing your system's security.

## Prerequisites

Before getting started, ensure that:
- You have a Linux system with SELinux installed and enabled.
- You have root or sudo privileges on this system.
- The `semanage` and `seinfo` commands are available (These come with the policycoreutils-python package on many distributions).

## Step-by-Step Guide

### Step 1: Checking SELinux Status

First, ensure that SELinux is enabled and set to enforcing mode. You can check this by running:

```bash
sestatus
```

The output should indicate `SELinux status: enabled` and `Current mode: enforcing`. If SELinux is disabled or in permissive mode, you need to enable it and set it to enforcing for this tutorial.

### Step 2: Display Current Port Labels

To see the current SELinux port labels, use the `semanage port -l` command. This will list all port and protocol combinations along with their associated SELinux types.

```bash
semanage port -l
```

This command provides a lot of output, so you might want to use `grep` to filter for the specific service or port, for instance:

```bash
semanage port -l | grep http
```

### Step 3: Adding a New Port Label

If you need to allow a service to listen on a non-standard port that isn't already labeled appropriately, you will need to add a new port label. Suppose you want to allow the HTTP service to listen on port 8080. You would first check if this port is already labeled:

```bash
semanage port -l | grep 8080
```

If no results are returned, you can add a label using:

```bash
semanage port -a -t http_port_t -p tcp 8080
```

Here, `-a` stands for add, `-t` specifies the type (http_port_t is typically used for HTTP services), `-p` denotes the protocol, and `8080` is the port.

### Step 4: Modifying Existing Port Labels

Should you need to change the label of an existing port, you use the modify command. For example, if HTTP is mistakenly set to listen on port 8020 and it should be 8080, you would:

```bash
semanage port -m -t http_port_t -p tcp 8020
```

### Step 5: Deleting a Port Label

To remove a port label, which might be necessary if a service is no longer used or a port should no longer be specifically labeled, you can do so with:

```bash
semanage port -d -t http_port_t -p tcp 8080
```

Here, `-d` is used to delete the specified port label.

## Detailed Code Examples

Here are some concrete code examples to manage SELinux port labels:

**Add a new SELinux port label:**

```bash
# Add SMTP service on TCP port 2525
semanage port -a -t smtp_port_t -p tcp 2525
```

**Modify an existing SELinux port label:**

```bash
# Change SSH port label from 22 to 2222
semanage port -m -t ssh_port_t -p tcp 2222
```

**Delete an SELinux port label:**

```bash
# Remove custom SSH port label
semanage port -d -t ssh_port_t -p tcp 2222
```

## Conclusion

Managing SELinux port labels is essential for maintaining secure system configurations. By properly assigning SELinux types to ports, you can ensure that only designated services have access to them, thus enhancing your system's overall security posture. Regularly reviewing and updating these settings as your network services change is a best practice that should not be overlooked.