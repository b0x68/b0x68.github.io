# Tech Tutorial: Deploy, Configure, and Maintain Systems

## Introduction

In this tutorial, we will explore how to install and update software packages on Red Hat Enterprise Linux (RHEL), utilizing resources such as the Red Hat Network (RHN), a remote repository, or the local file system. This is a key competency for the Red Hat Certified System Administrator (RHCSA) exam, and mastering it is essential for effective system administration in a RHEL environment.

## Prerequisites

- A running instance of Red Hat Enterprise Linux.
- Root or sudo access on the system.
- Internet connectivity for accessing remote repositories.

## Step-by-Step Guide

### 1. Registering the System with Red Hat Subscription Management

Before installing packages from the Red Hat Network, your system needs to be registered with Red Hat Subscription Management (RHSM). This allows the system to download and install packages from Red Hat repositories.

```bash
# Register your system
sudo subscription-manager register --username YOUR_USERNAME --password YOUR_PASSWORD

# Attach a subscription
sudo subscription-manager attach --auto
```

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your Red Hat account credentials.

### 2. Installing Software Packages from Red Hat Network

To install packages using `yum` or `dnf` (on RHEL 8 and later), you first need to ensure your package repositories are up to date. Here’s how to do it:

```bash
# On RHEL 7
sudo yum check-update

# On RHEL 8
sudo dnf check-update
```

To install a new package:

```bash
# Using yum (RHEL 7)
sudo yum install package_name

# Using dnf (RHEL 8)
sudo dnf install package_name
```

Replace `package_name` with the name of the software package you want to install.

### 3. Updating Software Packages

Updating your installed software packages is crucial for security and functionality. Use the following commands:

```bash
# Using yum (RHEL 7)
sudo yum update

# Using dnf (RHEL 8)
sudo dnf update
```

This command updates all installed packages to the latest available versions.

### 4. Installing Software from a Local File System

If you have a `.rpm` file on your local file system, you can install it using the `rpm` command:

```bash
sudo rpm -ivh /path/to/package_name.rpm
```

The `-ivh` flag stands for install, verbose, and hash, providing a progress bar during installation.

### 5. Adding a Remote Repository

Sometimes, you might need to install packages from a third-party repository. Here’s how to add it:

```bash
# On RHEL 7
sudo yum-config-manager --add-repo repository_url

# On RHEL 8
sudo dnf config-manager --add-repo repository_url
```

Replace `repository_url` with the URL of the repository you wish to add.

### 6. Removing Software Packages

To remove an installed package:

```bash
# Using yum (RHEL 7)
sudo yum remove package_name

# Using dnf (RHEL 8)
sudo dnf remove package_name
```

## Detailed Code Examples

**Example 1:** Installing Apache Web Server

```bash
# RHEL 7
sudo yum install httpd

# RHEL 8
sudo dnf install httpd
```

**Example 2:** Updating all packages on the system

```bash
# RHEL 7
sudo yum update

# RHEL 8
sudo dnf update
```

**Example 3:** Installing a package from a local file (e.g., `example.rpm`)

```bash
sudo rpm -ivh /home/user/example.rpm
```

## Conclusion

Understanding how to manage software packages is fundamental for any system administrator working with Red Hat Enterprise Linux. By following this guide, you should now be able to install, update, and manage software packages from various sources efficiently. Always ensure that your systems are registered and subscriptions are attached to access official Red Hat repositories. Regular updates and maintenance are crucial for system security and stability.