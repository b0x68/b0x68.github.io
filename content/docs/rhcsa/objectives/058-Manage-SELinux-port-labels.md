# Tech Tutorial: Manage SELinux Port Labels

## Introduction

**Security-Enhanced Linux (SELinux)** is a mandatory access control (MAC) security mechanism implemented in the kernel. SELinux offers a means of enforcing some security policies which would otherwise not be effectively implemented by a System Administrator.

When you are managing a system that uses SELinux, one of the tasks you may need to perform is managing port labels. SELinux uses port labels to enforce policies on how processes can access ports. This tutorial will guide you through the process of managing SELinux port labels on a Red Hat Enterprise Linux (RHEL) system, which is crucial for the preparation of the Red Hat Certified System Administrator (RHCSA) exam.

## Prerequisites

Before you begin, ensure that you have:

- A running RHEL 8 system.
- Sudo privileges or access to the root account.

## Step-by-Step Guide

### Step 1: Checking the Status of SELinux

Before manipulating SELinux settings, it’s important to check whether SELinux is enabled and enforcing. You can do this with the following command:

```bash
$ getenforce
```

This command will return `Enforcing`, `Permissive`, or `Disabled`.

### Step 2: Discovering Current Port Labels

To see the SELinux labels for ports, you can use the `semanage` command. For example, to list the current SELinux port contexts:

```bash
$ sudo semanage port -l
```

This command will output a list of port types and their associated ports, which is helpful to understand before making any changes.

### Step 3: Adding a Port Label

If a specific application needs to listen on a port that does not currently have the correct SELinux label, you will need to add a new label. For instance, if you have a service that needs to run on port 8080 and requires the `http_port_t` label, you would use:

```bash
$ sudo semanage port -a -t http_port_t -p tcp 8080
```

- `-a` is for add.
- `-t` specifies the type (in this case, `http_port_t`).
- `-p` specifies the protocol (tcp or udp).
- `8080` is the port number.

### Step 4: Modifying an Existing Port Label

If the port is already labeled but needs a different label, you must modify it. For instance, if port 8080 was incorrectly set to `ssh_port_t` and it needs to be `http_port_t`, you would use:

```bash
$ sudo semanage port -m -t http_port_t -p tcp 8080
```

- `-m` is for modify.

### Step 5: Deleting a Port Label

If a port label is no longer necessary, it can be removed. For example, to remove the label for port 8080, you would use:

```bash
$ sudo semanage port -d -p tcp 8080
```

- `-d` is for delete.

### Step 6: Verifying Changes

After making changes, it's a good practice to verify them. List the SELinux port contexts again to ensure your changes were applied:

```bash
$ sudo semanage port -l | grep 8080
```

## Detailed Code Examples

Here’s a more complex scenario where you need to ensure a custom application running on TCP ports 5000 and 5001 has the correct SELinux labels:

1. **Check existing labels:**

    ```bash
    $ sudo semanage port -l | grep 5000
    $ sudo semanage port -l | grep 5001
    ```

2. **Add required labels if they do not exist:**

    ```bash
    $ sudo semanage port -a -t my_custom_port_t -p tcp 5000
    $ sudo semanage port -a -t my_custom_port_t -p tcp 5001
    ```

3. **Verify the labels:**

    ```bash
    $ sudo semanage port -l | grep my_custom_port_t
    ```

## Conclusion

Managing SELinux port labels is a critical skill for any system administrator working with RHEL, particularly in environments where security is a priority. By understanding how to add, modify, and delete port labels, you can ensure that services on your system run smoothly without compromising on security. Remember, incorrect SELinux settings can lead to services failing to start or operate correctly, so always verify your changes.