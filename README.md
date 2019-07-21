# Django-k8s-app


Django Kubernetes application!

This is a CI/CD application using Python specifically the Django-Rest-Framework, this is the same blog-style application shown by Corey Schafer on YouTube. The blog application includes posts with CRUD operations, as well as a User service with
Authentication. We then dockerize the application and run the application on Kubernetes!

The first half of the ReadMe is theory based, with some of the project sprinkled in.

## Environment 
 ```                                                                                      __ _ _ _
  - - - - -         - - - - -   - -              |  - - - - -  | - - - - - - - - - - - - -| PVC   |
 | Google | - - - | Ingress- Nginx | - - -| Ser  | Django      | - - - - | Postgres |- - -|_ _ _ _|
 |  LB    |       |                |      | vice | App         |         |_ _ _ _ _ |
 |        | - - - |                | - - -|      | Deployment  | - - - |            |
  --- - - -         - - - - - - - -               - - - - - - - - -  - |  Redis Pod |
                                                                       | ___________|
````
From the crude image it is definitely not obvious, but the end goal of this project is that we want to achieve a Kubernetes Cluster with a Ingress-Nginx running for routing requests as well as deployments and services for the monolithic application and connecting that application to both Postgres and Redis. Postgres is going to be connected to a [Persistent Volume Claim] (https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) ensuring that we have a reliable means of storage. The application is a monolith, and for the sake of brevity for the image above, I did not include the services which are required for the Redis or Postgres pods. So in all we will have Ingress-Nginx, which will set up the routing rules, as well as a deployments and a services for the Django Application, Postgres, and Redis. All the Kubernetes manifest files will be located inside the K8s directory, 


# Application Settings
Because we are not using the traditional staging environment and are more focusing on Continous Delivery, on every commit to the master, we want to ensure that we develop and test properly. As such when developing we separate our environment into multiple sections a local environment, a Dev environment, and a Production Environment. There are also requirements specific for the production environment specifically the Gunicorn webserver.

## Local Development Environment
For local development, we use the standard out of the box Django settings such as the default SQLite3 database, except we are going to use an S3 bucket for rendering our HTML and CSS files, this is enabled by running [django-storages](https://django-storages.readthedocs.io/en/latest/). This means every time we run 
``` python manage.py collectstatic ``` 
The static files will be uploaded to an S3 bucket, so we need to have an account set up. 
``` pip install django-storages ```

This enables us to have a CDN, a content delivery network responsible for rending our content for us.
We run our local development environment and ensure that the changes are running properly.

## Dev Development Environment
For our development environment we are going to be using Docker-Compose explained later, essentially it enables us to run and connect multiple containers and allow ease of communication. This environment implements a production ready USWGI server, which is neccessary for production use for any Python Application. I opted to using [Gunicorn] (https://gunicorn.org/) for the production server. The Dev stage is used to ensure that the environment is working properly, and that we can containizer the application. Only then can we move into running this on a Kubernetes cluster.

## Production Development Environment
This environment is supposed to mimic the production level environment, in a true production environment, we would definitely use a staging cluster and run the manifests there. For our sake, we will be using MiniKube, which sets up a small cluster locally using VirtualMachine. In this environment we are going to create manifest files, which declare the state of our cluster.

## Containerizing our Application
Containers have revolutionized the way in which developers create and run code, Docker the most popular container platform
helps us in doing just that. A container allows us to create immutable infrastructure including all dependencies
and run time environment variables or settings. This enables other developers to easily run the same container on their own 
machines. 

For our container environment, I have create both Dockerfile.dev as well as the production docker files, the reason for this is because I implemented this same project with AWS Elasticbeanstalk, and there was a need to provide test the environment with two dockerfiles. In our case because we are using Kubernetes we have to build the images before creating the manifest files. So that is why we use Docker-Compose it can build the images, which we are using, and if everything works correctly we can push the images to Dockerhub

## Docker-Compose
Docker-compose is helpful for creating a development environment, with a simple command
``` docker-compose up ```
We can have all our containers up and running, when using Docker-Compose, Docker creates an isolated networking environment for us to use. As such all the containers inside the environment are able to communicate with each other by using the DNS container names. This is important, docker-compose makes networking much easier when compared to Kubernetes, where we need to explicitly state how we want other pods to connect to our containers.

## Kubernetes
Kubernetes is or already is becoming the de facto standard for production level container orchestration, the only other alternative is Docker-Swarm, I have never tried Docker-Swarm, but a majority of companies implement Kubernetes and it is extremely efficient so we will be using this. 

# Why container orchestration?
When we are scaling our application, not neccessarily this application, but when we are scaling, we need to have more computing power, Kubernetes allows us to have multiple VMs called "Nodes" and it is simple to add more, Kubernetes does all the heavy lifting, the Kube-apiserver is the only point of communication, we Declaratively state our desired state and Kubernetes handles scheduling pods in those Nodes as well as the communication through the Kube-Scheduler and Kube-Controller. Simply Kubernetes makes our lives much easier.

# CI/CD
CI/CD standard for continous integration/continous delivery, we want to automate our build processes as well as delivery/deployment depending on our environment. Everytime a developer makes a commit to a particular branch, namely the Master branch, we want to kick off a build/Deploy pipeline. Because we want to ensure that only good code is merged, we develop and push or a feature branch, request a merge, allow TravisCI, our CI/CD tool to do the rest namely, run integration tests, build the docker images, Imperatively update our kubernetes manifest container tags, and push to Google Kubernetes Engine. 

``` 
# logging into docker/ using TravisCI environment variables
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

  # building our test environment
  - docker build -t farhansajid2/django-test -f ./docker/dev/Dockerfile.dev .

