FROM python:3.6-slim
RUN apt-get update -y 
RUN apt-get install tree -y
COPY . /app
WORKDIR /app
RUN cat .bashrc_alias.sh >> ~/.bashrc
RUN pip install -U pip && pip install -r requirements.txt
