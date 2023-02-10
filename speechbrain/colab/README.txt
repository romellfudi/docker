bentoml serve -p 3000 speaker_recognition_service.py:svc

bentoml build
bentoml containerize speaker_recognition_service:latest
docker run -p 3000:3000 speaker_recognition_service:ixbjlmqg3cjbluqjixx


ref: https://github.com/bentoml/BentoML/tree/main/examples/custom_python_model/simple_pickable_model