FROM paidax/dev-containers:ubuntu22.04-py3.11-v2.3
ENV HTTP_PROXY=http://192.168.100.20:7890
ENV HTTPS_PROXY=http://192.168.100.20:7890
RUN git clone https://github.com/THUDM/ChatGLM2-6B && \
    cd ChatGLM2-6B && \
    pip install -r requirements.txt
WORKDIR /home/ChatGLM2-6B
COPY . .
ENV HTTP_PROXY=""
ENV HTTPS_PROXY=""