###############################################
# 废弃
# FUCK NVIDIA
###############################################
FROM ubuntu:20.04
ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890
ENV DEBIAN_FRONTEND=noninteractive

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
    software-properties-common \
    tzdata \
    wget \
    git && \
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
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

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin && \
    mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub && \
    add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" && \
    apt update && \
    apt -y install cuda
RUN wget https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.2/local_installers/11.x/cudnn-local-repo-ubuntu2004-8.9.2.26_1.0-1_amd64.deb && \
    dpkg -i cudnn-local-repo-ubuntu2004-8.9.2.26_1.0-1_amd64.deb && \
    cp /var/cudnn-local-repo-*/cudnn-local-*-keyring.gpg /usr/share/keyrings/ && \
    apt update && \
    apt -y install \
    libcudnn8=8.9.2.26_1.0-1+cuda11.6 \
    libcudnn8-dev=8.9.2.26_1.0-1+cuda11.6






WORKDIR /home

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""
    