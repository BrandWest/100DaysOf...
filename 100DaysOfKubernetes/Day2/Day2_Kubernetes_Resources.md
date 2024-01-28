# Day 2: Resources Continued

## Pod info continued
- Generally want to use specific namesapces for specific applicaitons.
- Should remove resources that are not needed.
- If you have a deployment, you can't delete a pod (which I knew) due to restarting the pod once deleted.

## Services
- Services sit in front of pods
- Serivces are abstraction from pods IP address
- Helps with ephemeral Pods.
- The service accepts the requests and determines which pod is bet to handle the request (If there is more than 1 pod)
- Cluster IPs are defined in the pod yamls, the service would interface with ingresses 
- Ingress is interface with outside world.
- Internet -> Ingress -> Service -> Pod
- All pods have access to the Node Port

## Deployments
- Used to get the resoureces wanted
- Responsible for the pod lifecycle
- Different to services
- Ensure that the resouces are there to be used

## ReplicaSets
- Creating exact instances of each other
- Names the number of pods we want running no matter what.
- If we have 3 up and only want 2, it will remove the additional pod.
- Memory, cpu is used when deciding if it can meet the definition
- This makes the cluster "self healing"
- In the selector you can use the *matchLabels* in order to have the RS pick that pod to replicate. [Example_RS](./resource_examples/go-demo-2.yml)
- The pods and replica-sets share the naming conventions

## Errors 
### Crashloop Backoff
- Some error occured
    - Misconfiguration 
    - Yaml issues
    - So the container cant start, if it continues to crash, it'll slow donw the restarts
- 


## Key terms
- Selectors: Provides a keyvalue pair in yaml - for the service to identify the pod
- Service types:
    - Load Balancer: Only used in combination with cloud cluster and use that load balancer
    - ClusterIp: Only things within the cluster can communicate, not outside communication
    - NodePort: NodePort can give access to the outside world.


### Interesting commands
- kubectl run <name> --image <image name> --generator "run-pod/v1" # Although this is less useful in terms of declaring the pods
- kubectl exec --stdin --tty <container name> -- bash
- kubectl get <resource name> --namespace <name>
- kubectl config current-context --> lets you know the specific context you're in
- kubectl expose <resource> <resource name> --name=<resource full name> --target-port=<port number __Specifically where the cotnainer port is listening__> type=<resource type (NodePort, ClusterIP, LoadBalancer)>


### Resources
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](certified-kubernetes-administrator-with-practice-tests)
- [Anais Urlichs Day 4](https://www.youtube.com/watch?v=cmc4f4TyHaU&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=5)
- [Anais Urlichs Day 6](https://www.youtube.com/watch?v=qt76R2G4h-0&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=7)
- [vfarcic/k8s-specs](https://github.com/vfarcic/k8s-specs) *Note*: This repo is hosted by vfarcic