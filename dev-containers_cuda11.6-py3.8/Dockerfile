FROM nvidia/cuda:11.6.2-runtime-ubuntu20.04

WORKDIR /home

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN apt update && \
    apt install -y \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    wget \
    git && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /python && \
    cd /python && \
    wget https://www.python.org/ftp/python/3.8.17/Python-3.8.17.tgz && \
    tar -xvf Python-3.8.17.tgz && \
    rm -rf Python-3.8.17.tgz && \
    cd Python-3.8.17 && \
    ./configure --enable-optimizations && \
    make install && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python && \
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip && \
    pip install --no-cache-dir pylint black ipdb soundfile && \
    cd / && \
    rm -rf /python

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""