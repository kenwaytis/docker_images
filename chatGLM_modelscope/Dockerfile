FROM registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-cuda11.3.0-py37-torch1.11.0-tf1.15.5-1.6.0
WORKDIR /modelscope/pytorch

RUN pip install --no-cache-dir \
    loguru \
    pydub \
    protobuf==3.20.0 \
    transformers==4.27.1 \
    icetk \
    cpm_kernels \
    fastapi[all] && \
    rm -rf /root/.cache/pip/*

COPY . .
