FROM python:3.9-slim

RUN apt-get update && apt-get install -y

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py"]