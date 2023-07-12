FROM paidax/dev-containers:ubuntu22.04-py3.11-v2.3

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN pip install \
    jiwer \
    websockets \
    loguru
