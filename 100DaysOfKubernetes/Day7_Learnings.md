# Study Log - Day 7

## Date: [8-10 Feburary, 2024 ]

### Today's Goals

- [x] Goal 1: Get VSCODE into a dev/prod namespace, apply the kustomization, and get the prod runnning.
- [x] Goal 2: Get Secrets implemented
- [ ] Goal 3: If time permits, apply the argocd deployment model

### Progress Overview
**Description**: I was able to take what I knew about kustomize and expand creating a vscode dev container which has custom values

### Skills Acquired
- **Skill 1:**
  - Kustomization: Understood the structure, resources, and requriments to put the patches and kustomizations in place
  - [Notes](Day6_Kustomize.md)
  - [Kustomize vscode base](./Day7/base/)
  - [Kustomize vscode overlay](./Day7/overlays/dev/)

### Challenges Faced

- **Challenge 1:**
  - I found dynamically setting names is difficult and have not found a solution for this yet. Specifically if there are namePrefix/Suffix, setting those on sepcific resources may cause issues IE: Secrets, Storage, etc.

### Plan for Tomorrow

Outline next steps for the next study session. Include specific goals, topics, or tasks to be focused on in the next day's session.

- [ ] Goal 1: Implement HashVault + Secrets handler
- [ ] Goal 2: Implement argocd model

