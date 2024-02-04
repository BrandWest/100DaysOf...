# Study Log - Day 6

## Date: [3 Feburary, 2024 ]

### Today's Goals

- [x] Goal 1: Understand Kustomize

### Progress Overview
**Description**: I worked on a simple application which takes a manifest for deployment, configmaps, and services and created a kustomization bases, overlays (dev/prod) and kustomization.yaml files for each

### Skills Acquired

- **Skill 1:**
  - Kustomization: Understood the structure, resources, and requriments to put the patches and kustomizations in place
  - [Notes](Day6_Kustomize.md)


### Challenges Faced

- **Challenge 1:**
  - The tutorial I was following used "patches" which are deprecated and would not let me get the new conifg via kubectl kustomize
  - I was able to find the reason for the issue in the kubernetes documentation
- **Challenge 2:**
  - The image used was not arm based and could not be put on my raspberry pi's
  - The image looked to be running and immediately fell into a CrashloopBackoff. I found that in the logs there was an exec error which is caused by the wrong format for the image.


### Resources Used

- **Resource 1:**
  - I followed the DevOps Journey youtube channel to identify how kustomizations work.
  - [Kustomize By DevOps Journey](https://www.youtube.com/watch?v=spCdNeNCuFU)
  - [mykustomap - devopsjourney1](https://github.com/devopsjourney1/mykustomapp/tree/master)
- **Resource 2:**
  - I reviewed the kustomization patching details in the docmentation
  - [Kustomize Patch Documentation](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#composing)


### Plan for Tomorrow

Outline next steps for the next study session. Include specific goals, topics, or tasks to be focused on in the next day's session.

- [ ] Goal 1: Get VSCODE into a dev/prod namespace, apply the kustomization, and get the prod runnning.
- [ ] Goal 2: Get Secrets implemented
- [ ] Goal 3: If time permits, apply the argocd deployment model

