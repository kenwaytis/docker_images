FROM paidax/dev-containers:ubuntu22.04-py3.11-v2.3
ARG HTTP_PROXY

ENV HTTP_PROXY=${HTTP_PROXY}
ENV HTTPS_PROXY=${HTTP_PROXY}
RUN git clone https://github.com/THUDM/ChatGLM2-6B && \
    cd ChatGLM2-6B && \
    pip install -r requirements.txt
WORKDIR /home/ChatGLM2-6B
COPY . .
ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""