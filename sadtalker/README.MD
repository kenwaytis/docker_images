### 使用说明
SadTalker的github项目更新会修改很多文件，有可能造成不兼容问题。故每次大版本更新后需要重构镜像。

镜像启动容器命令：
```Shell
docker run --gpus all --name sadtalker -v /path/to/your/checkpoint:/home/SadTalker/checkpoints -v /path/to/your/gfpgan/weights:/home/SadTalker/gfpgan/weights -dit paidax/sadtalker:xxx bash
```
新建容器后待办：
1. 更换wav2lip模型，修改代码。