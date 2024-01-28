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

## Deployments


## ReplicaSets
- 

## Errors 
### Crashloop Backoff
- Some error occured
    - Misconfiguration 
    - Yaml issues
    - So the container cant start, if it continues to crash, it'll slow donw the restarts
- 


## Key terms
- Selectors: Provides a keyvalue pair in yaml - for the service to identify the pod

### Interesting commands
- kubectl run <name> --image <image name> --generator "run-pod/v1" # Although this is less useful in terms of declaring the pods
- kubectl exec --stdin --tty <container name> -- bash
- kubectl get <resource name> --namespace <name>


### Resources
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](certified-kubernetes-administrator-with-practice-tests)
- [Anais Urlichs Day 4](https://www.youtube.com/watch?v=cmc4f4TyHaU&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=5)
- [Anais Urlichs Day 6](https://www.youtube.com/watch?v=qt76R2G4h-0&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=7)
- [vfacic/k8s-specs](https://github.com/vfarcic/k8s-specs)