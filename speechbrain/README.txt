Speechbrain

docker build . -t speech_nova
docker run --rm -it -p 7860:7860 speech_nova

docker tag speech_nova romellfudi/speech_nova:1.0
docker push romellfudi/speech_nova:1.0

docker pull romellfudi/speech_nova:1.0
docker run -d -p 7860:7860 romellfudi/speech_nova:1.0