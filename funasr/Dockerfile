FROM registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-cuda11.3.0-py37-torch1.11.0-tf1.15.5-1.6.0
ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890
WORKDIR /modelscope/pytorch

RUN pip install --no-cache-dir \
    loguru \
    fastapi[all] && \
    rm -rf /root/.cache/pip/*

COPY . .

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""