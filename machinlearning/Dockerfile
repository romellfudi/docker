FROM python:2.7

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
ENV DJANGODIR=/webapp

RUN mkdir $DJANGODIR
WORKDIR $DJANGODIR

RUN apt-get update -y

COPY requirements.txt $DJANGODIR/
RUN pip install -r requirements.txt

COPY . $DJANGODIR/