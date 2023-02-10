bentoml serve -p 3000 speaker_recognition_service.py:svc

// activate python environment

pip install -r ./requirements.txt
python ./model.py
bentoml serve -p 3000 speaker_recognition_service.py:svc
bentoml build
bentoml containerize voices_belong_to_same_person:latest
docker run -it --rm -p 3000:3000 voices_belong_to_same_person:latest


ref: https://github.com/bentoml/BentoML/tree/main/examples/custom_python_model/simple_pickable_model



----------------
# Simple Python model via bentoml.picklable_model
0. Install dependencies:

```bash
pip install -r ./requirements.txt
```

1. Save the simple python model:

```bash
python ./model.py
```

2. Run the service:

```bash
bentoml serve service.py:svc
```

3. Send test request:

```bash
curl -X POST -H "content-type: application/json" --data "[1,2,3,4,5]" http://127.0.0.1:3000/square
```

4. Build Bento

```bash
bentoml build
```

5. Build docker image

```bash
bentoml containerize simple_square_svc:latest
```

```bash
docker run -p 3000:3000 simple_square_svc:ixbjlmqg3cjbluqj
```