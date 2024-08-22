# Tech Tutorial: Deploy, Configure, and Maintain Systems

## Introduction

In this tutorial, we will explore how to install and update software packages on a Red Hat-based system using different sources such as the Red Hat Network (RHN), a remote repository, or from the local file system. Managing software packages efficiently is crucial for system administrators for maintaining the security and stability of Linux systems.

## Prerequisites

- A Red Hat-based system (such as Red Hat Enterprise Linux, CentOS, or Fedora)
- Root or sudo access
- Internet connectivity (for downloading packages from remote repositories or RHN)

## Step-by-Step Guide

### 1. Installing and Updating Software from Red Hat Network (RHN)

Red Hat Network is a subscription service provided by Red Hat for its enterprise customers. It provides secure package management and updates. Here's how to manage packages using RHN.

#### Registering Your System with Red Hat Subscription Management

Before you can download packages from RHN, your system must be registered and subscribed to relevant channels. Run:

```bash
sudo subscription-manager register --username your_username --password your_password
sudo subscription-manager attach --auto
```

Replace `your_username` and `your_password` with your Red Hat customer portal credentials.

#### Installing Software Packages

To install a package, use the `yum` or `dnf` command (depending on your Red Hat version):

```bash
sudo yum install package_name
```

or

```bash
sudo dnf install package_name
```

For example, to install Apache HTTP Server:

```bash
sudo yum install httpd
```

#### Updating Software Packages

To update all packages to their latest available versions:

```bash
sudo yum update
```

or

```bash
sudo dnf update
```

To update a specific package:

```bash
sudo yum update package_name
```

or

```bash
sudo dnf update package_name
```

### 2. Installing and Updating Software from a Remote Repository

You can also configure additional third-party repositories. EPEL (Extra Packages for Enterprise Linux) is a popular choice.

#### Adding the EPEL Repository

Install the EPEL release package:

```bash
sudo yum install epel-release
```

or

```bash
sudo dnf install epel-release
```

#### Installing Software from EPEL

Once EPEL is enabled, you can install packages from it like any other repository:

```bash
sudo yum install htop
```

or

```bash
sudo dnf install htop
```

### 3. Installing Software from the Local File System

If you have a `.rpm` package file locally, you can install it using `rpm` or `yum/dnf` which resolves dependencies automatically.

#### Installing a Local RPM Package

Navigate to the directory containing your `.rpm` file, then:

```bash
sudo rpm -ivh package_name.rpm
```

or using `yum/dnf`:

```bash
sudo yum localinstall package_name.rpm
```

or

```bash
sudo dnf install ./package_name.rpm
```

## Detailed Code Examples

Let's consider a scenario where you need to set up a web server using Apache, manage it through a secure shell server, and ensure both are always updated.

### Installing Apache and SSH

```bash
sudo yum install httpd openssh-server
```

### Starting and Enabling Services

```bash
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl start sshd
sudo systemctl enable sshd
```

### Keeping the System Updated

Set up a cron job to update all packages daily:

```bash
echo "0 3 * * * root /usr/bin/yum update -y" | sudo tee -a /etc/crontab
```

## Conclusion

In this tutorial, we've covered how to manage software package installations and updates from various sources on Red Hat-based systems. Mastery of these techniques is essential for maintaining secure, stable, and up-to-date Linux systems. Regularly updating your system and applications ensures you have the latest features and security patches, reducing vulnerability to attacks and system failures.