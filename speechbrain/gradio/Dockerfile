FROM python:3.9-slim

RUN apt-get update && apt-get install -y ffmpeg

COPY . /app
WORKDIR /app
# RUN pip3 install git+https://github.com/speechbrain/speechbrain.git
RUN pip3 install -r requirements.txt

EXPOSE 7860

ENTRYPOINT ["python", "nova.py"]