FROM paidax/dev-containers:ubuntu-py3.8

WORKDIR /home

ENV HTTP_PROXY=http://192.168.100.18:7890
ENV HTTPS_PROXY=http://192.168.100.18:7890

RUN pip install openai

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""