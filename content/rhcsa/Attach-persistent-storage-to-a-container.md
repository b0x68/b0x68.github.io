+++
title = "Attach persistent storage to a container"
date = "2024-02-16T10:40:09-05:00"
author = "root"
cover = ""
tags = ["container"", "container:", ""persistentvolumeclaim":", ""volumemounts":", "command", ""containers":", "container", ""myimage","]
keywords = [""/mount/path",", "--image=myimage", ""volumes":", "volume", ""image":", "container.", "systems", ""myimage","]
description = ""
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Tutorial: Attaching Persistent Storage to a Container

In this tutorial, we will learn how to attach persistent storage to a container in Red Hat Certified Systems Administrator Exam 200. Persistent storage is used to store data that needs to be accessed by a container even if the container is restarted or recreated.

We will cover the following topics:

1. Understanding persistent storage
2. Creating a persistent volume
3. Attaching persistent storage to a container
4. Verifying successful attachment

## Understanding Persistent Storage

Persistent storage is a form of storage that is designed to retain data even when the container that uses it is stopped or deleted. This is different from volatile storage, which only stores data while the container is running.

Managing persistent storage is important for applications that require data persistence, such as databases or file servers. In a container environment, persistent storage can be attached to a container as a shared volume, allowing multiple containers to access the same data.

## Creating a Persistent Volume

Before we can attach persistent storage to a container, we need to create a persistent volume. A persistent volume is a part of storage that is independent from any individual container, making it accessible to any container within the cluster.

To create a persistent volume, follow these steps:

1. Log into your Red Hat server and open the command line interface.
2. Use the `oc` command to create a persistent volume, specifying the storage size, access mode, and storage type.
```
oc create -f my_pv.yaml
```
3. The YAML file should have the following structure:
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi # Change this value according to your storage needs
  accessModes: 
    - ReadWriteOnce # Change this value according to your access mode preferences
  persistentVolumeReclaimPolicy: Retain
  nfs:
    path: /path/to/data # Change this value to the path where you want to store the data for this persistent volume
    server: <nfs-server-address> # Change this value to the address of your NFS server
```
4. Save the file and wait for the persistent volume to be created.

## Attaching Persistent Storage to a Container

Now that we have created our persistent volume, we can attach it to a container. To do this, we will use a persistent volume claim, which is a request for a specific persistent volume to be attached to our container.

Follow these steps to attach persistent storage to a container:

1. Start your container using the `oc run` command and specifying the persistent volume claim name.
```
oc run my-container --image=myimage --restart=Always --overrides='{ "apiVersion": "v1", "spec": { "volumes": [ { "name": "mypvlclaim", "persistentVolumeClaim": { "claimName": "my-pvc" } } ], "containers": [ { "name": "my-container", "image": "myimage", "volumeMounts": [ { "mountPath": "/mount/path", "name": "mypvclaim" } ], "env": [ { "name": "MOUNT_DIR", "value": "/mount/path" } ] } ] } }'
```
2. The `MOUNT_DIR` environment variable specifies the directory within the container where you want to mount the persistent volume.
3. Save the changes and start the container.
4. Once the container is running, you can access the persistent storage through the mount directory specified in the `MOUNT_DIR` environment variable.

## Verifying Successful Attachment

To verify that persistent storage has been successfully attached to a container, follow these steps:

1. Log into your Red Hat server and open the command line interface.
2. Use the `oc` command to check the status of your container.
```
oc get pods
```
3. The output should show the status of your container as "Running".
4. Use the `oc` command to check the status of your persistent volume claim.
```
oc get pvc
```
5. The output should show the status of your persistent volume claim as "Bound".
6. Use the `oc` command to check the status of your persistent volume.
```
oc get pv
```
7. The output should show the status of your persistent volume as "Available" or "Claimed", indicating that it is successfully attached to your container.

Congratulations! You have successfully attached persistent storage to a container. This will ensure that your container can access the necessary data for your applications even if it is restarted or recreated.

In this tutorial, we covered the basics of persistent storage, creating a persistent volume, attaching it to a container, and verifying the successful attachment. You are now ready to confidently handle the "Attach persistent storage to a container" objective in the Red Hat Certified Systems Administrator Exam 200. 