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
- Liveness checks - Does the pod have to be restarted
- Readiness Check - Is the pod ready to be served to users
- Termination grace period - Determines how long its up and running until its actually terminated 30s by default.


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

## Resources and Configurations

### Deployments and Upgrades
- When the deployment is changed, and the image changes the rollout will be automatically triggered by the deployment
    - This does take some time.
    - This can be gradually rolled out for maintaining access to all users
    - It creates a 4th of 3 pods when upgrading with no LB access. 
    - The liveness + readiness checks are passed
    - Now it'll serve from the loadbalancer
    - The termination grace period is passed, and the deployment deletes the pod.
    - This occurs for each of the replicas you want (3 in our case)
- This can be configured.

#### Examples
- [First Deployment Example](./Examples/example-depoyment.yaml)

### Namespaces
- Namespaces are used to isolate different apps and resources from one another. 
- If I have a namespace called demo1 and a second one called demo2, they can run on the same node, use similar services.
- If a service is namespaced to demo1, demo2 can not use that. Similarly with storage, if you have a storage block of 1GB on the same node or endpoint as demo1 and demo2 but namespaced to demo2, demo1 can not access that storage block.
- Namespaces are a way to divide cluster resources between multiple users [k8s namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- there are some premade namespaces which are usable including:
    - Default: The default namespace for apps if not specified
    - kube-node-lease: 
    - kube-public
    - kube-system
- When a custom namespace is applied your endpoint will now have a different DNS record <service name>.<namespace>.svc.cluster.local
- Often times we can have a production and a development namespace
    - One for operations team to manage (Production)
    - One for developmental team to manage (Development)
#### Examples
- [Namespace Config Example](./Examples/example-namespace.yaml)

### Pods
- Ephemeral, meaning the data is not saved here.
- Are the smallest point of the kubernetes resource
- The pods is not type locked to the underlying OS
- Containers within a pod are run on the same node.
- [Images](https://kubernetes.io/docs/concepts/containers/images/): 
    - A container image (generally docker) is the software package that runs the application
- Containers are to be considered stateless and imutable (not to be changed) while running
- [Container environments](https://kubernetes.io/docs/concepts/containers/container-environment/):
    - Provide a filesystem which is an image and one or more volumes
    - Information ont he container
    - Informaiton on other objects in the cluster.
- [Container information](https://kubernetes.io/docs/concepts/containers/container-environment/#container-information):
    - The hostname of a container is the name of the Pod the container is running.
    - User defined env variables
    - The pod name and namespace
- [Cluster information](https://kubernetes.io/docs/concepts/containers/container-environment/#cluster-information):
    - Services that were run whent he container was created (as env vars)
    - This is limited to services within the same ns.
- [Runtime Class](https://kubernetes.io/docs/concepts/containers/runtime-class/):
    - Selects the runtime configuration for a container. 
    - You have to balance between security and performance
        - Security: Maybe a virtualized hardware solution including isolation, but larger overhead.
        - Performance: Faster, and more efficent, less secure.
    -There are a few Runtime Classes built in 
        - containerd
        - CRI-O
- [Container Life-Cycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/):
    - Managed by kubelet
    - Allows Containers to be aware of events in the management lifecycle.
    - This allows code to be run based on the lifecycle hook executed.
    - [PostStart]():
        - Exposed to containers
        - Executed immediately after a container is created
        - This could run after ENTRYPOINT
    - [PreStop]():
        - Exposed to containers
        - Run imediately before termination due to API request or management event.
            - liveness/startup probe failure
            - resource contention
            - more...
        - Fails if the container is already in a terminated or completed state.
        - Hook must complete BEFORE the TERM signal can be sent to the container.
        - Termination grace time is started before PreStop is sent. Guarentees container terminates.
    - [Hook Handler Implementations]():
        - Exec: Executes specific commands (pre-stop.sh)
        - HTTP: Performs an HTTP request
        - Sleep: Pauses the container for a specified time. Must have PodLifecycleSleepAciton enabled.
    - [Hook handler execution]():
        - Lifecycle management hook is called and executes the handler according to the hook action. The following are exected by the kublet process:
            - httpGet
            - tcpSocket
            - sleep
        - Where exec is executed in the container
        - Hook handlers are synchronous within container and pod creation.
            - For a PostStart hook, ENTRYPOINT and hook fire asynchronously
            - if it fails, the pod will not reach a running state.
    - [Debugging Hook Handlers]():
        - The hook handler logs are brodcast as events and not located within a pods logs.

#### Examples
- [Runtime Class Example with Pod](./Examples/example-RuntimeClass.yaml)
- [A Simple Pod](./Example/example-pod.yaml)

### Interesting commands
- kubectl delete namespace <name>: Deletes EVERYTHING under the ns.
- kubectl create -f <filename>: Creates the resource with the config from the sepcified filename
- kubectl create deployment snowflake --image=registry.k8s.io/serve_hostname -n=development --replicas=2
    - Although you can run things like this, I don't like it.
    - This will create a deployment called snowflake
    - uses the image registry.k8s.io/serve_hostname
    - -n=development indicates the namespace
    - replicas are how many pods to create
- kubectl apply -f <fileame.yaml || url to yaml file>: Applies a configuration based on a file

### Resources
- [What is Kubernetes | TechWorld with Nana](https://www.youtube.com/watch?v=VnvRFRk_51k)
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](ertified-kubernetes-administrator-with-practice-tests)
