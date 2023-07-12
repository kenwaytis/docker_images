FROM paidax/dev-containers:ubuntu-py3.8-v1.0

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 && \
    git clone https://github.com/yeyupiaoling/Whisper-Finetune.git && \
    cd Whisper-Finetune && \
    python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/Whisper-Finetune


ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""