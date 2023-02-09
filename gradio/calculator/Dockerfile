FROM python:3.9-slim

RUN apt-get update && apt-get install -y

COPY . /app
WORKDIR /app
RUN pip3 install gradio

EXPOSE 7000

HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

ENTRYPOINT ["python", "app.py"]