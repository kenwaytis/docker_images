FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04
WORKDIR /home
ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN apt update -y && \
    apt install -y \
    python3.11 \
    wget \
    git && \
    rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3.11 /usr/local/bin/python && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm -rf ./*
RUN apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""