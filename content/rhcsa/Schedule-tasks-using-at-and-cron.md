+++
title = "Schedule tasks using at and cron"
date = "2024-02-16T10:34:55-05:00"
author = "root"
cover = ""
tags = ["`crontab`,", "`cron`.", "task.", "scheduled", "file", "systems", "tasks", "task"]
keywords = ["system.", "command:", "command", "`cron`", "process", "`crontab", "command,", "file."]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


## Introduction
In this tutorial, we will be discussing how to schedule tasks using the `at` and `cron` commands on a Red Hat operating system. This is an important topic covered in the Red Hat Certified Systems Administrator Exam 200 and understanding how to schedule tasks is crucial for the efficient management of a system.

### What is Task Scheduling?
Task scheduling is the process of automatically executing a command or script at a specified time or interval. This allows for automation of repetitive tasks and ensures that important tasks are completed on time without manual intervention. In a Red Hat system, there are two main tools used for task scheduling - `at` and `cron`.

### The `at` Command
The `at` command is used to schedule a one-time task to be executed at a specific date and time. This is useful for tasks that do not need to be repeated or run on a regular basis. To use the `at` command, follow the steps below:

1. Open a terminal window and type in `at` followed by the time and date you want the task to be executed. For example, `at 2pm tomorrow` or `at 10:30am + 2 days`.
2. Once you have specified the time, press Enter to open the `at` prompt.
3. Enter the command or script you want to be executed at the specified time. You can also redirect the output of the command to a file.
4. Press `Ctrl+D` to save and exit the `at` prompt.

### The `crontab` Command
The `crontab` command is used to schedule recurring tasks that need to be executed at specified intervals. This is achieved by editing the `crontab` file, which contains a list of commands and their corresponding schedule. To schedule a task using `crontab`, follow these steps:

1. Open a terminal window and type in `crontab -e` to open the `crontab` file in your preferred editor.
2. The `crontab` file is divided into six columns representing the schedule of the task. The columns are as follows:
    * Minute: Ranges from 0-59
    * Hour: Ranges from 0-23
    * Day of Month: Ranges from 1-31
    * Month: Ranges from 1-12
    * Day of Week: Ranges from 0-6 (0 - Sunday, 1 - Monday, etc.)
    * Command: The command or script to be executed

3. Enter the schedule for your task in the appropriate columns. For example, if you want your task to run every day at 2am, your schedule would be `0 2 * * *`.
4. Enter the command or script you want to be executed in the last column.
5. Save and exit the `crontab` file.

### Useful Tips for Scheduling Tasks
1. Use `crontab -l` to view the current list of scheduled tasks in your `crontab` file.
2. Use `crontab -r` to remove all scheduled tasks from your `crontab` file.
3. Use `atq` to verify the status of your `at` tasks.
4. Use `atrm [job number]` to remove a specific `at` task.
5. Use `at -l` to list all `at` tasks.
6. Use `at -c [job number]` to view the command of a specific `at` task.
7. Use `man` command to get help and more information about `crontab` and `at` commands.

## Conclusion
In this tutorial, we have covered the basics of scheduling tasks using `at` and `cron` commands on a Red Hat system. You now have the knowledge and tools to automate tasks and improve the efficiency of your system. Remember to practice and familiarize yourself with these commands to confidently tackle any task scheduling questions on the Red Hat Certified Systems Administrator Exam 200. Good luck!