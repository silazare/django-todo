# Django-todo application deploy in Kubernetes

Test task for dockerize and deploy django-todo application in Kubernetes with Helm.
Application Docker image contains all migrations, including fake accounts creation for testing purposes only.

## Requirements

- [Minikube](https://github.com/kubernetes/minikube) v1.20.0 or later
- [Docker](https://docs.docker.com/get-docker) 19.03.14 or later
- [Helm](https://github.com/helm/helm) v3.2.x or later
- [Helmfile](https://github.com/roboll/helmfile) v0.139.x or later
- [helm-secrets](https://github.com/jkroepke/helm-secrets) v3.6.1 or later
- [Sops](https://github.com/mozilla/sops) 3.7.1 or later
- [GnuPG](https://gnupg.org/download/index.html) 2.2.x or later

Please follow the installation steps provided for each requirement tool.    
PGP key for secrets decryption should be provided separately and apart from this repository.

Example requirements installation for MacOS:
```
brew install helm helmfile sops gnupg
helm plugin install https://github.com/jkroepke/helm-secrets --version v3.6.1
```

## Project layout

 * [app](./app) -- Application local files, Dockerfile and docker-compose.yml
 * [helm](./helm) -- Directory with Helm charts
   * [django-todo](./helm/django-todo) -- Helm chart for django-todo application
 * [manifests](./manifests) -- Initial K8s manifests for deployment
 * [helmfile.yaml](./helmfile.yaml) -- Helmfile for deployment
 * [secrets.yaml](./secrets.yaml) -- Secrets for Helmfile deployment

## Service deploy steps with Helm

1) Clone the repository using Git:

```
$ git clone git@github.com:silazare/django-todo.git
```

2) Go to `django-todo` folder

3) Build Docker image localy if needed (Optional):

```
cd app
docker build -t django-todo:1.0 .
```

You can use already prepared image from [DockerHub](https://hub.docker.com/repository/docker/exciter86/django-todo)    
By default it is already defined in django-todo Helm chart [values](./helm/django-todo/values.yaml)

4) Start minikube cluster:

```
minikube start
```

5) Enable minikube ingress addon:

```
minikube addons enable ingress
```

6) Import provided PGP key:

```
gpg --import private.rsa
gpg --list-secret-keys
```

7) Check PGP key and make sure that you can view/encrypt the secrets:

```
sops -d secrets.yaml
helm secrets view secrets.yaml
```

8) Apply Helmfile

```
helmfile apply --skip-diff-on-install
```

9) Wait until helm charts would be deployed and check that resources are up:

```
kubectl get all
kubectl get ing -o=jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}'
```

10) HTTP to ingress IP via your web browser and make sure that you can reach the service.
All test accounts at django-todo should be accessible.

## Service cleanup steps with Helm

1) Destroy Helmfile

```
helmfile destroy
```

2) Delete minikube cluster:

```
minikube delete
```

## Appendix A: Service deploy steps with K8s manifests

1) Follow the same steps for minikube cluster creation

2) Go to manifests folder and apply all resources:

```
cd manifests
kubectl apply -f .
```

3) Wait until resource deployed and check that they are up:

```
kubectl get all
kubectl get ing -o=jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}'
```

4) HTTP to ingress IP via your web browser and make sure that you can reach the service.
All test accounts at django-todo should be accessible.

5) Delete all resources:

```
kubectl delete -f .
```
