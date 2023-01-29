
docker-compose build
docker-compose run -it python bash

python hello_world.py


py src/app.py
docker build . -t datascience
docker run -it datascience bash
docker run --rm -it -v $(pwd):/code -p 8888:8888 datascience bash
docker rename {} datascience
docker start datascience
docker stop datascience
docker exec -it datascience bash
nosetests --with-watch --rednose --nologcapture
nosetests --rednose --nologcapture