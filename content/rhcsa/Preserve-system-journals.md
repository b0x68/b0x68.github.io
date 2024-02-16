+++
title = "Preserve system journals"
date = "2024-02-16T11:47:08-05:00"
author = "root"
cover = ""
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: How to Preserve System Journals on a Red Hat Certified System Administrator Exam

As a Red Hat Certified System Administrator, one of the key skills you are required to possess is the ability to preserve system journals. System journals contain important information and logs about the system's activities, which can be crucial in troubleshooting and identifying system issues. In this tutorial, we will explore in great depth how to preserve system journals on a Red Hat Certified System Administrator Exam.

## Step 1: Understanding the Importance of System Journals

System journals are a collection of log files that record various system activities, including system events, user activities, software updates, and more. These logs are essential in monitoring and troubleshooting the system's performance and identifying any issues that may arise.

Preserving system journals is crucial as it ensures that the data recorded in these logs is not lost. This data can be critical in diagnosing and resolving system problems, and without it, the troubleshooting process can become much more challenging.

## Step 2: Identifying the Different Types of System Journals

There are two main types of system journals that you may encounter on the Red Hat Certified System Administrator Exam: the systemd journal and the rsyslog journal.

The **systemd journal** is the default logging system on Red Hat Enterprise Linux (RHEL) 7 and above. It collects and stores system logs in binary format in /run/log/journal. This type of journal is managed by the `journalctl` command.

The **rsyslog journal** is the legacy logging system that is still used in RHEL 6 and some older versions. It collects and stores logs in plain text format in /var/log directory. This type of journal is managed by the `rsyslogd` service.

## Step 3: Configuring Systemd Journal Preserving on RHEL 7 and above

To preserve systemd journals on RHEL 7 and above, you need to configure the journal's retention policy. This policy defines how long the system logs will be preserved before being automatically deleted.

1. To configure the retention policy, open the /etc/systemd/journald.conf file with a text editor.

2. Locate the `[Journal]` section and add the following line: `MaxRetentionSec=<duration>`

3. Replace `<duration>` with the desired retention period in seconds. For example, to preserve the logs for 1 year, you would input `MaxRetentionSec=31536000` (60 seconds x 60 minutes x 24 hours x 365 days).

4. Save the changes and exit the text editor.

5. Reload the systemd journal configuration by running the command `systemctl restart systemd-journald`.

6. Test the retention policy by creating a test log and checking if it is still present after the specified duration.

## Step 4: Configuring Rsyslog Journal Preserving on RHEL 6 and older versions

To preserve rsyslog journals on RHEL 6 and older versions, you will need to configure the rsyslogd service to store logs in a separate directory. This will ensure that the logs are not deleted when the /var/log directory is rotated.

1. Create a new directory to store the preserved logs. For example, `/var/log/preserved`.

2. Open the `/etc/rsyslog.conf` file with a text editor.

3. Locate the `$WorkDirectory` line and edit it to point to the new directory you created in the previous step. For example, `$WorkDirectory /var/log/preserved`.

4. Locate the `$ActionFileDefaultTemplate` line and add `DefaultFile` at the end. This will ensure that logs are stored in the specified directory with the correct file name.

5. Save the changes and exit the text editor.

6. Reload the rsyslogd service by running the command `service rsyslog restart`.

7. Test the configuration by creating a test log and checking if it is present in the new directory.

## Step 5: Other Tips for Preserving System Journals

Here are a few additional tips to keep in mind when preserving system journals on a Red Hat Certified System Administrator Exam:

- Regularly back up the system logs to a separate location to ensure they are not lost in case of system failure.
- Adjust the log rotation frequency to ensure that logs are not deleted before the retention period.
- Use the `journalctl` or `rsyslogd` commands to view and manage the system logs.
- Familiarize yourself with the various log files and their contents to better understand the system's activities.

## Conclusion

Preserving system journals is an essential skill for any Red Hat Certified System Administrator. In this tutorial, we have explored how to configure the retention policy for systemd and rsyslog journals, as well as some additional tips to keep in mind. By following these steps, you will be well prepared to preserve system journals on the Red Hat Certified System Administrator Exam.