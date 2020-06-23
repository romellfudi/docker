https://medium.com/@bluedme/connecting-jupyterhub-to-auth0-e92f0bb6efb0

# Docker Jupyterhub

```sh
docker pull jupyterhub/jupyterhub
```

Time for some docker arguments explanation now: 
- -p is used to map your local port 8000 to the container port 8000
- -d is used to run the container in background, jupyterhub will just write logs so no need to output them in your terminal unless you want to troubleshoot a server error
- “ — name jupyterhub” names your container jupyterhub
- “jupyterhub” is the last command used to start the jupyterhub server
```sh 
docker run -p 8000:8000 -d --name jupyterhub jupyterhub/jupyterhub jupyterhub
```

Enter into docker and set user & password
```sh
docker exec -it jupyterhub bash # allows us to run a bash process
useradd --create-home romellfudi
passwd romellfudi # put your own password 1qA
exit
```

```sh
docker restart jupyterhub # restart
```

```sh
export JUPYTERHUB_CONTAINER_ID=$( docker ps | awk '/jupyterhub/ { print $1 }' )
docker commit --change='CMD ["jupyterhub", "--config", "/srv/jupyterhub/jupyterhub_config.py"]' $JUPYTERHUB_CONTAINER_ID dev/jupyterhub_oauth:v1
```

```sh
docker images | grep dev/jupyterhub_oauth
docker stop jupyterhub
docker rm jupyterhub
```

```
sudo mkdir -p /opt/jupyterhub/etc/jupyterhub/
sudo jupyterhub --generate-config
sudo code jupyterhub_config.py
sudo mkdir -p /opt/jupyterhub/etc/systemd
sudo code /opt/jupyterhub/etc/systemd/jupyterhub.service