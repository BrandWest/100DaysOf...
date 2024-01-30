# Day 3-4: Resources Continued from Day2

## Deployments
- Used to get the resoureces wanted
- Responsible for the pod lifecycle
- Different to services
- Ensure that the resouces are there to be used
- [Example Deployment](./Examples/deployment.example.yaml)
    - Our example shows us the following:
        - the spec shows what the overall deployment will look like, what it'll do.
        - Match Labels within the selector is indicating that the deployment should only run where these labels match
        - Expose ports within the containers spec.
        - Always pull images on build
    - Its important to make sure that labels match.
    - Image: <username>/<image name>:<tag of image>
- [Example Service](./Examples/service.example.yaml)
    - Provides service outside of the kubernetes cluster
    - Accessing the pods via 
        - Port: THis is how people can access the services
        - targetPort: the container 
        - NodePort: How can resources outside of the cluster. It has the benefits of IP and the service accept from outside.
        - name: Can provide a name for easier port application instead of numbers
    

## Ingress
    - Requires an ingress controller to connect with the type ingress
    - Requires a load balancer to be connected
    - We create resources which can accept connections from outside
    - Ingress type connects to load balancer
    - Outside connections can connect to those endpoints via the ingress
    - Can be limited to ClusterIP which will only be internal 
    - Nginx Ingress controller examples via official nginx


## Accessing UIs
    - You can grab the kubernetes IP for the service 


## Key terms
    - Ingress: Through the application ingress application, it knows how to serve requests
    - Helm: Esentially a package manager can modify via values.yaml generally


### Interesting commands
    - kubectl config get-contexts: gives some additional information
    - kubectl get svc <service name> -o yaml: get the yaml of the service


### Resources
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](certified-kubernetes-administrator-with-practice-tests)
- [vfarcic/k8s-specs](https://github.com/vfarcic/k8s-specs) *Note*: This repo is hosted by vfarcic
- [Kubernetes By Example](https://kubebyexample.com/)
- [Kubernetes Ingress](https://www.youtube.com/watch?v=rNvFvGVzT5o&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=14)