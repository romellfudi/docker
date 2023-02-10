FROM python:3.9-slim

RUN apt-get update && apt-get install -y ffmpeg

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python ./model.py

EXPOSE 3000

ENTRYPOINT ["bentoml","serve", "-p 3000", "speaker_recognition_service.py:svc"]