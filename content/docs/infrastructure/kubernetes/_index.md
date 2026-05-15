---
bookCollapseSection: false
weight: 4
title: "Kubernetes"
---

{{< hint info >}}
An interactive Kubernetes tutorial covering cluster architecture, core resources, networking, storage, RBAC, and debugging — with hands-on YAML examples and quizzes.
{{< /hint >}}

## Interactive Tutorial

The tutorial runs as a full-page interactive app. Use the sidebar inside it to navigate between the 10 modules.

{{< rawhtml >}}
<iframe
  src="/k8s-tutorial.html"
  style="width:100%; height:90vh; border:none; border-radius:4px; display:block;"
  title="Kubernetes Tutorial"
></iframe>
{{< /rawhtml >}}

---

**Can't see the tutorial above?** Open it directly: [k8s-tutorial.html](/k8s-tutorial.html)

## Modules

| # | Module | Topics |
|---|--------|--------|
| 01 | What is Kubernetes? | Container orchestration, declarative model, K8s vs Docker |
| 02 | Cluster Architecture | API server, etcd, scheduler, kubelet, reconciliation loop |
| 03 | Lab Setup | k3s install, kubectl config, bash completion |
| 04 | Pods | Manifests, health probes, liveness/readiness/startup |
| 05 | Deployments & Rollouts | Rolling updates, rollbacks, HPA autoscaling |
| 06 | Services & Networking | ClusterIP, NodePort, LoadBalancer, Ingress, CoreDNS |
| 07 | ConfigMaps & Secrets | Env injection, volume mounts, encryption at rest |
| 08 | Persistent Storage | PV, PVC, StorageClass, access modes |
| 09 | RBAC & Security | Roles, ClusterRoles, bindings, `auth can-i` |
| 10 | Observability & Debugging | Triage workflow, failure states, `kubectl top` |
