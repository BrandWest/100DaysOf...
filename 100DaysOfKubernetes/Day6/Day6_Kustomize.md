# Day 6: Kustomize

## Kustomize
- After learning a bit about Kustomize I wanted to get more information about it so I've decided to dedicate a day to it.
- Can limit the amount of complex templating in different files
- Keeps things consistent using common things
- Overrides manifest files for each of Envs.
    - Patches 
    - Overlays
- Patches & Overlays live in the directories
- Much easier than helm.
- You set the specific resources
    - The files that are to be modififed
- You specify the specific common attributes you want depending on your needs    
    - commonLables - provide selectorlabels
    - commonAnnotations - annotating resoucres
    - namePrefix - provides what each name should be before the actual name
    - nameSuffix - ending name
- Generators
    - Remove need for configmap manifests
        - secrets can work witht his
- The file stucture can be found: [File structure of a simple kustomization file](./Examples/file_structure.txt)
- Overlays
    - Overriding base manifest and patch the specific files
    - The following examples show the differences between the original and kustomize versions 
        - Kustomize file v1, these changes create the changes within the below examples:
            resources:
                - deployment.yaml
                - service.yaml
                commonLabels:
                    app: mywebapp
        - [Deployment Differences](./Examples/example.kustomize.deployment.yaml)
        - [Service Differences](./Examples/example.kustomize.service.yaml)
- The files get read and generate a new config which can be applied directly to k8s, or to a file.
    - Once you run kubectl kustomize . you will receive an output: 
        - [Post Kustomize Changes](./Examples/example.post.kustomize.yaml)
- when you set up different overlays you do not need to specify anything in the kustomziation (resources)
    - [Example Dev Kustomization](./Examples/kustomize/overlays/dev/kustomization.yaml)
    - You can then override specific values
    - You can change the namespaces
    - You can change the number of replicas
        - When you are making changes to the specific spec, you copy more of the data into a new file. 
        - [Example Dev Replica Change](./Examples/kustomize/overlays/dev/replicas.yaml)
        - With this you can even change further down, if you wanted to change the image you'd copy to there. Commented out in the above example.
        - You can add different env files via new config map generators too. This means you can have separate secrets for the env. 
        - The below example has the patches which are used in this instance for the replicas, and the new config map generator.
        - In addition, you can remove the .env file in the base since you are adding your own values in each prod/dev instance
        - [Example Dev Env](./Examples/kustomize/overlays/dev/kustomization.yaml)
        - For this type of example to work, you need a dev/prod NAMESPACES already
- Performing adhoc patches
    - New patches can replace adhoc strings by outlining the path
    - [Adhoc replacements](./Examples/other.patch.example.yaml)



## Key terms
- Base: These are the main files that are to be kustomized when working through the kustomization pipeline
- Overlays: These are the specific changes for each resource, what to add, change, modify, patch. 


### Interesting commands
- kubectl apply -k . : Applies the configurations
- kubectl kustomize : outputs the different changes to the files


### Examples
- [Kustomize Example File 1](./Examples/example.kustomization.yaml)
- [File structure of a simple kustomization file](./Examples/file_structure.txt)
- [Deployment Differences](./Examples/example.kustomize.deployment.yaml)
- [Service Differences](./Examples/example.kustomize.service.yaml)




### Resources
- [Kustomize By DevOps Journey](https://www.youtube.com/watch?v=spCdNeNCuFU)
- [mykustomap - devopsjourney1](https://github.com/devopsjourney1/mykustomapp/tree/master)
- [Kustomize Patch Documentation](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#composing)