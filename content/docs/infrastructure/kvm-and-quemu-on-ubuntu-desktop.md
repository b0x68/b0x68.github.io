---
title: "KVM and QEMU on Ubuntu Desktop: Comprehensive Guide"
---

# KVM & QEMU on Ubuntu Desktop: Comprehensive Tutorial

A complete guide to installing, configuring, and operating a KVM/QEMU virtualization stack on Ubuntu Desktop — covering everything from hardware verification through advanced VM management, networking, storage, and automation.

---

## Table of Contents

1. [Prerequisites & Hardware Verification](#1-prerequisites--hardware-verification)
2. [Installation](#2-installation)
3. [User & Group Configuration](#3-user--group-configuration)
4. [Networking](#4-networking)
5. [Storage Pools & Disk Images](#5-storage-pools--disk-images)
6. [Creating & Managing VMs with virt-manager](#6-creating--managing-vms-with-virt-manager)
7. [Command-Line VM Management with virsh](#7-command-line-vm-management-with-virsh)
8. [Creating VMs with virt-install](#8-creating-vms-with-virt-install)
9. [QEMU Directly (Without libvirt)](#9-qemu-directly-without-libvirt)
10. [Snapshots & Cloning](#10-snapshots--cloning)
11. [Performance Tuning](#11-performance-tuning)
12. [GPU Passthrough (VFIO)](#12-gpu-passthrough-vfio)
13. [Cloud Images & cloud-init](#13-cloud-images--cloud-init)
14. [Automation with Terraform + libvirt](#14-automation-with-terraform--libvirt)
15. [Monitoring & Troubleshooting](#15-monitoring--troubleshooting)
16. [Security Considerations](#16-security-considerations)

---

## 1. Prerequisites & Hardware Verification

### Check CPU Virtualization Support

KVM requires hardware-assisted virtualization (Intel VT-x or AMD-V).

```bash
# Check for vmx (Intel) or svm (AMD) flags
grep -Eoc '(vmx|svm)' /proc/cpuinfo
# Non-zero output = virtualization is supported

# More detailed check
egrep -c '(vmx|svm)' /proc/cpuinfo
# Shows number of CPU threads with support
```

If you get 0, check your BIOS/UEFI and enable "Intel Virtualization Technology" or "AMD-V / SVM".

### Verify KVM Module is Loaded

```bash
lsmod | grep kvm
# Expected output:
# kvm_intel   (or kvm_amd)
# kvm

# Load manually if not present
sudo modprobe kvm
sudo modprobe kvm_intel   # or kvm_amd
```

### Check IOMMU (for PCI passthrough)

```bash
# Check if IOMMU is enabled
dmesg | grep -e DMAR -e IOMMU
# Look for "DMAR: IOMMU enabled" or "AMD-Vi: AMD IOMMUv2 loaded"

# Check IOMMU groups
find /sys/kernel/iommu_groups/ -type l | sort -V
```

To enable IOMMU, add to `/etc/default/grub`:

```bash
# Intel
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_iommu=on iommu=pt"

# AMD
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amd_iommu=on iommu=pt"

sudo update-grub
sudo reboot
```

### System Requirements

- Ubuntu 22.04 LTS or 24.04 LTS (Desktop)
- 64-bit CPU with VT-x/AMD-V
- At minimum 4GB RAM (8GB+ recommended for running VMs)
- Adequate disk space for VM images (SSDs strongly preferred)

---

## 2. Installation

### Install the Full KVM/QEMU/libvirt Stack

```bash
sudo apt update
sudo apt install -y \
    qemu-system-x86 \
    qemu-utils \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils \
    virt-manager \
    ovmf \
    virtinst \
    libguestfs-tools \
    cloud-image-utils
```

**Package breakdown:**

| Package | Purpose |
|---|---|
| `qemu-system-x86` | KVM-accelerated QEMU hypervisor |
| `qemu-utils` | Tools like `qemu-img` for disk management |
| `libvirt-daemon-system` | libvirt daemon (manages VMs via API) |
| `libvirt-clients` | `virsh` CLI and other client tools |
| `bridge-utils` | Network bridge tools (`brctl`) |
| `virt-manager` | Graphical VM manager |
| `ovmf` | UEFI firmware for VMs (required for Secure Boot, GPU passthrough) |
| `virtinst` | `virt-install` CLI for VM creation |
| `libguestfs-tools` | Tools for inspecting/modifying VM disk images |
| `cloud-image-utils` | Tools for cloud-init images |

### Enable and Start the libvirt Daemon

```bash
sudo systemctl enable --now libvirtd
sudo systemctl status libvirtd
```

### Verify Installation

```bash
virsh version --daemon
# Should show libvirt version and QEMU version

kvm-ok
# "KVM acceleration can be used" = you're good
# If kvm-ok isn't found: sudo apt install cpu-checker
```

---

## 3. User & Group Configuration

By default, only root can manage VMs. Add your user to the appropriate groups.

```bash
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER

# Apply without logging out (for current session)
newgrp libvirt
```

Log out and back in to make the group membership permanent.

### Verify Group Membership

```bash
groups $USER
# Should show: ... libvirt kvm ...
```

### Session vs. System Connection

libvirt supports two connection URIs:

```bash
# System connection (manages system-wide VMs, requires group membership)
virsh -c qemu:///system list --all

# Session connection (user-space VMs, no root required, more limited)
virsh -c qemu:///session list --all
```

For infrastructure use, always use `qemu:///system`. Set it as the default in `~/.config/libvirt/libvirt.conf`:

```ini
uri_default = "qemu:///system"
```

---

## 4. Networking

libvirt provides several networking modes. The default NAT network is created automatically.

### Default NAT Network

```bash
# Check default network
virsh net-list --all

# Start default network if not active
virsh net-start default
virsh net-autostart default

# Inspect network details
virsh net-dumpxml default
```

The default network (`virbr0`) provides:
- NAT to the host's network
- DHCP for guests (192.168.122.x range)
- DNS resolution for guests
- No direct access from external hosts to VMs

### Bridged Networking (VMs on Your LAN)

A bridged network puts VMs directly on your physical LAN — they get IPs from your router's DHCP and are reachable from other machines.

**Step 1: Identify your physical interface**

```bash
ip link show
# Note your NIC name: e.g., enp3s0, eth0, eno1
```

**Step 2: Create a bridge with Netplan (Ubuntu 22.04+)**

Edit `/etc/netplan/01-bridge.yaml`:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp3s0]
      dhcp4: yes
      parameters:
        stp: false
        forward-delay: 0
```

```bash
sudo netplan apply
ip addr show br0
```

**Step 3: Define bridge network in libvirt**

Create `bridge-network.xml`:

```xml
<network>
  <name>bridge-net</name>
  <forward mode="bridge"/>
  <bridge name="br0"/>
</network>
```

```bash
virsh net-define bridge-network.xml
virsh net-start bridge-net
virsh net-autostart bridge-net
```

### Isolated Network (VM-to-VM Only)

```xml
<network>
  <name>isolated</name>
  <bridge name="virbr1" stp="on" delay="0"/>
  <ip address="10.10.10.1" netmask="255.255.255.0">
    <dhcp>
      <range start="10.10.10.2" end="10.10.10.254"/>
    </dhcp>
  </ip>
</network>
```

```bash
virsh net-define isolated.xml
virsh net-start isolated
virsh net-autostart isolated
```

### Static DHCP Leases (Reserve IPs for VMs)

```bash
# Get VM's MAC address
virsh dumpxml myvm | grep 'mac address'

# Add static lease
virsh net-update default add ip-dhcp-host \
  "<host mac='52:54:00:XX:XX:XX' name='myvm' ip='192.168.122.50'/>" \
  --live --config
```

---

## 5. Storage Pools & Disk Images

### Default Storage Pool

libvirt's default pool stores images in `/var/lib/libvirt/images/`.

```bash
virsh pool-list --all
virsh pool-info default
```

### Create a Custom Storage Pool

```bash
# Directory-based pool
virsh pool-define-as mypool dir --target /data/vms
virsh pool-build mypool
virsh pool-start mypool
virsh pool-autostart mypool
```

### Disk Image Formats

**qcow2** — recommended for most uses:
- Supports snapshots
- Supports compression
- Thin-provisioned (only uses space as needed)
- Copy-on-write

**raw** — best for performance:
- No overhead
- No snapshot support natively
- Full pre-allocated space

### Creating Disk Images with qemu-img

```bash
# Create a 50GB qcow2 image (thin-provisioned)
qemu-img create -f qcow2 /var/lib/libvirt/images/myvm.qcow2 50G

# Create a raw image (pre-allocated)
qemu-img create -f raw /var/lib/libvirt/images/myvm.raw 50G

# Convert between formats
qemu-img convert -f raw -O qcow2 input.raw output.qcow2
qemu-img convert -f qcow2 -O raw input.qcow2 output.raw

# Inspect an image
qemu-img info myvm.qcow2

# Resize an image (grow only; shrinking is risky)
qemu-img resize myvm.qcow2 +20G

# Check image integrity
qemu-img check myvm.qcow2
```

### LVM-based Storage (Better I/O Performance)

```bash
# Create a VG for VMs (replace /dev/sdb with your device)
sudo pvcreate /dev/sdb
sudo vgcreate vms-vg /dev/sdb

# Define LVM pool in libvirt
virsh pool-define-as lvm-pool logical \
  --source-name vms-vg \
  --target /dev/vms-vg
virsh pool-start lvm-pool
virsh pool-autostart lvm-pool

# Create an LV for a VM
virsh vol-create-as lvm-pool myvm-disk 50G
```

---

## 6. Creating & Managing VMs with virt-manager

`virt-manager` is the graphical frontend — the quickest way to get a VM running.

### Launch virt-manager

```bash
virt-manager
```

### Creating a New VM (GUI walkthrough)

1. Click **"Create a new virtual machine"** (top-left)
2. Select installation method:
   - **Local install media** — ISO file
   - **Network install** — HTTP/FTP URL
   - **Import existing disk image** — use a pre-existing qcow2/raw
3. Browse to your ISO and select the OS type (helps virt-manager tune defaults)
4. Allocate RAM and CPUs
5. Create or select disk storage
6. **Enable "Customize configuration before install"** — recommended to review settings
7. Click **Finish** → VM boots from ISO

### Key Customization Settings

In the "Customize" view before install:

- **Overview tab**: Set firmware to UEFI (if needed), set chipset to Q35 (modern VMs)
- **CPU tab**: Enable "Copy host CPU configuration" for best performance
- **Boot Options**: Set boot order, enable UEFI Secure Boot
- **Video**: Set to virtio (best performance) or QXL (for SPICE)
- **NIC**: Set to virtio for best network performance
- **Disk**: Set bus to virtio (fastest), cache to none or writeback

### VM Console Access

virt-manager provides a built-in VNC/SPICE console. For headless VMs, you can also use:

```bash
# Connect via serial console (if configured in guest)
virsh console myvm

# Disconnect from serial console
Ctrl + ]
```

---

## 7. Command-Line VM Management with virsh

`virsh` is the primary CLI for libvirt. Almost everything you can do in virt-manager is doable here.

### VM Lifecycle

```bash
# List VMs
virsh list           # running only
virsh list --all     # all VMs including stopped

# Start / Stop / Reboot
virsh start myvm
virsh shutdown myvm      # graceful (ACPI)
virsh destroy myvm       # forced off (like power cut)
virsh reboot myvm
virsh reset myvm         # hard reset

# Suspend / Resume
virsh suspend myvm
virsh resume myvm

# Delete a VM (removes definition; does NOT delete disk images)
virsh undefine myvm

# Delete VM and its storage volumes
virsh undefine --nvram myvm --remove-all-storage
```

### Autostart

```bash
virsh autostart myvm           # enable autostart on host boot
virsh autostart --disable myvm # disable
```

### VM Configuration

```bash
# Dump full XML config
virsh dumpxml myvm

# Edit VM XML config (opens in $EDITOR)
virsh edit myvm

# Set vCPUs (while VM is stopped)
virsh setvcpus myvm 4 --config --maximum
virsh setvcpus myvm 4 --config

# Set RAM (in kibibytes)
virsh setmaxmem myvm 8388608 --config   # 8GB max
virsh setmem myvm 8388608 --config      # 8GB current
```

### Attaching and Detaching Devices

```bash
# Attach a disk image to running VM
virsh attach-disk myvm /var/lib/libvirt/images/extra.qcow2 vdb \
  --driver qemu --subdriver qcow2 --live --config

# Detach disk
virsh detach-disk myvm vdb --live --config

# Attach a USB device (by vendor:product)
virsh attach-device myvm usb-device.xml --live

# Eject/change CD-ROM
virsh change-media myvm sda /path/to/new.iso --live
virsh change-media myvm sda --eject --live
```

### Monitoring VM Resources

```bash
# CPU/memory stats
virsh domstats myvm
virsh cpu-stats myvm

# Disk I/O stats
virsh domblkstat myvm vda

# Network stats
virsh domifstat myvm vnet0

# Top-like view across all VMs
virt-top
```

### Virsh Snapshots

```bash
# Create snapshot
virsh snapshot-create-as myvm snap1 "Before update" --disk-only --atomic

# List snapshots
virsh snapshot-list myvm

# Revert to snapshot
virsh snapshot-revert myvm snap1

# Delete snapshot
virsh snapshot-delete myvm snap1
```

---

## 8. Creating VMs with virt-install

`virt-install` lets you script VM creation without the GUI.

### Basic VM from ISO

```bash
virt-install \
  --name ubuntu-server \
  --ram 4096 \
  --vcpus 2 \
  --disk path=/var/lib/libvirt/images/ubuntu-server.qcow2,size=40,format=qcow2,bus=virtio \
  --cdrom /home/user/iso/ubuntu-22.04-server.iso \
  --os-variant ubuntu22.04 \
  --network network=default,model=virtio \
  --graphics spice \
  --video qxl \
  --boot uefi \
  --noautoconsole
```

### VM from Existing Disk Image

```bash
virt-install \
  --name myvm \
  --ram 2048 \
  --vcpus 2 \
  --disk path=/var/lib/libvirt/images/existing.qcow2,format=qcow2,bus=virtio \
  --import \
  --os-variant linux2022 \
  --network network=default,model=virtio \
  --noautoconsole
```

### List Available OS Variants

```bash
osinfo-query os | grep -i ubuntu
osinfo-query os | grep -i rhel
```

### Useful virt-install Options

```bash
--cpu host-passthrough       # Pass host CPU features to guest
--hugepages                  # Use hugepages for memory
--memorybacking hugepages=on
--numatune 0                 # Pin to NUMA node 0
--disk cache=none            # Safest for data integrity
--disk cache=writeback       # Better performance (with UPS)
--network bridge=br0         # Use bridged network
--console pty,target_type=serial  # Enable serial console
--extra-args 'console=ttyS0,115200'  # Kernel args for serial
```

---

## 9. QEMU Directly (Without libvirt)

For maximum control or quick testing, you can invoke QEMU directly without libvirt.

### Basic QEMU Launch

```bash
qemu-system-x86_64 \
  -name "test-vm" \
  -machine type=q35,accel=kvm \
  -cpu host \
  -m 2048 \
  -smp 2 \
  -drive file=/var/lib/libvirt/images/test.qcow2,format=qcow2,if=virtio \
  -cdrom /path/to/install.iso \
  -boot order=dc \
  -netdev user,id=net0 \
  -device virtio-net-pci,netdev=net0 \
  -display sdl \
  -vga virtio
```

### Headless QEMU with VNC

```bash
qemu-system-x86_64 \
  -name "headless-vm" \
  -machine type=q35,accel=kvm \
  -cpu host \
  -m 4096 \
  -smp 4 \
  -drive file=/var/lib/libvirt/images/vm.qcow2,format=qcow2,if=virtio,cache=none \
  -netdev bridge,id=net0,br=virbr0 \
  -device virtio-net-pci,netdev=net0 \
  -display vnc=:0 \
  -daemonize \
  -pidfile /tmp/myvm.pid
```

Connect with: `vncviewer localhost:5900`

### QEMU with UEFI

```bash
qemu-system-x86_64 \
  -machine type=q35,accel=kvm \
  -cpu host \
  -m 2048 \
  -drive if=pflash,format=raw,unit=0,readonly=on,file=/usr/share/OVMF/OVMF_CODE.fd \
  -drive if=pflash,format=raw,unit=1,file=/tmp/OVMF_VARS.fd \
  -drive file=vm.qcow2,format=qcow2,if=virtio \
  ...
```

### Useful QEMU Runtime Commands (QEMU Monitor)

Press `Ctrl+Alt+2` in the QEMU window to access the monitor, or connect via socket:

```bash
# Launch with monitor socket
-monitor unix:/tmp/qemu-monitor.sock,server,nowait

# Connect to monitor
socat - UNIX-CONNECT:/tmp/qemu-monitor.sock

# Monitor commands
(qemu) info status
(qemu) info block
(qemu) savevm snap1
(qemu) loadvm snap1
(qemu) system_powerdown
(qemu) quit
```

---

## 10. Snapshots & Cloning

### Internal Snapshots (qcow2 only)

Stored inside the qcow2 file. VM must be shut down (or suspended) for consistent state.

```bash
# Via virsh (recommended)
virsh snapshot-create-as myvm \
  --name "pre-upgrade" \
  --description "Before OS upgrade" \
  --atomic

# Revert
virsh snapshot-revert myvm pre-upgrade

# List
virsh snapshot-list myvm --tree

# Delete
virsh snapshot-delete myvm pre-upgrade
```

### External Snapshots (Disk-Only)

Creates a new overlay file; original becomes read-only backing. Supports running VMs.

```bash
virsh snapshot-create-as myvm snap1 \
  --disk-only \
  --diskspec vda,snapshot=external,file=/var/lib/libvirt/images/myvm-snap1.qcow2 \
  --atomic
```

### Merging External Snapshots (Blockcommit)

```bash
# Commit changes back to base image and pivot back to base
virsh blockcommit myvm vda --active --verbose --pivot
```

### Cloning VMs

```bash
# Clone a shut-down VM
virt-clone \
  --original myvm \
  --name myvm-clone \
  --auto-clone

# Clone with specific disk path
virt-clone \
  --original myvm \
  --name myvm-clone \
  --file /var/lib/libvirt/images/myvm-clone.qcow2
```

### Manual Disk Cloning with qemu-img

```bash
# Create a full copy
qemu-img convert -f qcow2 -O qcow2 source.qcow2 dest.qcow2

# Create a linked clone (thin, uses source as backing)
qemu-img create -f qcow2 -b source.qcow2 -F qcow2 linked-clone.qcow2
```

---

## 11. Performance Tuning

### CPU Tuning

```bash
# Use host-passthrough for best performance
# In virt-manager: CPU > Copy host CPU configuration
# Or in XML:
<cpu mode='host-passthrough' check='none'>
  <topology sockets='1' cores='4' threads='2'/>
</cpu>
```

**CPU pinning** (pin vCPUs to specific physical CPUs, eliminates NUMA migrations):

```xml
<vcpupin vcpu='0' cpuset='2'/>
<vcpupin vcpu='1' cpuset='3'/>
<vcpupin vcpu='2' cpuset='6'/>
<vcpupin vcpu='3' cpuset='7'/>
<emulatorpin cpuset='0-1'/>
```

Check NUMA topology first:

```bash
numactl -H
lstopo
```

### Memory Tuning

**Hugepages** dramatically reduce TLB misses for large VMs:

```bash
# Check available hugepages
cat /proc/meminfo | grep Huge

# Allocate hugepages at runtime (not persistent)
echo 2048 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

# Persistent allocation via /etc/sysctl.conf
vm.nr_hugepages = 2048

# Mount hugetlbfs if not already
sudo mount -t hugetlbfs -o pagesize=2M none /dev/hugepages
```

In libvirt XML:

```xml
<memoryBacking>
  <hugepages>
    <page size='2048' unit='KiB'/>
  </hugepages>
  <nosharepages/>
  <locked/>
</memoryBacking>
```

### Disk I/O Tuning

```bash
# cache=none: safest, bypasses host cache (good for databases)
# cache=writeback: faster, uses host cache
# cache=unsafe: fastest, ignore fsync (never for production)

# io=native: use Linux AIO (requires cache=none)
# io=threads: thread-based async I/O
```

In XML:

```xml
<disk type='file' device='disk'>
  <driver name='qemu' type='qcow2' cache='none' io='native' discard='unmap'/>
  ...
</disk>
```

Enable `discard=unmap` to allow TRIM/UNMAP so the host can reclaim freed qcow2 space.

### Network Tuning

Always use `virtio` network model. For multi-queue (high-throughput):

```xml
<interface type='network'>
  <source network='default'/>
  <model type='virtio'/>
  <driver name='vhost' queues='4'/>
</interface>
```

Enable multi-queue inside the guest:

```bash
sudo ethtool -L eth0 combined 4
```

### Balloon Driver (Dynamic Memory)

The balloon driver lets the host reclaim unused guest memory:

```xml
<memballoon model='virtio'>
  <stats period='10'/>
</memballoon>
```

Monitor from host:

```bash
virsh dommemstat myvm
```

---

## 12. GPU Passthrough (VFIO)

Pass a physical GPU directly to a VM for near-native performance (gaming, CUDA, ML workloads).

### Requirements

- Two GPUs (or integrated + discrete): one for host display, one to pass through
- IOMMU enabled (see Section 1)
- GPU in its own IOMMU group (or ACS patch if not)

### Step 1: Check IOMMU Groups

```bash
#!/bin/bash
for d in /sys/kernel/iommu_groups/*/devices/*; do
  n=${d#*/iommu_groups/*}; n=${n%%/*}
  printf 'IOMMU Group %s ' "$n"
  lspci -nns "${d##*/}"
done
```

Your GPU and its audio function should be in the same IOMMU group, ideally alone.

### Step 2: Get GPU PCI IDs

```bash
lspci -nn | grep -E 'VGA|Audio'
# Example output:
# 01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP104 [GeForce GTX 1080] [10de:1b80]
# 01:00.1 Audio device [0403]: NVIDIA Corporation GP104 High Definition Audio Controller [10de:10f0]
```

Note the IDs in brackets: `10de:1b80` and `10de:10f0`.

### Step 3: Bind GPU to VFIO at Boot

Add to `/etc/modprobe.d/vfio.conf`:

```
options vfio-pci ids=10de:1b80,10de:10f0
softdep nvidia pre: vfio-pci
```

Add to `/etc/modules`:

```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

Update initramfs:

```bash
sudo update-initramfs -u
sudo reboot
```

### Step 4: Verify VFIO Binding

```bash
lspci -nnk -d 10de:1b80
# Should show "Kernel driver in use: vfio-pci"
```

### Step 5: Add GPU to VM

In virt-manager: Add Hardware > PCI Host Device > select your GPU and its audio device.

Or in XML:

```xml
<hostdev mode='subsystem' type='pci' managed='yes'>
  <source>
    <address domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
  </source>
</hostdev>
<hostdev mode='subsystem' type='pci' managed='yes'>
  <source>
    <address domain='0x0000' bus='0x01' slot='0x00' function='0x1'/>
  </source>
</hostdev>
```

The VM will need a display output connected to the passed-through GPU.

---

## 13. Cloud Images & cloud-init

Cloud images are pre-built OS images designed for VMs — no installer needed. cloud-init handles first-boot configuration (users, SSH keys, packages, etc.).

### Download Ubuntu Cloud Image

```bash
wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
```

### Create a VM Disk from Cloud Image

```bash
# Create a working copy (don't modify the base)
qemu-img create -f qcow2 \
  -b jammy-server-cloudimg-amd64.img \
  -F qcow2 \
  /var/lib/libvirt/images/my-ubuntu.qcow2 \
  20G
```

### Create cloud-init Config

**user-data:**

```yaml
#cloud-config
hostname: my-ubuntu
manage_etc_hosts: true

users:
  - name: brian
    groups: sudo
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh_authorized_keys:
      - ssh-ed25519 AAAA... your-public-key

package_update: true
packages:
  - qemu-guest-agent
  - htop

runcmd:
  - systemctl enable --now qemu-guest-agent
```

**meta-data:**

```yaml
instance-id: my-ubuntu-01
local-hostname: my-ubuntu
```

### Build cloud-init ISO

```bash
cloud-localds /var/lib/libvirt/images/my-ubuntu-seed.iso user-data meta-data
```

### Boot VM with cloud-init

```bash
virt-install \
  --name my-ubuntu \
  --ram 2048 \
  --vcpus 2 \
  --disk path=/var/lib/libvirt/images/my-ubuntu.qcow2,format=qcow2,bus=virtio \
  --disk path=/var/lib/libvirt/images/my-ubuntu-seed.iso,device=cdrom \
  --os-variant ubuntu22.04 \
  --network network=default,model=virtio \
  --import \
  --noautoconsole
```

After first boot, cloud-init runs, then you can eject and remove the seed ISO:

```bash
virsh change-media my-ubuntu sda --eject --config
```

---

## 14. Automation with Terraform + libvirt

The `terraform-provider-libvirt` lets you define VMs as code.

### Install Terraform

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

### Example Terraform Configuration

**main.tf:**

```hcl
terraform {
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"
      version = "~> 0.7"
    }
  }
}

provider "libvirt" {
  uri = "qemu:///system"
}

# Base image pool
resource "libvirt_pool" "vms" {
  name = "vms"
  type = "dir"
  path = "/var/lib/libvirt/images/terraform"
}

# Base cloud image volume
resource "libvirt_volume" "ubuntu_base" {
  name   = "ubuntu-22.04-base.qcow2"
  pool   = libvirt_pool.vms.name
  source = "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img"
  format = "qcow2"
}

# Per-VM disk (thin clone of base)
resource "libvirt_volume" "vm_disk" {
  count          = var.vm_count
  name           = "vm-${count.index}.qcow2"
  pool           = libvirt_pool.vms.name
  base_volume_id = libvirt_volume.ubuntu_base.id
  size           = 21474836480  # 20GB in bytes
}

# cloud-init config
data "template_file" "user_data" {
  count    = var.vm_count
  template = file("${path.module}/user-data.tpl")
  vars = {
    hostname = "vm-${count.index}"
    ssh_key  = var.ssh_public_key
  }
}

resource "libvirt_cloudinit_disk" "init" {
  count     = var.vm_count
  name      = "init-${count.index}.iso"
  pool      = libvirt_pool.vms.name
  user_data = data.template_file.user_data[count.index].rendered
}

resource "libvirt_domain" "vm" {
  count  = var.vm_count
  name   = "vm-${count.index}"
  memory = "2048"
  vcpu   = 2

  cloudinit = libvirt_cloudinit_disk.init[count.index].id

  network_interface {
    network_name   = "default"
    wait_for_lease = true
  }

  disk {
    volume_id = libvirt_volume.vm_disk[count.index].id
    scsi      = true
  }

  cpu {
    mode = "host-passthrough"
  }
}

output "vm_ips" {
  value = [for vm in libvirt_domain.vm : vm.network_interface[0].addresses[0]]
}
```

**variables.tf:**

```hcl
variable "vm_count" {
  default = 3
}

variable "ssh_public_key" {
  type = string
}
```

```bash
terraform init
terraform plan
terraform apply -var='ssh_public_key=ssh-ed25519 AAAA...'
terraform destroy
```

---

## 15. Monitoring & Troubleshooting

### QEMU Guest Agent

The guest agent enables host-to-guest communication (IP discovery, consistent snapshots, etc.).

Install in guest:

```bash
# Debian/Ubuntu
sudo apt install qemu-guest-agent
sudo systemctl enable --now qemu-guest-agent

# RHEL/Rocky
sudo dnf install qemu-guest-agent
sudo systemctl enable --now qemu-guest-agent
```

Add channel to VM XML (if not already present):

```xml
<channel type='unix'>
  <target type='virtio' name='org.qemu.guest_agent.0'/>
</channel>
```

Use from host:

```bash
virsh qemu-agent-command myvm '{"execute":"guest-info"}'
virsh domifaddr myvm --source agent    # get IPs via agent
virsh snapshot-create-as myvm snap1 --quiesce  # filesystem-consistent snapshot
```

### Useful Diagnostic Commands

```bash
# Check VM logs
sudo journalctl -u libvirtd
sudo cat /var/log/libvirt/qemu/myvm.log

# See all active QEMU processes
ps aux | grep qemu

# Check open file handles for a VM
sudo ls -la /proc/$(pgrep -f 'qemu.*myvm')/fd

# Network diagnostics
ip link show type bridge
bridge link show
iptables -t nat -L -n -v   # Check NAT rules for default network

# Storage diagnostics
virsh vol-list default
virsh pool-refresh default
qemu-img check /var/lib/libvirt/images/myvm.qcow2

# Performance: Check if KVM is actually being used
virsh dominfo myvm | grep "CPU time"
# Or check /proc for kvm usage
cat /sys/module/kvm/parameters/enable_vmware_backdoor
```

### Common Issues & Fixes

**"Failed to connect to socket /var/run/libvirt/libvirt-sock"**

```bash
sudo systemctl start libvirtd
# Or check group:
groups $USER | grep libvirt
```

**"Error starting domain: internal error: ... network 'default' is not active"**

```bash
virsh net-start default
virsh net-autostart default
```

**"Cannot access storage file (as uid:X gid:X)"**

```bash
# Check apparmor
sudo aa-status
# Fix ownership
sudo chown libvirt-qemu:kvm /path/to/image.qcow2
```

**VM very slow / KVM not being used**

```bash
virsh dominfo myvm | grep "Emulated machine"
# Confirm KVM acceleration:
virsh capabilities | grep kvm
```

**High steal time in guest**

CPU is being starved. Reduce VM count or use CPU pinning.

---

## 16. Security Considerations

### AppArmor

Ubuntu enables AppArmor profiles for libvirt by default. If a VM fails to access a file, AppArmor may be blocking it.

```bash
# Check AppArmor denials
sudo dmesg | grep -i apparmor
sudo aa-status | grep libvirt

# Add a custom path to the libvirt profile
echo '/data/vms/** rwk,' | sudo tee -a /etc/apparmor.d/abstractions/libvirt-qemu
sudo systemctl reload apparmor
```

### SELinux (if using RHEL-based guests or custom kernels)

Not default on Ubuntu, but relevant if you migrate configs from RHEL:

```bash
# Check SELinux context on disk images
ls -lZ /var/lib/libvirt/images/
# Correct context should be: svirt_image_t

# Restore correct context
sudo restorecon -Rv /var/lib/libvirt/images/
```

### Network Isolation

- Prefer isolated networks for dev/test VMs
- Use firewall rules on `virbr0` to limit what VMs can reach
- Disable the default network if you don't need NAT

```bash
# Drop forwarding from default network to internet (example)
sudo iptables -I FORWARD -i virbr0 -o enp3s0 -j DROP
```

### Secure VNC/SPICE Consoles

Always tunnel VNC over SSH rather than exposing to the network:

```bash
# Local tunnel example
ssh -L 5900:localhost:5900 user@hypervisor-host
# Then connect VNC to localhost:5900
```

Or use SPICE with TLS in the VM XML:

```xml
<graphics type='spice' port='-1' tlsPort='-1' autoport='yes'>
  <listen type='address' address='127.0.0.1'/>
  <image compression='auto_glz'/>
</graphics>
```

### Limit VM Privileges

Ensure VMs run as the `libvirt-qemu` user (default). Never run as root:

```bash
ps aux | grep qemu
# Should show: libvirt-qemu   (not root)
```

---

## Quick Reference Cheat Sheet

```bash
# List all VMs
virsh list --all

# Start / stop
virsh start <vm>
virsh shutdown <vm>
virsh destroy <vm>        # force off

# Get VM IP
virsh domifaddr <vm>
virsh domifaddr <vm> --source agent

# Snapshot
virsh snapshot-create-as <vm> <name> --atomic
virsh snapshot-revert <vm> <name>
virsh snapshot-list <vm>

# Edit config
virsh edit <vm>

# Clone
virt-clone --original <vm> --name <clone> --auto-clone

# Create disk
qemu-img create -f qcow2 /path/to/disk.qcow2 50G

# Inspect disk
qemu-img info disk.qcow2

# Convert disk
qemu-img convert -f qcow2 -O raw src.qcow2 dst.raw

# Network
virsh net-list --all
virsh net-start default
virsh net-dumpxml default

# Storage pools
virsh pool-list --all
virsh pool-refresh default
virsh vol-list default

# Logs
sudo journalctl -u libvirtd -f
sudo tail -f /var/log/libvirt/qemu/<vm>.log
```

---

*Tutorial covers KVM/QEMU with libvirt on Ubuntu 22.04/24.04 LTS. Tested configurations reflect common infrastructure use cases including bridged networking, storage management, performance tuning, and cloud-image automation.*
