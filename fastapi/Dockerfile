FROM paidax/dev-containers:ubuntu-py3.8-v1.0

ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890

RUN pip install "fastapi[all]" && \
    mkdir -p /home/fastapi

WORKDIR /home/fastapi

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""