FROM python:3.6-slim
RUN apt-get update -y 
COPY . /app
WORKDIR /app
RUN pip install -U pip && pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]