script:
  - docker run farhansajid2/django-test python manage.py test

# deploy script to update images
deploy:
  provider: script
  script: bash ./deploy.sh
  on:
    branch: master

```

# TravisCI and imperatively changing the image Tags
TravisCI is a free CI/CD tool used to make our lives easier, we are going to test, build, and change our image tags. The reason for this is because in Kubernetes if we leave the tag as :latest Kubernetes does not notice that the manifest has changed 
For example
``` 
spec:
      containers:
        - name: app
          image: farhansajid2/django-k8s-app
          ports:
            - containerPort: 8990

```
if we were to leave this every time we run our pipeline, the image would never get updated, this is because latest is automatically added as the tag, and Kubernetes thinks the manifest hasn't been updated, instead we are going to tag the image with the Git-SHA of the latest commit, this is only possible because of an environment variable in TravisCI 

```
SHA=$(git rev-parse HEAD)
spec:
      containers:
        - name: app
          image: farhansajid2/django-k8s-app:$SHA
          ports:
            - containerPort: 8990
```

this is the end result which we want to achieve, and this is done through an imperative command. An imperative command means specifying exactly what we want to change in our cluster. For example, if I wanted to update all my pods to version 1.5, a declarative approach says update to 1.5 thats it. For an imperative approach we have to specify exactly how to reach that state, I could say update two pods to 1.5 from 1.25 or update to 1.5 from 1.0, etc..

# The imperative command is as follows
```
kubectl set image deployment/app-deployment app=farhansajid2/django-k8s-app:$SHA
```
kubectl set <attribute_to_change> <deployment>/<deployment_name> <pod_selector>=<new_image_tag>
 

# Application Specifics

## Environment Variables
All the environment variables are found inside the django-app-deployment.yml, requirements include an S3 bucket, GMAIL account. Other than that you just need to create postgres as well as Redis

## Ingress-Nginx
We do not create a specific nginx pod, we are going to rely on the [Ingress-Nginx] (https://github.com/kubernetes/ingress-nginx), the reason is that we do not want to write these nginx files, the community lead project handles all of this for us, we can just add TLS support through annotations and the rest is pretty straight forward. See the ingress.yml file for examples on how to add routing rules. We can also specify a host once you purchase a domain-name. 

## Helm and Tiller Setup
To install packages such as Datadog for monitoring or Ingress-Nginx, we will be implementing helm. Helm is a package manager for Kubernetes and it makes it easy to install application through charts. To install Helm we simply follow the [guide here](https://helm.sh/docs/using_helm/#installing-helm) afterward we need to give tiller, the client pod which carries changes to the cluster permission. On GKE, pods do not have the permission to make changes to the cluster, we need to give explicit permission beforehand. 

``` 
 kubectl create serviceaccount --namespace kube-system tiller
 kubectl create clusterrolebinding tiler-cluster-rule --clusterole=cluster-admin --serviceaccount=kube-system:tiller

```

First we create a service account, which is an account for pods to administer the cluster, then we want to give clusterrolebinding, which are privileges to make changes to the entire cluster. 
Once this is done we simply run 
``` 
 helm init --service-account tiller --upgrade
```
This sets up helm and tiller, and now you can install third party software.
