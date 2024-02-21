# Day 8: Hashivault

## HashiVault
- HashiVault is used to access tokens and store them securely
- Installed Vault onto my machine
- there are different -mount types, specifically secret uses the kv v2 secrets engine -mount=secret
- This version of using the CLI (kv put) for putting the kv will store in the shell. You can use Resource 2 to identify other ways to find this
    - Alternatives include:
        1. key=- which opens up a text input
        2. json {"key":"value"} with command: vault kv put -mount=secret @keyfilename.json
        3. Disable command history for vault export HISTIGNORE="&:vault*"
- using vault kv get retuns the following in the cli:
    == Secret Path ==
    secret/data/hello

    ======= Metadata =======
    Key                Value
    ---                -----
    created_time       2024-02-11T16:02:46.264329205Z
    custom_metadata    <nil>
    deletion_time      n/a
    destroyed          false
    version            1

    === Data ===
    Key    Value
    ---    -----
    foo    world
- When deleting parameters you can set destroyed to false, which will let you recover the old secret using `vault kv undelete -mount=<type> -versions=# <name>`
- You must start hasivault with `vault secrets enable -path=kv kv` Since all paths are isolated from one another.
- You can specify the path to use and the specific storage via `vault kv put <vaultname>/<name> <key>=<value>`

- I followed the guide from resource #4 to help set up the vault instance.
- There were a bunch of issues trying to set up HashiVault and applying an ingress to it, I think I have a solutoin but for now its working and I'm happy with that. I'm not thrilled with the requirements for port-forwarding but I will modify that in the future. Currently its ina  place where I can set up and run the vault with no issues.

### Interesting commands
- vault -help _note_: all subcommands have a help screen similar to kubectl/kustomize
- vault server -dev: Starts a dev server with an unsealed secret with a browser gui @ http://127.0.0.1:8200
- vault kv -help: provides information for vault key/vaule store engine
- vault kv put -mount=<type> <name> <key>=<value> # Add a key value part to a path and vault 
- vault kv get -mount=<type> <name> # Get a key from a path
- vault kv delete -mount=<type> <name> # delete a secret

### Examples



### Resources
- 1. [HashiVault](https://developer.hashicorp.com/vault)
- 2. [Alternative Secret Implementations](https://developer.hashicorp.com/vault/tutorials/secrets-management/static-secrets#q-how-do-i-enter-my-secrets-without-exposing-the-secret-in-my-shell-s-history)
- 3. [k8s and vault](https://developer.hashicorp.com/vault/docs/platform/k8s)
4. [How to deploy Vault for Kubernetes in 2022 and inject secrets](https://www.youtube.com/watch?v=2Owo4Ioo9tQ)