# Day 1: Basics of Kubernetes

## What is Kubernetes
    - Definition: Open source container orchestration tool developed by google.
    - Use: Manages containerzed applicaitons, in different envionrments (physical, virtual, cloud, hybrid)
    - Offerings: High availablilty (little to no downtime), scalabililty (High performance, loads fast), Disaster recovery (data loss) backup and restoring for the latest state

## Key terms
    - Conductor: Runs the entire cluster, for scheduling tasks
    - Worker: Running application processes
    - Microservices: singular applications leveraging containers
    - Pods: The smallest form which will be interacted (wrapper) of a container. 
        - Usually 1 application has 1 pod. database pod, server pod, frontend pod, etc.
        - Each pod gets its own IP address from the virtual network. 
        - Pods are an abstraction of the containers.
        - Pods are ephemeral, they are spun up frequently
        - Pod dies -> Conductor identifies -> Schedules -> Creates Pod -> Provides new IP
    - Service: 
        - Sits infront of each pod which talk to each other. 
        - The service does not die.
        - A permanant IP address for communication between the pods
        - Acts as a load balancer.
    - Deployments are descriptors of pods
        - Describes resources are required
        - Ports needed
        - Environment Variables
    - Declarative: Kubernetes tries to apply these pods, the controller manager will identify that one pod when desired is two. 

## Basic Architecture
    - Has at least 1 Conductor node
    - 1 or more worker node
    - A number of different applications/docker containers on the different worker nodes.
    - Conductor node has:
        - API Server: Container which is the entrypoint into the cluster.
        - Controller Manager: Overview of whats happening inside the workers
        - Scheduler: Places the containers on the worker nodes, based on resources and load the container needs.
        - etcd: KV storage, holding the current state of the cluster (esentially the brain). This is what is leveraged in the etcd snapsots
    - Virtual network: Allows for communicaiton across the networks. It becomes on unified machine inside these machines. Workers have the most load, are usually much bigger due to what they are running.
    - Conductor is much more important than the worker nodes. You cannot access the cluster if your conductors go down. Generally in most instances, you'll have more than 1 conducotr
    - The Conductor controls all resources, and deals with all configuration requests. 
        - The requests have to be in Yaml or JSON

### Conductor Explained
    - Manages the worker nodes
    - Different processes on every conductor node.
        - API Server: 
            - When a user wants to deploy a new application. 
            - Cluster gateway
            - Gets the query or request
            - Authetnication gatekeeper.
            - Schedling pods, applications, services, API Server -> Validates request -> Forward request to the Schdeuler.
            - 1 entry point 
        - Scheduler:
            - API Server validates, then hands it to the scheduler.
            - The schdeuler does specific logic for which worker gets schedulerd.
            - Sees available resources on each of them
            - Sees least busy it will schedule it on that node.
            - Scheudler only decides where it will be schdeuled.
            - Kubelet gets request from scheduler and executes
        - Controller Manager:
            - Detects state changes like crashing of pods.
            - Contorller manager -> Reschedules for pods -> Decides which should restart the pods -> Kubelet request on the worker nodes
        - etcd
            - Key Value store of cluster state
            - Every change in the cluster is saved / updated in the KV store
            - The data here is what describes and enables the scheduler, controller manager, and API server. This is pulled from the conductor
            - Actual application data is NOT stored here.


### Worker Explained
    - Multiple application pods which run on that node.
    - Uses 3 processes on every node for schedling and managing containers
        - container runtime (docker, et al.)
        - Kublet: Interfaces with the container runtime and node itself. Starts pods with a container inside.
        - Kube Proxy: Intelligent forwarding logic, helps with performance and low overhead. It will forward to the replica on the same node for network latency.
    - Normally multiple Nodes which have a number of replicas
    - Services: A load balancer, which directs the data into the application and forwards it to the respected pod
    

### How it all works together
    - Self managed - Where the scheduler gets notification from the API Server. The resources are implmemented by kubelet. And monitored via etcd.
    - Self Healing - If the desired state does not equal the current state, as determined by ETCD, the scheduler and kublet attempt to remedy this
    - Automated - You don't have to manually backup, restore, or fix issues with running pods, they will do that themselves.

## Examples
    [First Deployment Example](./Examples/example-depoyment.yaml)
    
### Resources

- [What is Kubernetes | TechWorld with Nana](https://www.youtube.com/watch?v=VnvRFRk_51k)
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](ertified-kubernetes-administrator-with-practice-tests)