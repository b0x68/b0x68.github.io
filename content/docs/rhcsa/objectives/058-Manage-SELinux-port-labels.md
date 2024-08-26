# Tech Tutorial: Manage SELinux Port Labels

## Introduction

SELinux (Security-Enhanced Linux) is a security architecture integrated into the kernel that provides a mechanism for supporting access control security policies. This tutorial focuses on one of the specific aspects of SELinux management: port labeling. Port labels are crucial for defining how services interact with different ports, ensuring that only allowed services can bind to specific ports.

This guide is designed to help system administrators and security professionals understand and effectively manage SELinux port labels to enhance system security.

## Prerequisites

Before proceeding, ensure you have:
- A Linux system with SELinux installed and enabled (Preferably CentOS, Fedora, or RHEL).
- Root or sudo access to the system.
- Familiarity with basic Linux commands and the command line interface.

## Step-by-Step Guide

### Step 1: Checking SELinux Status

First, check the status of SELinux on your system:

```bash
sestatus
```

Ensure that the output says `SELinux status: enabled`. If SELinux is disabled, you'll need to enable it and possibly restart your system.

### Step 2: Understanding SELinux Port Labeling

SELinux classifies ports using the context, which includes a type. Each daemon running on your system will have a specific type, and only ports with a compatible type can be accessed by that daemon.

To view the current SELinux context of ports, use the `semanage port -l` command:

```bash
semanage port -l
```

This command lists all current port type definitions.

### Step 3: Adding a New Port Label

Suppose you have a service that runs on a non-standard port, and SELinux is preventing it from starting. You need to add a new port label to allow this.

For example, if you want to allow the Apache HTTP Server to listen on port 8080, you can add a label to this port:

```bash
semanage port -a -t http_port_t -p tcp 8080
```

Here, `-a` is for adding, `-t http_port_t` specifies the type, `-p tcp` indicates the protocol, and `8080` is the port number.

### Step 4: Modifying an Existing Port Label

If a port is already labeled but needs to be changed (e.g., if you want to change the port type that Apache listens on from 8080 to 8090):

First, delete the existing label:

```bash
semanage port -d -t http_port_t -p tcp 8080
```

Then, add the new label:

```bash
semanage port -a -t http_port_t -p tcp 8090
```

### Step 5: Troubleshooting

If a service fails to start and you suspect an SELinux port labeling issue, use the `audit2why` utility to analyze the logs:

```bash
audit2why < /var/log/audit/audit.log
```

This command helps identify and explain AVC (Access Vector Cache) denials related to port labeling, providing insights into what might be the issue.

## Detailed Code Examples

Let's consider a scenario where you are configuring an FTP server that needs to operate on a non-standard port, say 2121:

1. **Check existing FTP port contexts:**

   ```bash
   semanage port -l | grep ftp
   ```

2. **Add the new port label:**

   ```bash
   semanage port -a -t ftp_port_t -p tcp 2121
   ```

3. **Verify the new setting:**

   ```bash
   semanage port -l | grep ftp
   ```

4. **Restart the FTP service:**

   ```bash
   systemctl restart vsftpd
   ```

5. **Check for any AVC denials:**

   ```bash
   audit2why < /var/log/audit/audit.log
   ```

## Conclusion

Managing SELinux port labels is a critical task for maintaining the security integrity of your services. By correctly setting port contexts, you ensure that only designated services have access to their respective ports, thereby minimizing potential security risks. Always use tools like `semanage` and `audit2why` to configure and troubleshoot SELinux settings effectively. Remember, understanding and managing SELinux policies can significantly enhance your system's security posture.