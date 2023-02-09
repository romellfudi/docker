FROM python:3.9-slim

RUN pip3 install --upgrade pip
RUN apt-get update && pip install numpy && apt-get install git gcc g++ -y
# RUN yum install gcc-c++

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/slundberg/shap.git

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py"]