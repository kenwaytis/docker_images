FROM paidax/dev-containers:ubuntu-py3.8

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN apt update -y && \
    apt install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    liblzma-dev && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*  /tmp/* /var/tmp/* && \
    pip install -v \
    backports.lzma && \
    rm -rf /root/.cache/pip/*
RUN sed -i 's/from _lzma import \*/try:\n    from _lzma import *\n    from _lzma import _encode_filter_properties, _decode_filter_properties\nexcept ImportError:\n    print("using backports.lzma")\n    from backports.lzma import *\n    from backports.lzma import _encode_filter_properties, _decode_filter_properties/' /usr/local/lib/python3.8/lzma.py && \
    sed -i '/from _lzma import _encode_filter_properties, _decode_filter_properties/d' /usr/local/lib/python3.8/lzma.py

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""
