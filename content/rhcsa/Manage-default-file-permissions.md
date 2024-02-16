+++
title = "Manage default file permissions"
date = "2024-02-16T10:37:32-05:00"
author = "root"
cover = ""
tags = ["command,", "system.", "`usermod`", "permissions,", "group,", "system", "permissions", "`usermod"]
keywords = ["linux", "`usermod", "users),", "`groupmod", "command", "permissions.", "`groupmod`", "permissions""]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Red Hat Certified Systems Administrator Exam 200 Objective: Manage Default File Permissions

In this tutorial, we will be discussing the Red Hat Certified Systems Administrator Exam 200 objective: Manage Default File Permissions. This topic is important for system administrators as it allows them to set and control default file permissions for users on the system. Having a good understanding of file permissions will help you secure sensitive data and ensure the proper access to files for various users.

## Before we Begin

Before diving into the steps on how to manage default file permissions, it is important to have basic knowledge of Linux file permissions and how they work. If you are unfamiliar with this topic, we recommend reading through our tutorial on "Understanding Linux File Permissions" before continuing.

## Step 1: Understanding Default File Permissions

The default file permissions are the permissions that are automatically assigned to newly created files or directories. These permissions are determined by the umask value, which is a value that is subtracted from the maximum permissions set by the system. The resulting value is then applied as the default permissions for new files and directories.

For example, if the umask value is set to 022, the system will subtract 022 from the maximum permission value of 777 (read, write, execute for all users), resulting in default permissions for new files and directories of 755 (read, write, execute for owner, and read, execute for group and others).

Knowing this, we can now move on to managing default file permissions in our system.

## Step 2: Viewing and Changing the Umask Value

To view the current umask value, we can use the `umask` command in the terminal. This will display the value in octal format. For example, if the output is `0022`, it means the umask value is set to 022.

To change the umask value, we can use the `umask` command with the desired value. For example, to set the umask value to 077, we can use the command `umask 077`. This will change the default permissions for new files and directories to 700 for owner, and no permissions for group and others.

## Step 3: Setting Default File Permissions for Specific Users or Groups

Now that we have a basic understanding of default file permissions and how to change the umask value, let's dive into setting default permissions for specific users or groups.

### Setting Default File Permissions for a Specific User

To set default permissions for a specific user, we can use the `usermod` command with the `-s` option, followed by the desired umask value and the username. For example, if we want to set the default permissions for the user "John" to 0644, we can use the command `usermod -s 0644 John`.

### Setting Default File Permissions for a Specific Group

To set default permissions for a specific group, we can use the `groupmod` command with the `-S` option, followed by the desired umask value and the group name. For example, if we want to set the default permissions for the group "engineers" to 0755, we can use the command `groupmod -S 0755 engineers`.

## Step 4: Customizing Default File Permissions for Specific Directories

In some cases, we may want to customize default permissions for files and directories within a specific directory. This can be achieved by using the `chmod` or `setfacl` commands.

### Using chmod

To customize default permissions for a specific directory, we can use the `chmod` command with the `-R` option to recursively apply the permissions to all files and directories within the specified directory. For example, if we want to set default permissions of 670 for all files and directories within the "secret" directory, we can use the command `chmod -R 670 secret`.

### Using setfacl

Another way to achieve this is by using the `setfacl` command, which allows for more fine-grained control over file permissions. To modify default permissions for a specific directory, we can use the `-d` option followed by the desired permissions and the directory name. For example, to set default permissions of 775 for the "secret" directory and all subdirectories, we can use the command `setfacl -d -m u::rwx,g::rwx,o::rx secret`.

## Conclusion

In this tutorial, we have covered the Red Hat Certified Systems Administrator Exam 200 objective of managing default file permissions. We discussed the importance of understanding umask values and the steps to view and change them. We also learned how to set default permissions for specific users or groups and how to customize default permissions for specific directories. 

Managing default file permissions is essential for maintaining a secure and organized system. We hope this tutorial has provided you with a thorough understanding of this topic and will help you successfully complete this objective on the exam. 