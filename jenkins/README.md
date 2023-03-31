## commands

- build image

```bash
docker build -t <image_name> .
docker build -t jenkins-docker-1 .
```

- run container with port 8080 exposed to 8082 on host

```bash
docker run -it --rm -p 8082:8080 --name <container_name> <image_name>
docker run -it -p 8082:8080 --name jenkins-container-1 jenkins-docker-1
// install plugins:: Docker Plugin, Master node setting and add label 'main'
```

- run container with port 8080 exposed to 8082 on host and volume mounted mapped to /app

```bash
docker run -it --rm -p 8082:8080 -v $(pwd):/app <image_name>
```

## Imoportant directories that should be mapped to host

```sh
-v /your/host/jenkins/home:/var/jenkins_home
-v /var/run/docker.sock:/var/run/docker.sock
-v /your/host/maven/repository:/root/.m2/repository
```

- start a container

```bash
docker start <container_name>
docker start jenkins-container-1
```

- stop a container

```bash
docker stop <container_name>
docker stop jenkins-container-1
```

- enter to terminal

```bash
docker exec -it jenkins-container-1 --user root /bin/bash
apt-get update && apt-get install -y 
```

## Docker Compose commands
Here are some essential Docker Compose commands to work with the Docker Compose file we created:

- docker-compose up -d: starts the services defined in the Docker Compose file in detached mode (in the background).
- docker-compose down: stops and removes the containers created by the Docker Compose file.
- docker-compose logs <service>: displays the logs of a specific service defined in the Docker Compose file.
- docker-compose ps: lists the running containers defined in the Docker Compose file.
- docker-compose exec <service> <command>: runs a command inside a container of a specific service defined in the Docker Compose file.
- docker-compose build <service>: builds the image for a specific service defined in the Docker Compose file.

For example, to start the services defined in the Docker Compose file, you can run:
```
docker-compose up -d
```
To view the logs of the jenkins service, you can run:
```
docker-compose logs jenkins
```
To execute a command inside the dependencies service, you can run:
```
docker-compose exec dependencies <command>
Replace <command> with the command you want to execute.
```
To stop and remove the containers created by the Docker Compose file, you can run:
```
docker-compose down
```