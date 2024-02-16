+++
title = "List and identify SELinux file and process context"
date = "2024-02-16T10:38:00-05:00"
author = "root"
cover = ""
tags = ["user's", "user_r", "linux", "kernel", "command.", "user", "(security-enhanced", "processes,"]
keywords = ["permissions", "linux", "kernel", "files", "security", "command.", "permissions.", "user_r"]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: List and identify SELinux file and process context

## Introduction:
The SELinux (Security-Enhanced Linux) is a Linux kernel security module that provides a mandatory access control (MAC) mechanism. It allows system administrators to restrict user's access to the system resources based on the granular security policies. In this tutorial, we will explore the objective "List and identify SELinux file and process context" in detail.

## Prerequisites:
Before proceeding with this tutorial, it is assumed that you have a basic understanding of SELinux and its role in a Red Hat Enterprise Linux (RHEL) system.

## List and Identify SELinux File Context:
SELinux provides a context-based security model, where every file and process is assigned a unique security context. This context contains information about the file's type, user, role, and sensitivity level. To list the SELinux file context, you can use the `ls -Z` command.

```
$ ls -Z /var/www/index.html
-rw-r--r--. root root system_u:object_r:httpd_sys_rw_content_t:s0 /var/www/index.html 
```

Here, the security context is displayed in the last column of the output. It follows the `user:role:type:level` syntax. Let's understand each of these fields in more detail.

- **User:** The SELinux user is the map of the Linux user to a SELinux security identity. It is used to determine a user's permissions within the system.
- **Role:** The SELinux role defines a set of permissions that a user can assume. For example, the sysadm_r role has more permissions compared to the user_r role.
- **Type:** The SELinux type determines the type of access that is allowed or denied to a process or file. Each type is assigned a unique label, which can be used in security policies to restrict access.
- **Level:** The SELinux level is used to specify the sensitivity of data. A higher level means it has a higher sensitivity.

## List and Identify SELinux Process Context:
Similar to file context, SELinux also assigns a context to every process. This context contains information about the user, role, type, and sensitivity level of a process. To list the SELinux context of processes, you can use the `ps -efZ` command.

```
$ ps -efZ | grep httpd
system_u:system_r:httpd_t:s0 root      9588     1  0 Jul16 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
system_u:system_r:httpd_t:s0 apache    9591  9588  0 Jul16 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
system_u:system_r:httpd_t:s0 apache    9592  9588  0 Jul16 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
system_u:system_r:httpd_t:s0 apache    9593  9588  0 Jul16 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
system_u:system_r:httpd_t:s0 apache    9594  9588  0 Jul16 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
```

The output follows the same format as the file context, with the `user:role:type:level` syntax. In this case, the type is httpd_t as the processes belong to the Apache HTTP server. 

## Modifying SELinux File and Process Context:
The SELinux context of a file or process can be modified using the `chcon` command. This command allows administrators to change the SELinux type of an object without modifying the underlying permissions. However, it is recommended to use the `semanage` command, which is the SELinux Policy Management tool, to make permanent changes to the SELinux context.

```
$ semanage fcontext -a -t samba_share_t "/var/share(/.*)?"
```

The above command adds a rule to the SELinux policy to allow the Samba service to access files in the /var/share directory. 

## Conclusion:
In this tutorial, we learned about the SELinux file and process context. We explored how to list and identify the SELinux context of files and processes and how to modify them. Understanding how SELinux context works is crucial for securing a RHEL system and passing the Red Hat Certified Systems Administrator Exam 200.