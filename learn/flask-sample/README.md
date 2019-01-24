>app.py
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
```

>requirements.txt 
```txt
flask==0.10.1
```

>Dockerfile
```dockerfile
ROM ubuntu:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

```sh
docker build -t flask-sample-one:latest .
docker run --name flask -d -p 5000:5000 flask-sample-one
docker start flask
docker ps -a
```

```sh
docker stop flask
docker rm flask
```


