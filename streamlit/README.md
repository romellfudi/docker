Streamlit

docker build . -t streamlit_fake
docker run --rm -it -p 8501:8501 streamlit_fake
docker run --rm -it -p 8501:8501 streamlit

// Dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ENTRYPOINT ["streamlit", "run", "app.py", "--port=8501", "--server.address=0.0.0.0"]