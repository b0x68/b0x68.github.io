# Tech Tutorial: Manage Containers with Persistent Storage on RHEL

## Introduction

In this tutorial, we will explore how to attach persistent storage to a container, a crucial skill for the Red Hat Certified System Administrator (RHCSA) exam. Persistent storage is essential in containerized environments because, by default, containers are ephemeral. This means that any data written to the container's writable layer is lost when the container is deleted. Persistent storage solves this by enabling data to be stored in a way that survives independently of the container's lifecycle.

We will focus on using Podman, the container management platform available in Red Hat Enterprise Linux (RHEL), which is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System.

## Prerequisites

- A running RHEL 8.x system.
- Podman installed. Starting from RHEL 8, Podman is included by default.
- Basic familiarity with command-line interface and containerization concepts.

## Step-by-Step Guide

### Step 1: Setting Up the Environment

Before attaching storage, ensure that Podman is installed and running correctly on your system. You can check the version of Podman installed by running:

```bash
podman --version
```

### Step 2: Creating a Persistent Volume

For demonstration purposes, we will use a local directory on the host as a persistent volume. In a production environment, you might use more complex solutions like NFS, iSCSI, or cloud-provided storage solutions.

First, create a directory on the host:

```bash
sudo mkdir -p /mydata/persistent-volume
```

### Step 3: Running a Container with Persistent Storage

We will run a PostgreSQL container as an example, mounting our previously created directory as a volume in the container. This setup ensures that the database data persists across container restarts and deletions.

1. Pull the official PostgreSQL image:

```bash
podman pull postgres
```

2. Start the PostgreSQL container with the volume attached:

```bash
podman run -d \
    --name my-postgres-container \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -v /mydata/persistent-volume:/var/lib/postgresql/data \
    postgres
```

In this command:
- `-d` runs the container in detached mode.
- `--name` assigns a name to the container for easier management.
- `-e` sets environment variables in the container; `POSTGRES_PASSWORD` is required to set the default password.
- `-v` mounts the host directory `/mydata/persistent-volume` to `/var/lib/postgresql/data` inside the container.

### Step 4: Verify the Data Persistence

To test data persistence, follow these steps:

1. Access the PostgreSQL command line:

```bash
podman exec -it my-postgres-container psql -U postgres
```

2. Create a sample database:

```sql
CREATE DATABASE testdb;
```

3. List databases to verify it was created:

```sql
\l
```

4. Exit PostgreSQL and stop the container:

```bash
\q
podman stop my-postgres-container
```

5. Remove the container:

```bash
podman rm my-postgres-container
```

6. Restart the container using the same command from Step 3. Then, access PostgreSQL and list databases to ensure `testdb` is still there.

## Conclusion

In this tutorial, you learned how to attach persistent storage to a container using Podman in RHEL, ensuring that data remains safe across container lifecycle events. This skill is vital for deploying stateful applications in containers and is essential for the Red Hat Certified System Administrator (RHCSA) exam.

Understanding how to manage storage effectively allows you to leverage the power of containerization without sacrificing the data persistence required by most production applications. Remember to explore further storage options like NFS or cloud storage integrations for more complex scenarios.