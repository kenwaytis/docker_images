FROM paidax/dev-containers:cuda11.6-py3.8

ARG HTTP_PROXY
ARG HTTPS_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && \
    apt install -y \
    ffmpeg && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Winfredy/SadTalker.git && \
    pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113 && \
    cd SadTalker && \
    mkdir checkpoints && \
    mkdir -p gfpgan/weights && \
    pip install -r requirements.txt && \
    pip install \ 
    fastapi[all] \
    onnxruntime-gpu \
    loguru && \
    rm -rf /root/.cache/pip/*  # 清除pip缓存

WORKDIR /home/SadTalker

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""
