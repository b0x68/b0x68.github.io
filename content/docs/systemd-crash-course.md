---
date: 2025-01-03
linktitle: Systemd Crash Course
title: Systemd Crash Course
---
![alt](me.jpg)
### **1. What is systemd?**
**systemd** is a system and service manager for Linux that replaces the traditional **SysVinit** and **Upstart**. It's designed for faster boot times, better resource management, and centralized configuration.

Key components of systemd:
- **`systemd`**: The main daemon.
- **`journald`**: Centralized logging system.
- **`timedated`, `logind`, `networkd`**: Manage time, user sessions, and networking.
- **Units**: systemd uses "unit files" to define and control system components like services, sockets, devices, and more.

---

### **2. Basic Commands**

#### **Service Management**
- **Start a service**:
  ```bash
  systemctl start <service>
  ```
- **Stop a service**:
  ```bash
  systemctl stop <service>
  ```
- **Restart a service**:
  ```bash
  systemctl restart <service>
  ```
- **Enable a service (start at boot)**:
  ```bash
  systemctl enable <service>
  ```
- **Disable a service (prevent from starting at boot)**:
  ```bash
  systemctl disable <service>
  ```
- **Check the status of a service**:
  ```bash
  systemctl status <service>
  ```

#### **System State**
- **Reboot the system**:
  ```bash
  systemctl reboot
  ```
- **Power off the system**:
  ```bash
  systemctl poweroff
  ```
- **View system logs**:
  ```bash
  journalctl
  ```

---

### **3. Unit Files**

#### **What are Unit Files?**
Unit files describe system resources and are located in `/etc/systemd/system/` (custom), `/lib/systemd/system/` (default), or `/usr/lib/systemd/system/`.

Types of unit files:
- **`.service`**: Services (e.g., web servers, databases).
- **`.socket`**: Sockets for communication.
- **`.timer`**: Timers (like cron jobs).
- **`.target`**: Group of units (like runlevels).

#### **Viewing and Editing Unit Files**
- **View a unit file**:
  ```bash
  systemctl cat <unit>
  ```
- **Edit a unit file**:
  ```bash
  sudo systemctl edit <unit>
  ```
  This opens an override file for safe customization.

#### **Reload systemd after editing**:
  ```bash
  systemctl daemon-reload
  ```

---

### **4. Boot Targets**
**Targets** are similar to runlevels in SysVinit.

Common targets:
- `graphical.target`: Multi-user with a graphical interface.
- `multi-user.target`: Multi-user without GUI (default for servers).
- `rescue.target`: Single-user mode.
- `emergency.target`: Minimal system, no services.

Commands:
- **Check current target**:
  ```bash
  systemctl get-default
  ```
- **Change default target**:
  ```bash
  systemctl set-default <target>
  ```
- **Switch to a target**:
  ```bash
  systemctl isolate <target>
  ```

---

### **5. Logging with journalctl**
`journalctl` manages logs. It's a central logging system for systemd.

- **View logs**:
  ```bash
  journalctl
  ```
- **View logs for a service**:
  ```bash
  journalctl -u <service>
  ```
- **Follow logs in real-time**:
  ```bash
  journalctl -f
  ```
- **View logs since a specific time**:
  ```bash
  journalctl --since "2025-01-01 00:00:00"
  ```

---

### **6. Creating a Custom Service**

1. **Create the unit file**:
   ```bash
   sudo nano /etc/systemd/system/myapp.service
   ```
   Example:
   ```ini
   [Unit]
   Description=My Custom Application
   After=network.target

   [Service]
   ExecStart=/usr/bin/myapp
   Restart=always
   User=myuser

   [Install]
   WantedBy=multi-user.target
   ```

2. **Reload systemd**:
   ```bash
   systemctl daemon-reload
   ```

3. **Enable and start the service**:
   ```bash
   systemctl enable myapp.service
   systemctl start myapp.service
   ```

4. **Check status**:
   ```bash
   systemctl status myapp.service
   ```

---

### **7. Useful Tools**
- **`systemctl`**: Main tool for managing services and units. 
- **`journalctl`**: Log management. 
- **`systemd-analyze`**: Debug and analyze boot performance. 
  ```bash
  systemd-analyze blame
  ```

---

### **8. Advanced Features**
- **Timers**: systemd alternative to `cron`. 
  Example timer unit:
  ```ini
  [Unit]
  Description=Run MyApp Daily

  [Timer]
  OnCalendar=daily
  Persistent=true

  [Install]
  WantedBy=timers.target
  ```

- **Socket Activation**: Services start only when needed. 
- **Resource Management**: Use `systemd-cgls` and `systemd-cgtop` to manage cgroups. 

---

Mastering **systemd** makes you more efficient at managing Linux systems. It's a powerful tool with many features to explore. Dive deeper into its documentation and practice to become a pro! 🚀
