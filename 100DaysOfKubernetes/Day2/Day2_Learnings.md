# Study Log - Day 2

## Date: [January 27, 2024]

### Today's Goals

- [x] Goal 1: I would like to have a better understanding of the yaml syntax, how it works, and how it can be leveraged into a efficent model.
- [x] Goal 2: Continue to grow my fundanmentals.

### Progress Overview
**Description**: Although I did not complete everything I wanted to on Day2, I did get an starter on the YAML and different fundamental services which include:
  - Services: They are a layer of abstraction and enable the self healing of the pods with ephemeral ips. 
    - Load Balancer: Only used in combination with cloud cluster and use that load balancer
    - ClusterIp: Only things within the cluster can communicate, not outside communication
    - NodePort: NodePort can give access to the outside world (or internal network outside of k8s cluster).
  - Deployments: Indicate the desired state of the resources
  - ReplicaSes: Indicate the number of instances
  - Match labels can be used to match replicas, services, etc. to specific apps

### Skills Acquired

- **Skill 1:**
  - Understanding of services, deployments, replicasets, and different configurations

### Challenges Faced

Document any challenges or difficulties encountered during the days study. This could include concepts that were challenging to grasp, technical issues, or any other obstacles.

- **Challenge 1:**
  - Motivation. I strugged today to get into the groove of studying and only managed about an hour or so.
    - To combat this, I will continue to work on my discipline and work towards continuing my learning, not getting discouraged by the amount of time studying.
- **Challenge 2:**
  - There are quite a few different resources out there and it can be a bit overwhelming
    - Try to limit myself to 1 or 2 videos/documents, and the documentation from k8s itself.

### Resources Used

Resources for the days studying

- **[Anais Urlichs Day 4](https://www.youtube.com/watch?v=cmc4f4TyHaU&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=5):**
  - Used to identify some of the common elements within K8s
- **[Anais Urlichs Day 6](https://www.youtube.com/watch?v=qt76R2G4h-0&list=PLWnens-FYbIpUpmiiNYfkqTZQUYppGMFV&index=7):**
  - Used to identify some of the common yaml pitfalls
- **[vfarcic/k8s-specs](https://github.com/vfarcic/k8s-specs) *Note*: This repo is hosted by vfarcic**
  - A repo with many examples of different resources levereaged by Anais in their 100 Days Challenge.


### Plan for Tomorrow

Outline next steps for the next study session. Include specific goals, topics, or tasks to be focused on in the next day's session.

- [ ] Goal 1: Complete todays studying.

### Reflection

My studying today was a bit less optimal as I was fairly distracted. I'm hoping by sitting down and doing about 30 min chunks with breaks will help relieve the feelings of de-motivation increasing my willingness to sit down. I find that I'm distracted by all the things I COULD be doing, versus doing what I SHOULD be doing.
