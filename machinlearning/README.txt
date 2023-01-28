
docker-compose build
docker-compose run -it python bash

python hello_world.py


py src/app.py
docker build . -t datascience
ocker run -it -v $(pwd):/code -p 8888:8888 datascience bash
nosetests --with-watch --rednose --nologcapture