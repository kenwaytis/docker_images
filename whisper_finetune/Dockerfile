FROM paidax/dev-containers:ubuntu-py3.8-v1.0

ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890

RUN pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 && \
    git clone https://github.com/yeyupiaoling/Whisper-Finetune.git && \
    cd Whisper-Finetune && \
    python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/Whisper-Finetune


ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""