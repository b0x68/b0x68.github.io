# Tech Tutorial: Manage Security as a Red Hat Certified System Administrator

Managing security is a crucial aspect of system administration, particularly when working with Red Hat Enterprise Linux (RHEL). This tutorial aims to provide a comprehensive guide on how to manage security, which is a key objective for the Red Hat Certified System Administrator (RHCSA) exam.

![a young lad fending off a deer](/linux-defense-selinux.png)
## Introduction

Security management in RHEL involves a variety of tasks, from configuring firewalls and enforcing user policies to managing SELinux contexts and ensuring that the system is free from vulnerabilities. This tutorial will cover these aspects in detail, providing practical examples to help you prepare for the RHCSA exam.

## Step-by-Step Guide

### 1. Configuring and Managing Firewalls with firewalld

Firewalld is the default firewall management tool in RHEL and offers support for network/firewall zones, and even allows runtime modifications without dropping existing connections.

#### Installation and Basic Configuration

```bash
# Ensure firewalld is installed
sudo yum install firewalld

# Start firewalld
sudo systemctl start firewalld

# Enable firewalld to start at boot
sudo systemctl enable firewalld
```

#### Adding and Removing Services

```bash
# Add a service to the default zone
sudo firewall-cmd --add-service=http

# Remove a service from the default zone
sudo firewall-cmd --remove-service=http
```

#### Permanent Changes and Reloading

```bash
# Make changes permanent
sudo firewall-cmd --permanent --add-service=https

# Reload firewalld to apply changes
sudo firewall-cmd --reload
```

### 2. Managing User Authentication with PAM (Pluggable Authentication Modules)

PAM is used in RHEL to integrate multiple low-level authentication schemes into a high-level API, which allows programs that rely on authentication to be written independently of the underlying authentication mechanism.

#### Configuring Password Policies

Edit the `/etc/security/pwquality.conf` file to set password quality requirements:

```bash
# Open pwquality configuration file
sudo nano /etc/security/pwquality.conf

# Example configurations:
# minlen = 12
# dcredit = -1
# ucredit = -1
# ocredit = -1
# lcredit = -1
```

Apply changes in PAM by editing `/etc/pam.d/system-auth`:

```bash
# Add or modify the pam_pwquality.so line
password    requisite     pam_pwquality.so try_first_pass retry=3
```

### 3. Enforcing and Managing SELinux Policies

SELinux is a mandatory access control (MAC) security structure implemented in the kernel. Managing SELinux effectively is critical for system security.

#### Checking SELinux Status

```bash
# Check SELinux status
sestatus
```

#### Changing SELinux Modes

```bash
# Set SELinux to permissive mode temporarily
sudo setenforce 0

# To make it permanent, edit the config file
sudo nano /etc/selinux/config
# Change SELINUX=enforcing to SELINUX=permissive
```

#### Restoring Default File Contexts

```bash
# Restore file context to default
sudo restorecon -v /path/to/file
```

### 4. Scanning for Vulnerabilities and Applying Updates

Keeping your system updated is vital for security. RHEL provides tools to check for and apply updates securely.

```bash
# Check for updates
sudo yum check-update

# Apply updates
sudo yum update
```

#### Scanning for Vulnerabilities with OpenSCAP

OpenSCAP is an auditing tool that helps you maintain security compliance.

```bash
# Install OpenSCAP
sudo yum install scap-security-guide

# Perform a security audit
oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_pci-dss --report report.html /usr/share/xml/scap/ssg/content/ssg-rhel7-ds.xml
```

## Conclusion

This tutorial covered essential security management tasks in RHEL, including firewalld configuration, user authentication with PAM, SELinux management, and vulnerability scanning with OpenSCAP. Mastering these tasks will not only prepare you for the RHCSA exam but also equip you with the knowledge to manage RHEL systems securely in real-world scenarios. Remember, security is an ongoing process and staying updated with the latest practices and patches is crucial for maintaining system integrity.