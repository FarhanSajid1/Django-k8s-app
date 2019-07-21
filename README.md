# Django-k8s-app


Django Kubernetes application!

This is a CI/CD application using Python specifically the Django-Rest-Framework, this is a blog-style application inspired by 
Corey Schafer on YouTube. The blog application includes posts with CRUD operations, as well as a User service with
Authentication. We then dockerize the application and run the application on Kubernetes!

## Environment 
 ```                                                                                    __ _ _ _
  - - - - -         - - - - -   - -                - - - - -  | - - - - - - - - - - - - -| PVC   |
 | Google | - - - | Ingress- Nginx | - - -| Ser  | Django    | - - - - | Postgres |- - -|_ _ _ _|
 |  LB    |       |                |      | vice | App       |        |_ _ _ _ _ |
 |        | - - - |                | - - -|      | Deployment| - - -|  Redis Pod  
  --- - - -         - - - - - - - -               - - - - - - - - - |
 ````


# Application Settings
Because we are not using the traditional staging environment and are more focusing on Continous Delivery, on every commit to the master, we want to ensure that we develop and test properly. As such when developing we separate our environment into multiple sections a local environment, a Dev environment, and a Production Environment.

## Local Development Environment
For local development, we use the standard out of the box Django settings such as the default SQLite3 database, except we are going to use an S3 bucket for rendering our HTML and CSS files, this is enabled by running [django-storages](https://django-storages.readthedocs.io/en/latest/)
``` pip install django-storages ```

This enables us to have a CDN, a content delivery network responsible for rending our content for us.
We run our local development environment and ensure that the changes are running properly.

## Dev Development Environment
For our development environment we are going to be using Docker-Compose explained later, essentially it enables us to run and connect multiple containers and allow ease of communication. This environment implements the .dev settings as well as the .dev nginx container settings. 

## Containerizing our Application
Containers have revolutionized the way in which developers create and run code, Docker the most popular container platform
helps us in doing just that. A container allows us to create immutable infrastructure including all dependencies
and run time environment variables or settings. This enables other developers to easily run the same container on their own 
machines. 

For our container environment, I chose to use both a Dockerfile.Dev and a normal Dockerfile, like previously stated, because
we do not have a staging environment we want to ensure that everything works properly before pushing to Dockerhub. The Dockerfile.dev is useful for just creating a quick environment to ensure that the containers are build properly. The production Dockerfile mimics the real production level environment. In our case because we are using Kubernetes we have to build the images before creating the manifest files.

## Docker-Compose
Docker-compose is helpful for creating both 
