# Project Description

**Note: The documentation and code are still being improved and updated.**

Local deployment provides an AI service with a REST API, running everything in containers. Complete code and Dockerfile are provided for local image construction, or you can use docker-compose.yml to directly pull and start the pre-built image.

### How to Use

**Method 1: One-Click Startup with Docker Compose**

Most of the images have already been built and uploaded to Docker Hub. The specific image and startup command are specified in the docker-compose file. In the project directory, run:

```
docker compose up
```

**Method 2: Local Image Construction:**

Each project includes a Dockerfile, complete code, and models (download links are provided for large models, please raise an issue if there are any oversights). Run the following command locally:

```
docker build -t res/name:tag .
```

Then, refer to the README.md in the project or the command specified in docker-compose.yml to start the container and provide the service from the image.

### The currently available AI services include:

- ASR (fasterWhisper, FunASR)
- ASR Benchmark Testing
- chatGLM2-6B (Modelscope Launch, Source Code Launch)
- Face Recognition, Face Detection (Compreface)
- Translation (DeeplX)
- Development Image (Basic image used for development)
- Facial Expression Recognition (FER)
- Virtual Human (SadTalker)
- ASR Fine-tuning

### Service Descriptions:

#### compreface

[Compreface github](https://github.com/exadel-inc/CompreFace)
Open-source facial detection service that provides API interfaces within a container. To use this service, you will need the corresponding language SDK and an API key for accessing the service.

#### deeplx

[DeeplX](https://github.com/OwO-Network/DeepLX)
DeepL provides an API interface for local deployment, but it seems that the service still relies on DeepL servers. While it can be used, it may have slow response times for a large number of requests.

#### dev-containers

The base image used for personal development purposes. The initial version of the Dockerfile has been lost, and what remains now are the updated files. Ubuntu with Python 3.8 is being used.
#### fast_whisper

Whisper's Chinese fine-tuned model has been converted to CT operator and all parameters have been deployed as an API interface. The model files are not included.
#### fer_serving

Facial expression recognition. A pure CPU version that is fast and has high accuracy.

#### funasr

Alibaba DAMO Academy has open-sourced an ASR (Automatic Speech Recognition) model. It is deployed as a unified and highly available model that can provide services by switching models through parameters.
## sadtalker
[SadTalker](https://github.com/OpenTalker/SadTalker)
Sadtalker's personal research and development mirror, expanded by the developer.