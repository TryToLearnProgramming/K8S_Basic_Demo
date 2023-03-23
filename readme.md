WHAT IS A SETFULSET?
https://www.containiq.com/post/statefulset-vs-deployment#:~:text=A%20Deployment%20manages%20multiple%20pods,and%20uniqueness%20of%20pod%20replicas.

A StatefulSet is a Kubernetes resource object that manages a set of pods with unique identities. By assigning a persistent ID that is maintained even if the pod is rescheduled, a StatefulSet helps maintain the uniqueness and ordering of pods. With unique pod identifiers, administrators can efficiently attach cluster volumes to new pods across failures.
Although the StatefulSet controller deploys pods using similar specifications, pods are not interchangeable. As a StatefulSet does not create a ReplicaSet, the pod replicas cannot be rolled back to previous versions. StatefulSets are typically used for applications that require persistent storage for stateful workloads, and ordered, automated rolling updates.

Components of a Kubernetes StatefulSet Configuration Manifest
A Kubernetes StatefulSet configuration comprises the following:
StatefulSet: The template that defines pod selectors and replicas of containers that will run on the pods.
Headless service: The network domain controller that allows clients to connect with the pods using a DNS entry.
Volume claim template: The template specification that allows administrators to provision stateful storage using persistent volumes.


=======================================================
**********************When to Use**********************
=======================================================
A StatefulSet is better suited to stateful workloads that require persistent storage on each cluster node, such as databases and other identity-sensitive workloads. A Deployment, on the other hand, is suitable for stateless workloads that use multiple replicas of one pod, such as web servers like Nginx and Apache.

This practical scenario demonstrates how a StatefulSet differs from a Deployment:

Consider a web app that uses a relational database to store data. When traffic to the application increases, administrators intend to scale up the number of pods to support the workload. A straightforward approach is simply to change the replica count within the Deployment’s configuration manifest; then the Deployment controller will take care of scaling. Since new pod replicas are assigned the same set of ConfigMaps and environment variables when starting, they communicate with the backend the same way as the original pod, retaining the user experience for incoming traffic.

Similar to the web servers, the relational database may also need to be scaled up to meet the increased workload. Since the master and replica pods need to implement a leader-follower pattern, the pods of the database cannot be created or deleted randomly. In addition, while each pod needs to sync its data with the previous pod, it retains its own copy of the data stored. In such an instance, a StatefulSet helps create the database pods in an ordered sequence where every new pod acquires its copy of data from the last pod generated. If a pod fails, the StatefulSet controller automatically deploys new pod replicas incrementally with the same identity and attaches them to the same PVC.