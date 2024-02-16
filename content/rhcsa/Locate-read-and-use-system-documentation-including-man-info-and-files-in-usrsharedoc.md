+++
title = "Locate, read, and use system documentation including man, info, and files in /usr/share/doc"
date = "2024-02-16T11:45:12-05:00"
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



**Introduction:**
Welcome to the tutorial for the Red Hat Certified Systems Administrator Exam 200 Objective on locating, reading, and using system documentation. This is an important skill for Linux administrators as it allows them to effectively troubleshoot and manage their systems. In this tutorial, we will cover the various tools and resources available for accessing system documentation, including man pages, info pages, and files in the /usr/share/doc directory.

**Accessing Man Pages:**
The most common tool for accessing system documentation is the man command. Man pages, short for manual pages, provide detailed documentation on various commands, utilities, and system functions. To view a man page, simply type the command "man" followed by the name of the command or function you want to learn about.

For example, to view the man page for the "ls" command, you would type:
`man ls`

The man page will open in your terminal, allowing you to scroll through it using the arrow keys. You can also use the "page up" and "page down" keys to navigate through longer man pages.

**Understanding Man Page Sections:**
Man pages are divided into different sections to make it easier to find the information you need. The following are the most common sections you will come across:

- Section 1: User Commands - provides documentation on commands available to all users.
- Section 5: File Formats and Conventions - documents file formats and configuration conventions.
- Section 8: System Administration Commands - documents commands typically used by system administrators.

You can specify the section you want to view by adding the section number after the command name. For example:
`man 5 passwd`

This will show the man page for the "passwd" command under section 5, which covers file formats and conventions.

**Navigating Man Pages:**
Man pages are typically organized in a specific way, making it easier to find the information you need. Here are some tips for navigating through man pages:

- Use the "forward slash (/)" key to search for a specific term in the man page.
- Use the "n" key to move to the next instance of the search term.
- Use the "g" key to go to the top of the man page.
- Use the "G" key to go to the bottom of the man page.
- Use the "q" key to quit the man page and return to your terminal.

**Accessing Info Pages:**
Another tool for accessing system documentation is the info command. Info pages provide more in-depth documentation compared to man pages and are typically used for more complex commands or functions.

To view an info page, type the command "info" followed by the name of the command or function. For example:
`info tar`

The info page will open in a separate window, with a hierarchical structure that you can navigate using the arrow keys. Press the "q" key to return to your terminal.

**Accessing Documentation Files:**
The /usr/share/doc directory contains documentation files for various packages and applications installed on your system. These files are usually in plain text format and can provide additional information on how to use or troubleshoot a particular package.

To access these files, navigate to the /usr/share/doc directory and use the "ls" command to view the available files. You can then use the "cat" command to view the contents of a specific file. For example:
`cat /usr/share/doc/coreutils/README`

This will display the contents of the README file for the coreutils package.

**Conclusion:**
In this tutorial, we have covered the various tools and resources for accessing system documentation, including man pages, info pages, and files in the /usr/share/doc directory. Being able to locate, read, and use system documentation is a crucial skill for Linux administrators, and we hope this tutorial has helped you understand the process in great depth. Best of luck on your Red Hat Certified Systems Administrator Exam!