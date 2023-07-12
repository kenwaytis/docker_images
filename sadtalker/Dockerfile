FROM paidax/dev-containers:ubuntu-py3.8

WORKDIR /home

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN apt update -y && \
    apt install -y \
    liblzma-dev \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Winfredy/SadTalker.git && \
    pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113 && \
    cd SadTalker && \
    mkdir checkpoints && \
    mkdir -p gfpgan/weights && \
    pip install -r requirements.txt && \
    pip install backports.lzma && \
    rm -rf /root/.cache/pip/*  # 清除pip缓存

# Insert the modified lines here
RUN sed -i 's/from _lzma import \*/try:\n    from _lzma import *\n    from _lzma import _encode_filter_properties, _decode_filter_properties\nexcept ImportError:\n    print("using backports.lzma")\n    from backports.lzma import *\n    from backports.lzma import _encode_filter_properties, _decode_filter_properties/' /usr/local/lib/python3.8/lzma.py && \
    sed -i '/from _lzma import _encode_filter_properties, _decode_filter_properties/d' /usr/local/lib/python3.8/lzma.py

WORKDIR /home/SadTalker

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""

RUN apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
