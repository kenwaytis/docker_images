from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from modelscope.utils.logger import get_logger
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from loguru import logger as log
from pydub import AudioSegment
import io
import base64
import requests

app = FastAPI()
log.add("serving_{time}.log", level="INFO", rotation="5 MB", retention=2)
model = pipeline(task=Tasks.chat, model='ZhipuAI/ChatGLM-6B', model_revision='v1.0.16',device_map='auto')


class Audio(BaseModel):
    input: str

def format_input(input):
    return {'text':input, 'history': []}


@app.post("/chat", summary="chatGLM")
async def predict(items: Audio):
    result = model(format_input(items.input))
    log.info(result)
    return result

@app.get("/health")
async def health_check():
    try:
        log.info("health 200")
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@app.get("/health/inference")
async def health_check():
    try:
        result = model({'text':'你好', 'history': []})
        log.info("health 200")
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)