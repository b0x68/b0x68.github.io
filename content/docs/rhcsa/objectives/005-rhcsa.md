# Tech Tutorial: Understand and Use Essential Tools

## Exam Objective: Log in and Switch Users in Multiuser Targets

### Introduction

In any multi-user operating system, such as Linux, being able to switch between users efficiently is crucial for managing file permissions, running processes, and securing the system. This tutorial will cover how to log in and switch users in a system using multiuser targets. A "multiuser target" is a state of a system (common in systemd, which is a system and service manager for Linux operating systems) where multiple users can log in and operate the system simultaneously.

### Pre-requisites

- A Linux system with systemd installed (most modern Linux distributions like Ubuntu, CentOS, or Debian have this by default).
- Access to a terminal or command line interface.
- Some basic familiarity with using the command line.

### Step-by-Step Guide

#### 1. Logging into the System

When you boot up a Linux system, you are typically greeted with a login prompt where you can enter your username and password. This can either be in a graphical or a text-based environment.

**For Graphical Interface:**

- Enter your username and password on the login screen.
- Press Enter or click the login button.

**For Text Interface (TTY):**

- At the login prompt, type your username and press Enter.
- Enter your password and press Enter.

**Using the Command Line:**

If you are accessing the system remotely via SSH, use the following command:

```bash
ssh username@hostname
```

Replace `username` with your actual username and `hostname` with the IP address or domain name of the system.

#### 2. Switching Users in the Terminal

Once logged in, you may need to switch to another user account to perform specific tasks.

**Using `su` (Switch User):**

To switch to another user, use the `su` command followed by the username:

```bash
su - username
```

The `-` option provides an environment similar to what the user would expect had they logged in directly.

You will be prompted to enter the user's password unless you are the superuser (root).

**Example:**

```bash
su - john
```

**Using `sudo` to Switch Users:**

If your user has `sudo` privileges, you can switch to another user using:

```bash
sudo su - username
```

This command switches you to the specified user without needing that user's password, relying instead on your own `sudo` privileges.

**Example:**

```bash
sudo su - john
```

#### 3. Returning to the Original User

To return to your original user session after using `su`, type:

```bash
exit
```

This command will log you out of the current user session and revert to the previous one.

### Detailed Code Examples

Here's a common scenario in a system administration context:

**Task:** You need to log in as a regular user, switch to the root user, edit a configuration file, then revert to the original user.

**Step 1: Log in as the Regular User**

```bash
ssh regularuser@192.168.1.100
```

**Step 2: Switch to Root User**

```bash
sudo su -
```

**Step 3: Edit a Configuration File**

```bash
nano /etc/important-config.conf
```

Make necessary changes and save the file.

**Step 4: Revert to Original User**

```bash
exit
```

### Conclusion

Understanding how to log in and switch users in multiuser environments is fundamental for system administration and security management. By mastering these commands, you can effectively manage user permissions and tasks across a diverse system environment. Remember, with great power comes great responsibility, so always use these capabilities judically and securely.