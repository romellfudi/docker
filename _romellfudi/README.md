To begin

```sh
docker run --name some-sql -e MYSQL_ROOT_PASSWORD=root -d mysql
docker run --name some-wordpress --link some-sql:mysql -p 8080:80 -d wordpress

docker stack deploy -c stack.yml wordpress-stack
docker stack ls
docker stack rm wordpress-stack

docker-compose up
docker-compose stop

romellfudi
q89D5d05#A!*2&r#DE

boosttag
^hH1k$i)tTH3aX2jzn
```

```sh
docker stop $(docker ps -a -q) &
docker update --restart=no $(docker ps -a -q) &
systemctl restart docker
```

```sh
docker volume ls
docker volume inspect ""

docker exec -it romellfudi_wordpress_1 /bin/sh

docker cp romellfudi_wordpress_1:/var/www/html/wp-content/uploads/wp-static-html-output-1-1542738167-romellfudi.zip .

docker cp romellfudi_wordpress_1:/var/www/html/romellfudi/. romellfudi-wp

docker cp romellfudi_wordpress_1://var/www/html/wp-content/plugins/simply-static/static-files/. romellfudi-static

wget --convert-links --mirror --trust-server-names --adjust-extension http://localhost:8080/

docker ps
docker commit 9db2974fc695 romellfudi/romellfudi-wp:romellfudi_wordpress
docker commit d0c5816bee94 romellfudi/romellfudi-wp:romellfudi_mysql
docker commit romellfudi_wordpress_1
docker commit romellfudi_mysql_1
docker tag 28ae3d7c9802 romellfudi/romellfudi-wp:fudi_wordpress
docker tag 6580781fd6af romellfudi/romellfudi-wp:fudi_mysql
docker push romellfudi/romellfudi-wp:romellfudi_mysql
docker push romellfudi/romellfudi-wp:romellfudi_wordpress
```

