# 项目说明

Note: The documentation and code are still being improved and updated.

本地部署提供REST API的AI服务，一切运行在容器中。同时提供完整代码和Dockerfile进行本地镜像的构建，或使用docker-compose.yml直接拉取我构建好的镜像一键启动。

### 如何使用

**方式一：docker-compose一键启动**

大多数镜像我已经构建并上传至docker hub，在docker compose中已指定到具体的镜像和启动命令。在具体的项目路径中运行：

```bash
docker compose up
```

**方式二：本地构建镜像：**

每个项目中包含Dockerfile和完整代码与模型（大型模型会额外提供下载地址，如有疏忽可以提issuse）,在本地运行：

```shell
docker build -t res/name:tag .
```

随后根据项目内的README.md或docker-compose.yml中的command从镜像中启动容器提供服务。

### 目前包括的AI服务有：

- ASR（fasterWhisper、FunASR）

- ASR Benchmark测试

- chatGLM2-6B（modelscope启动、源代码启动）
- 人脸识别 人脸检测（Compreface）、翻译（DeeplX）
- 开发镜像（我用于开发的基础镜像）
- 人脸表情识别（FER）
- 虚拟人（SadTalker）
- ASR微调

### 服务说明

#### compreface

开源人脸检测服务，提供容器内的API接口。要使用此服务，您需要相应的语言SDK和访问服务的API密钥。

#### deeplx

DeepL提供了用于本地部署的API接口，但似乎该服务仍依赖于DeepL服务器。虽然可以使用，但对于大量请求可能响应时间较慢。

#### dev-containers

用于个人开发目的的基础映像。最初版本的Dockerfile已丢失，现在剩下的是更新后的文件。正在使用带有Python 3.8的Ubuntu。

#### fast_whisper

Whisper的中文微调模型已转换为CT运算符，并将所有参数部署为API接口。模型文件未包含在内。

#### fer_serving

面部表情识别。纯CPU版本，速度快且准确度高。

#### funasr

阿里巴巴达摩院开源了一种自动语音识别（ASR）模型。它以统一且高可用的模型部署，可以通过参数切换模型来提供服务。

#### sadtalker

Sadtalker的个人研发镜像，由开发人员进行扩展。
