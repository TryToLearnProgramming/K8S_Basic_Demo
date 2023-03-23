WHAT IS A DEPLOYMENT ?
https://www.containiq.com/post/statefulset-vs-deployment#:~:text=A%20Deployment%20manages%20multiple%20pods,and%20uniqueness%20of%20pod%20replicas.

A Deployment is a Kubernetes resource object that provides declarative updates for pods that encapsulate application containers. A Deployment represents a number of identical pods without unique IDs, while specifying the pods’ desired state and attributes. Deployments are typically used to autoscale the number of pod replicas, perform controlled rollouts for application code, and perform rollbacks when necessary.

Kubernetes administrators rely on Deployments to manage a containerized application’s lifecycle by defining the number of pods to be deployed, the image to be used for the application, and how to perform code updates. Kubernetes deployments help automate repeatable application updates, subsequently reducing the effort, time, and number of errors associated with manual updates.

Components of a Kubernetes Deployment
The primary components used to create and apply a Deployment to a cluster include:

Deployment template: This is a JSON or YAML configuration file that is used to define the Deployment’s configuration specification. The Kubernetes Deployment controller relies on the desired state described in the Deployment template to create, update, and scale pods. The JSON or YAML file is static, and it includes a pod template that defines what each pod should look like, as well as other common parameters, such as:
- Number of pod replicas
- Name of the image running in the pods
- Deployment’s image tag
- Secrets, ConfigMaps, and other settings injected into the pod
- Service labels
Service: Defines a single endpoint that is used to enable network access and expose workloads running on the pods within the Deployment. A service is a REST object that points to the Deployment pods and includes a policy to access them.
Persistent Volume: Allows pods within the Deployment to access a portion of node storage to store data.

<<<<<<<<<<<<--------------- HERE ARE THE Deployment Configaration Manifest


Scaling Deployments
The ‘kubect’l command can also be used to scale the number of pods with changing patterns of an application load. To increase the number of pods for darwin-deployment to 5, run the command:

=> kubectl scale deployment/darwin-deployment --replicas=5

Kubernetes Deployment Strategies: 

Kubernetes supports multiple rollout strategies for pod deployments. These include:

Recreate: Simultaneously terminates and replaces all pods running the old version of the application with new pods.
Ramped: Rolls out new application versions while terminating the old pods.
Rolling update: Replaces old pods with new ones, one-by-one, with zero downtime.
Canary deployment: Replaces a subset of existing pods with new ones, keeping both versions running, and then rolls out the new version to more pods if the test deployment is a success.