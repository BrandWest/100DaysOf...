# Day 5: Resources Continued from Day2

## Pesistent Volumes
    - Volumes are just references to directories and files
    - Can be local, cluster, or remote
    - Because pods are ephermeral, the volumes on shutdown will be gone, losing all data.
    - When data is spun back up, it is then an older state.
    - Theorietically a cluster should be agile
    - volume differences generally are from different resources, sources, etc.
    - 25 different types of volumes
        - Depends on use case for what is needed
    - Local volume which is stored within the container and only accesssible (based on configuration) from inside the container.
    - In example 1, we can see that the requirements for the pods to run are the volumes, names, and empytDir parameters
        - In the next step we write to the contents:  kubectl exec empty-dir --container busybox-a  -- sh -c "echo \"Hello World\" > /cache/hello.txt"
        - We can see it in the container b using: kubectl exec empty-dir --container busybox-b -- cat /cache/hello.txt
        - Because both pods are running in the same container they can see all the local data within the volume.
        - Once this container dies, it will not have any more data within it.
    - In example 2, we set up a host file with a host path
        - The host is the folder on the host machine.


## Config maps
    - Configmaps are a form of volumes
    - This is a resource to be mounted to the cluster and pods
    - This is differnent than the storage volumes
    - Configurations for passing into containers/pods
    - Can be a file or dir
    - Should not be over used
    - We don't want them to be over used.
    - Should be smaller apps and a specific use cases.
    - Could make your env less dynamic

## Kustomize
    - Assists in cluster management
    - Added to kubectl to use it use: kubectl -k
    - Helps with modifications to the file.
    - Each of the clusters could have a version of hte deployment on it.
        - Testing / Staging / Production
    - You prefer to add the most specific kustomizations in the kustomization file.
    - You can set up your file structure like:
        - base # Contains your base image and how it would look [Example](./Examples/base/kustomization.yaml)
            - deployment.yaml
            - service.yaml
            - kustomization.yaml
        - Overlay # contains your kustomzations for envs.
            - dev/kustomization.yaml # This is your folder for a dev env
            - prod/kustomization.yaml #This is your folder for prod env


## Key terms
- [Config Maps](https://kubernetes.io/docs/concepts/storage/volumes/#configmap): These are used to inject specific configuraiton data into pods. They are identified and referenced via volume types


### Interesting commands
- kubectl exec <name> --container <container name> -- <command>
- kubectl -k <Kustomize>
- kustomize build <file location> > somefile.yaml

### Examples
- [Example 1: Local Volumes](./Examples/pod.example.yaml): A local volume (within the container example)


### Resources
- [100 Day of Kubernetes](https://100daysofkubernetes.io/start/intro-to-k8s.html)
- [CKA: Certified Kubernetes Administrator](certified-kubernetes-administrator-with-practice-tests)
- [vfarcic/k8s-specs](https://github.com/vfarcic/k8s-specs) *Note*: This repo is hosted by vfarcic
- [Kubernetes Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)## Deployments
