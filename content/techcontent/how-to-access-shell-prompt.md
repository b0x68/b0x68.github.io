+++
title = "How to Access Shell Prompt"
date = "2024-01-31T13:18:25-05:00"
author = "root"
cover = "shell-prompt.png"
tags = ["red hat", "linux", "shell", "command line", "RHCSA",]
keywords = ["red hat", "linux", "shell", "command line", "RHCSA",]
description = "Understand and use essential tools: Access a shell prompt and issue commands with correct syntax"
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++

**Red Hat Certified Systems Administrator (RHCSA) Exam Objectives Tutorial**

**Access the Command Line**
---

Objective 1: Log in to a Linux system and run simple commands using the shell

In this tutorial, we will learn how to log in to a Linux system and execute simple commands using the shell.

1. **Logging in to a Linux system**: 
   - Open a terminal window.
   - Use the `ssh` command to connect to the desired Linux system: 
     ```bash
     ssh username@hostname
     ```
   - Enter the password when prompted.

2. **Executing Simple Commands**:
   - Once logged in, you can run various commands. Here are a few examples:
     - `ls`: List files and directories in the current location.
     - `pwd`: Print the current working directory.
     - `whoami`: Display the username of the current user.
     - `date`: Show the current date and time.
     
   Example:
   ```bash
   $ ls
   Desktop  Documents  Downloads  Music  Pictures  Videos

