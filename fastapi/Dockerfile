FROM paidax/dev-containers:ubuntu-py3.8-v1.0

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN pip install "fastapi[all]" && \
    mkdir -p /home/fastapi

WORKDIR /home/fastapi

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""