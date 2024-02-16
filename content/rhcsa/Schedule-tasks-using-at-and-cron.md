+++
title = "Schedule tasks using at and cron"
date = "2024-02-16T11:49:44-05:00"
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


# Introduction

In this tutorial, we will be discussing the Red Hat Certified Systems Administrator Exam 200 Objective of "Schedule tasks using at and cron". This topic is crucial in managing a Red Hat Linux system as it allows for automated tasks to be executed at specific times or intervals. We will walk through the concepts of at and cron, how they differ, and how to use them effectively to schedule tasks. 

# Prerequisites

Before beginning this tutorial, the following prerequisites are required:

- Basic knowledge of Red Hat Linux system administration
- A Red Hat Linux system, preferably version 7 or higher
- A user account with sudo privileges

# Understanding at and cron

The two primary tools used for scheduling tasks in a Linux system are at and cron. These tools have similar functionalities, but they have significant differences. 

## at

at is a command-line utility that allows for one-time tasks to be executed at a specific time and date. It is ideal for tasks that need to be performed at a specific time in the future, such as a system backup or maintenance task. The syntax for using at is as follows:

```
at <time> [OPTIONS] [<date>] [<file>]
```

Where `<time>` can be specified in various formats, such as "HH:MM" for a 24-hour time format or "12:00 am" for a 12-hour time format. The `[OPTIONS]` can include flags for specific behaviors, such as -f to specify a file containing the task to be executed. `<date>` is an optional field to specify a specific date when the task needs to be executed, and `<file>` is the file containing the task to be executed. 

## cron

cron is a system utility that allows for scheduled tasks to be executed repeatedly at specified intervals. It is ideal for tasks that need to be performed on a regular basis, such as system updates or log rotations. The syntax for using cron is as follows:

```
<minute> <hour> <day of month> <month> <day of week> <command>
```

Each field represents different time intervals, and the command is the task to be executed. For example, if we want to schedule a task to run every day at 2:30 am, the cron entry would look like this: 

```
30 2 * * * /bin/task
```

# Using at and cron

Now that we understand the basics of at and cron, let's go through a step-by-step guide on how to use them. 

## Using at to Schedule Tasks

1. To use at, we need to first start the atd service if it is not already running. We can do this by running the following command: 

```
sudo systemctl start atd.service
```

2. Once the service is running, we can use the at command to schedule a task. For example, let's schedule a system backup to run at 2:00 am tomorrow using the at command:

```
at 2:00 am tomorrow -f /bin/backup.sh
```

This will schedule the execution of the backup script at the specified time and date.

3. We can view all scheduled tasks using the `atq` command, and we can remove a scheduled task using the `atrm` command, followed by the job ID. 

## Using cron to Schedule Tasks

1. To use cron, we first need to access the crontab file by running the following command:

```
crontab -e
```

2. This will open the crontab file in a text editor. Using the syntax mentioned earlier, we can add our scheduled task to the end of the file. 

```
30 2 * * * /bin/backup.sh
```

This will schedule the backup script to run every day at 2:30 am.

3. Once we save and close the file, the task is scheduled and will be executed repeatedly at the specified intervals. 

# Additional Tips and Best Practices

- When using at, always specify a specific time and date to avoid any unexpected executions. 
- When using cron, use the absolute path for the task/command to ensure it runs correctly.
- To disable a cron job temporarily, comment it out with a `#` symbol at the beginning of the line in the crontab file.
- Use the `crontab -l` command to list all scheduled tasks in the crontab file.
- It is recommended to test the commands/scripts before scheduling them using at or cron to avoid any errors in the execution.

# Conclusion

In conclusion, scheduling tasks using at and cron are essential skills for managing a Red Hat Linux system. With the knowledge gained from this tutorial, you should now be able to effectively schedule tasks using these tools and enhance the automation of your system administration tasks. Remember to practice and experiment with different commands and scripts to become comfortable with using at and cron. Happy scheduling!