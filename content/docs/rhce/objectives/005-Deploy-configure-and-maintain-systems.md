# Tech Tutorial: Perform Tasks Expected of a Red Hat Certified System Administrator

## Introduction

In this tutorial, we will delve into essential tasks for deploying, configuring, and maintaining systems, which are critical skills for a Red Hat Certified System Administrator (RHCSA). Our focus will be on practical, real-world examples that will help you gain a solid understanding and hands-on experience. We will use CentOS, a popular Red Hat Enterprise Linux (RHEL) clone, to demonstrate these tasks, as it provides a free-to-use platform that mirrors RHEL’s functionality.

## Pre-requisites

Before you begin, ensure you have the following:

- A machine with CentOS installed (VirtualBox or VMware for virtual environments)
- Basic familiarity with Linux command line

## Step-by-Step Guide

This guide is divided into several sections to cover the deployment, configuration, and maintenance of Linux systems thoroughly.

### 1. System Deployment

**Deploying a New Service: Apache HTTP Server**

Let’s start by deploying the Apache HTTP Server, a widely used web server software.

#### Installation:

```bash
sudo yum install httpd -y
```

#### Configuration:

Edit the Apache configuration file to customize the server.

```bash
sudo vi /etc/httpd/conf/httpd.conf
```

You might want to change the `Listen` directive to specify the port Apache runs on (default is 80) and set the `ServerName` to your domain or IP address.

#### Enable and Start Service:

```bash
sudo systemctl enable httpd
sudo systemctl start httpd
```

Check the status to ensure it is running without errors.

```bash
sudo systemctl status httpd
```

### 2. System Configuration

**Setting Up a Cron Job**

Cron jobs are used to schedule scripts or commands to run automatically at specified times and dates.

#### Edit Cron Jobs:

```bash
crontab -e
```

#### Add a Cron Job:

For example, to backup a directory every day at 1 am:

```bash
0 1 * * * /usr/bin/rsync -av /home/user/data /backup/data
```

### 3. System Maintenance

**Updating System Packages**

Regular updates are essential for security and functionality.

#### Check for Updates:

```bash
sudo yum check-update
```

#### Apply Updates:

```bash
sudo yum update -y
```

**Setting Up System Logging with rsyslog**

System logging is crucial for diagnosing and understanding what happens on your system.

#### Install rsyslog (if not installed):

```bash
sudo yum install rsyslog -y
```

#### Configure rsyslog:

Edit the configuration file to define what data to collect and where to store it.

```bash
sudo vi /etc/rsyslog.conf
```

Add a line to store all critical messages in a specific file:

```bash
*.crit   /var/log/critical.log
```

#### Restart the service to apply changes:

```bash
sudo systemctl restart rsyslog
```

## Conclusion

In this tutorial, we covered key aspects of deploying, configuring, and maintaining systems as expected from a Red Hat Certified System Administrator. By following this guide, you have learned how to install and configure the Apache HTTP Server, manage cron jobs, update system packages, and set up basic logging with rsyslog.

These skills form the foundation of effective system administration and will help ensure that your systems are reliable, secure, and performant. Remember, practical experience and continuous learning are crucial in mastering Linux administration.