FROM paidax/dev-containers:ubuntu-py3.8

WORKDIR /home

ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}

RUN pip install openai

ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""