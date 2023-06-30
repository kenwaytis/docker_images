FROM paidax/dev-containers:ubuntu22.04-py3.11-v2.3

ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890

RUN pip install transformers \
    datasets \
    torch \
    tensorflow \
    flax \
    xformers \
    librosa \
    soundfile
