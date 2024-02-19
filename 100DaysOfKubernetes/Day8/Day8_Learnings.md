# Study Log - Day 8

## Date: [11 Feburary, 2024 ]

### Today's Goals

- [x] Goal 1: Implement HashVault + Secrets handler
- [ ] Goal 2: Implement argocd model
  - [ ] SubGoal 1: Implement Argocd + Hashivault for secret holding

### Progress Overview
**Description**: 
  - I was able to install, modify, and change the helm values for the Vault installation. This took a lot of time as the ingress was causing issues and certs (see challenge 1).
  - However, Goal 1 is complete and I can inject secrets into these pods. My next step is to get it to work with vscode. 
  - Once that POC is completed, I'll work on leveraging gitops + argocd for infra as code set up. This is the end goal of the majority of these projects so far.

### Skills Acquired
- **Skill 1:**
  - Setting up a Vault resource
- **Skill 2:**
  - Modifying helm packages to align with specific use cases.

### Challenges Faced
- **Challenge 1:**
  - Unable to update and access via ingress/domain. Tired multiple different things and was unable to complete this task. Ideally it would be accessible locally without port forwarding, I could add a service for the UI to do this. According to vault this is a securtiy consideration. 
- **Challenge 2:**
  - I struggled with implementing the specific certificates for this instance. I was unable to get cert-manager to dynamically create the certificates but now that its running, I feel I have a better idea and could potentially get it working.


### Resources Used
- **Resource 1:**
  - The main resource used was from "That DevOps Guy" on YouTube who describes the setup process for vault. [link](https://www.youtube.com/watch?v=2Owo4Ioo9tQ)


### Plan for Tomorrow

The next steps after this is to set up the vscode instance ot have the secret injected from vault. I'd also like to access the vault UI without needing to port forward. Finally, update the Day8_HashiVault.md file with more notes that I haven't written today.

