+++
title = "Build a container from a Containerfile"
date = "2024-02-16T11:54:36-05:00"
author = "root"
cover = "drphil.gif"
tags = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
keywords = ["RHCSA", "Red Hat", "System Administrator", "Linux", "Sysadmin", "Tutorial", "Exam 200" ]
description = "How to build a container using a Containerfile for the Red Hat Certified Systems Administrator Exam 200 Objective."
showFullContent = false
readingTime = true
hideComments = false
color = "" #color from the theme settings
+++


# Introduction to Building Containers with Containerfiles

In this tutorial, we will be discussing how to build a container using a Containerfile for the Red Hat Certified Systems Administrator Exam 200 Objective. Building containers has become a popular method for simplifying application deployments and providing consistent environments, making it an important skill for system administrators. We will go into great depth to ensure you have a thorough understanding of the steps involved and the components that make up a Containerfile.

## What is a Containerfile?

A Containerfile is a text file that contains instructions for building a container image. It is similar to a Dockerfile, but is used specifically for building containers with Red Hat's OpenShift Kubernetes platform. The Containerfile specifies the base image, software packages, and configurations needed to create the container.

## Prerequisites

Before we begin, ensure that you have the following:

- A system running RHEL or CentOS with Red Hat's OpenShift Kubernetes platform installed
- Basic knowledge of the command line interface (CLI)
- Familiarity with Docker and container concepts

Now, let's dive into the steps for building a container from a Containerfile.

## Step 1: Create a New Directory

First, we need to create a new directory for our Containerfile and the necessary files. This directory will act as our workspace for building the container. To create a directory called "mycontainer", use the following command:

```
mkdir mycontainer
```

## Step 2: Create a Containerfile

Next, we need to create the actual Containerfile. This file will contain the instructions for building our container image. Open your preferred text editor and enter the following:

```
FROM centos:7
RUN yum install -y httpd
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
```

Let's break down what each line is doing:

- `FROM`: This specifies the base image for our container. In this case, we are using the CentOS 7 image.
- `RUN`: This line runs a command inside the container. In this case, we are installing the Apache HTTP server package.
- `CMD`: This line specifies the command that should be run when the container is launched. Here, we are starting the HTTP server in the foreground.

Save the file as "Containerfile" in the "mycontainer" directory.

## Step 3: Add Additional Configuration (Optional)

You can also add additional configuration to your Containerfile, such as copying files or setting environment variables. For example, if you want to include an HTML file for your website, you can add the following line to your Containerfile:

```
COPY index.html /var/www/html/
```

This will copy the "index.html" file from your current directory to the virtual location where Apache will look for website files.

## Step 4: Build the Container Image

Now, we are ready to build our container image using the Containerfile we created. In your terminal, navigate to the "mycontainer" directory and run the following command:

```
oc create build -t mycontainer .
```

This will use the Containerfile in the current directory and build an image called "mycontainer". The build process may take a few minutes to complete.

## Step 5: Verify the Container Image

Once the build process is complete, we can verify that our container image was successfully built. Use the following command to view all the images in our local registry:

```
oc get images
```

You should see your "mycontainer" image listed among the others.

## Step 6: Launch the Container

Now that our container image is built, we can launch it as a running container. Use the following command to create a container from our "mycontainer" image:

```
oc run mycontainer --image=mycontainer --restart=Never
```

This will create a running container called "mycontainer" using our new image. Confirm that the container is running by checking its status:

```
oc get pods
```

You should see your "mycontainer" pod listed with a "Running" status.

## Step 7: Access the Application

Finally, we can access our application running inside the container by exposing it as a service. Use the following command to expose the container port and create a corresponding service:

```
oc expose pod mycontainer --port=80
```

Now, you can access the application by using the exposed service's URL. To find the URL, use the following command:

```
oc get route
```

You should see the service URL listed under the "HOST/PORT" column. Access this URL in your browser, and you should see your web application running.

## Conclusion

Congratulations! You have successfully built a container using a Containerfile. In this tutorial, we covered the step-by-step process for creating a Containerfile, building a container image, and launching a container using that image. Keep practicing and experimenting with different configurations to become comfortable with building containers for your applications. Remember, building containers is a sought-after skill for system administrators, making mastering it a valuable addition to your skillset. 
