
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

// To create a temporal container and expose directly, you must add the following lines to the Dockerfile:
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=8888", "--no-browser", "--allow-root"]
CMD python ./index.py
// to run the container:
docker run -rm -it -p 8888:8888 datascience

// Jupyer in one lines
docker run -it -p 8888:8888 jupyter/all-spark-notebook:4.0 ipython notebook --ip=0.0.0.0 --port=8888



RUN apt-get update && apt-get install -yqq --no-install-recommends  ffmpeg

RUN pip3 install --no-dependencies -r requirements.txt