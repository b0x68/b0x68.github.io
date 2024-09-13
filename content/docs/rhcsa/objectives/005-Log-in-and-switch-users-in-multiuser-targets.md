# Tech Tutorial: Understand and Use Essential Tools

## Introduction

One of the fundamental skills required for managing Red Hat Enterprise Linux (RHEL) systems, particularly in a multiuser environment, is the ability to manage user sessions. This includes logging in and switching users, especially in systems that operate with multiuser targets. This tutorial aims to equip you with the knowledge and skills needed to proficiently log in and switch users in RHEL, adhering strictly to the exam objectives of the Red Hat Certified System Administrator (RHCSA) exam.

## Step-by-Step Guide

### Logging In to RHEL

When you access a RHEL system, whether via a direct login at the physical machine or remotely using SSH (Secure Shell), you are prompted to enter your username and password. This process authenticates your access to the system, ensuring that user-specific settings and permissions are applied.

#### Using SSH to Log In

1. **Open your terminal**: Start by opening a terminal on your local machine.

2. **Connect via SSH**: Use the SSH command to log into the RHEL system. Replace `username` with your actual user name and `server-ip` with the IP address of the RHEL server.

   ```bash
   ssh username@server-ip
   ```

3. **Enter your password**: After entering the command, you will be prompted to enter the password for the `username`. Once authenticated, you will be logged into the user's home directory.

### Switching Users

Once logged into a RHEL system, you may need to switch between different users depending on the task requirements. This is commonly done using the `su` (substitute user) or `sudo` commands.

#### Using `su` to Switch Users

1. **Switch to another user**: To switch to another user, use the `su` command followed by the username. For example, to switch to the user `john`, you would use:

   ```bash
   su - john
   ```

   The hyphen (`-`) ensures that you inherit the user environment correctly.

2. **Enter the user's password**: You will be prompted to enter the password for the user `john`.

#### Using `sudo` to Switch to Root

The `sudo` command allows a permitted user to execute a command as the superuser or another user. This is configured through the `/etc/sudoers` file.

1. **Switch to the root user**: If you have sudo privileges, you can switch to the root user by typing:

   ```bash
   sudo su -
   ```

2. **No password prompt**: If your user is configured in the `sudoers` file to not require a password for switching to the root user, you won’t see a prompt.

### Detailed Code Examples

Let’s consider a scenario where you need to log into a server, switch to a user that has specific permissions, and run a command that requires those permissions.

1. **Log into the server**:

   ```bash
   ssh lisa@10.20.30.40
   ```

2. **Switch to the user with specific permissions**:

   ```bash
   su - specialuser
   ```

3. **Run a command that requires specialuser’s permissions**:

   ```bash
   whoami
   ```

   This command will output `specialuser`, confirming that you have switched users successfully.

### Conclusion

Being able to log in and switch users in RHEL is a crucial skill for system administrators, especially when managing multiuser environments. This tutorial covered the basics of logging into a RHEL system and switching between users using `su` and `sudo`. Mastery of these commands not only aids in effective system administration but also prepares you for tasks you might encounter on the RHCSA exam. Always remember to verify user permissions and ensure secure handling of authentication credentials when working in multiuser environments.