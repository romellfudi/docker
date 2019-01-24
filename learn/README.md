https://docker-curriculum.com/
```sh
docker search busybox
docker pull busybox
docker images
docker run busybox
docker run busybox echo "hello from busybox"
docker run -it busybox sh


docker run -d -P --name static-site prakhar1989/static-site
docker port static-site
docker stop static-site

docker pull ubuntu:12.04
docker run -it ubuntu:12.04

git clone https://github.com/prakhar1989/docker-curriculum
docker build -t prakhar1989/catnip .
docker run -p 8888:5000 prakhar1989/catnip

git clone https://github.com/prakhar1989/FoodTrucks
cd FoodTrucks
tree -L 2
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2
docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
docker container ls
docker container logs es
curl 0.0.0.0:9200

docker build -t prakhar1989/foodtrucks-web .
docker run -P --rm prakhar1989/foodtrucks-web
docker container ls
docker run -it --rm prakhar1989/foodtrucks-web bash
docker network create foodtrucks-net
docker container stop es
docker network inspect foodtrucks-net
docker run -it --rm --net foodtrucks-net prakhar1989/foodtrucks-web bash
root@9d2722cf282c:/opt/flask-app # curl es:9200
exit
docker run -d --net foodtrucks-net -p 5000:5000 --name foodtrucks-web prakhar1989/foodtrucks-web

overall
# build the flask container
docker build -t prakhar1989/foodtrucks-web .
# create the network
docker network create foodtrucks-net
# start the ES container
docker run -d --name es --net foodtrucks-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
# start the flask app container
docker run -d --net foodtrucks-net -p 5000:5000 --name foodtrucks-web prakhar1989/foodtrucks-web

docker stop foodtricks-web
docker stop es

cd FoodTrucks
./setup-docker.sh

ls
docker-compose --version
docker ps -q
docker stop $(docker ps -q)

docker-compose up
docker stop $(docker ps -q)
docker-compose up -d
docker-compose ps

docker-compose down -v
docker-compose ps

docker network ls
docker network rm foodtrucks-net
docker network ls

docker-compose up -d
docker container ls
docker network ls
docker ps
docker network inspect foodtrucks_default
curl -I 0.0.0.0:5000/hello
curl 0.0.0.0:5000/debug

change add into app.py
# add a new hello route
@app.route('/hello')
def hello():
  return "hello world!"

curl -I 0.0.0.0:5000/hello
docker-compose run web bash
>ls
>grep hello app.py
>exit
curl -I 0.0.0.0:5000/hello

docker-compose down -v
docker-compose up -d
# add or resave a new hello route
@app.route('/hello')
def hello():
  return "hello world!"
curl 0.0.0.0:5000/hello

sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-darwin-amd64-latest
sudo chmod +x /usr/local/bin/ecs-cli
ecs-cli --version


docker pull jupyter/base-notebook
docker run -it --rm --name ds -p 8888:8888 jupyter/base-notebook
docker container ls
docker container stop [ds]

docker run -it --name ds -p 8889:8888 jupyter/base-notebook
docker start ds
docker stop ds
docker ps -a
# start
docker start ds
# attach
docker exec -it ds /bin/bash
# get token
>jupyter notebook list
# view port mapping
# look NetworkSettings:Ports
docker inspect ds
# stop
docker stop ds


```