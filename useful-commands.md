# <- image
## <- container
```md
docker run -it --rm --name ds -p 8888:8888 jupyter/datascience-notebook
#Amazon
sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-darwin-amd64-latest
#Apply Execute Permissions to the Binary
sudo chmod +x /usr/local/bin/ecs-cli
ecs-cli --version
#docker commands
docker search busybox
docker pull busybox
docker images
docker run #/
docker run # echo "hello from busybox"
docker run -it busybox sh

docker port #
docker stop #
docker run -it #
docker build -t # .
docker run -p 8888:5000 #


docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2
docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
docker container ls
docker container logs es
curl 0.0.0.0:9200
docker run -it --rm --net foodtrucks-net prakhar1989/foodtrucks-web bash
docker run -d --net ## -p 5000:5000 --name foodtrucks-web #/#
./setup-docker.sh
docker-compose --version
docker ps -q
docker stop $(docker ps -q)

docker-compose up
docker-compose up -d
docker-compose ps
docker-compose down -v
docker network rm ##
docker network ls
docker ps
docker network inspect ##

docker inspect #
docker images | grep #

docker ps -a
docker rename CONTAINER NEW_NAME

# start
docker start ##
# attach
docker exec -it ## /bin/bash
# get token
>jupyter notebook list
# view port mapping
# look NetworkSettings:Ports
docker inspect ##
# stop
docker stop ##

# WORDPRESS
docker run --name some-sql -e MYSQL_ROOT_PASSWORD=root -d mysql
docker run --name some-wordpress --link some-sql:mysql -p 8080:80 -d wordpress

romellfudi
pa9Bu538rCgrB8c#vs
```






















