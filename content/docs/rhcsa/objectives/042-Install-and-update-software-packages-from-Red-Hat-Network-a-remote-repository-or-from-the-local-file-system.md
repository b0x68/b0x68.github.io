# Tech Tutorial: Deploy, Configure, and Maintain Systems

## Introduction

In this tutorial, we will delve into the process of installing and updating software packages on a Red Hat-based system. Managing software packages efficiently is crucial for maintaining the security and stability of your systems. We will explore how to handle these tasks using the Red Hat Network (RHN), a remote repository, and from the local file system.

### Objectives:

- Understand the use of `yum` and `dnf` package managers.
- Learn to install and update software packages from Red Hat Network.
- Discover how to configure and use remote repositories.
- Practice installing packages from the local file system.

## Prerequisites

- A Red Hat-based distribution (e.g., CentOS, Fedora, or RHEL)
- Basic familiarity with Linux terminal
- Sudo or root access on your system

## Step-by-Step Guide

### 1. Installing and Updating Software Packages using YUM and DNF

`yum` (Yellowdog Updater Modified) and `dnf` (Dandified YUM) are the package management utilities in Red Hat-based distributions. While `yum` is traditionally used in older versions (CentOS/RHEL 7 and before), `dnf` has taken its place in newer releases (Fedora 22+, CentOS 8+).

#### Installing a Package

To install a package, you can use the following command:

For `yum`:

```bash
sudo yum install package-name
```

For `dnf`:

```bash
sudo dnf install package-name
```

**Example:**

```bash
sudo dnf install httpd
```

This command installs the Apache HTTP Server.

#### Updating a Package

To update a specific package:

For `yum`:

```bash
sudo yum update package-name
```

For `dnf`:

```bash
sudo dnf update package-name
```

**Example:**

```bash
sudo dnf update httpd
```

This command updates the Apache HTTP Server to the latest version available in the repository.

### 2. Using the Red Hat Network (RHN)

Red Hat Network is a subscription-based service that allows you to manage your Red Hat systems and download updates and software from Red Hat's centralized server.

#### Registering Your System

Before using RHN, your system must be registered. Here's how you can register:

```bash
sudo subscription-manager register --username your-username --password your-password
```

After registration, you can attach a subscription:

```bash
sudo subscription-manager attach --auto
```

#### Installing and Updating from RHN

Once your system is registered, installing and updating packages is done using `yum` or `dnf` as described previously.

### 3. Configuring and Using a Remote Repository

Sometimes, you might need packages that are not available in the default repositories. You can configure additional repositories.

#### Adding a Repository

Create a `.repo` file in `/etc/yum.repos.d/`:

```bash
sudo vi /etc/yum.repos.d/example.repo
```

Add the following information:

```plaintext
[example-repo]
name=Example Repository
baseurl=http://example.com/repo/
enabled=1
gpgcheck=1
gpgkey=http://example.com/repo/RPM-GPG-KEY-example
```

#### Using the Repository

After adding the repository, you can install packages from it as follows:

```bash
sudo dnf install package-from-example-repo
```

### 4. Installing from the Local File System

If you have a `.rpm` file on your local system, you can install it using `dnf` or `yum`:

```bash
sudo dnf install /path/to/package.rpm
```

**Example:**

```bash
sudo dnf install /home/user/downloads/example-package.rpm
```

## Conclusion

In this tutorial, we covered the essentials of managing software packages on Red Hat-based systems using different methods: through standard package managers (`yum` and `dnf`), the Red Hat Network, remote repositories, and the local file system. Mastery of these tools and techniques is crucial for effective system administration in a Red Hat environment. Practice these skills to ensure you can maintain your systems efficiently and securely.