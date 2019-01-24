```sh
docker-compose up
docker ps -a

docker rename flask_compose_sample_web_1 flask_compose
docker stop flask_compose

docker commit flask_compose flask-compose
docker run -p 8888:8888 -td flask-compose


```