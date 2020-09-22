FROM python:3
RUN pip install -y --upgrade pip 
RUN pip install -y --upgrade virtualenv
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]