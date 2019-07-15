The easiest way to start a local instance of webauthn.io is to use the image on Docker Hub:

> docker run --rm -p 9005:9005 duolabs/webauthn.io

To run a local instance of webauthn.io in a Docker container, start by building the container image:

> docker build -t webauthn.io .

Then, run the container, exposing port 9005:

> docker run --rm -p 9005:9005 webauthn.io

After the container launches, you can navigate to localhost:9005 to see the application.
```