import os
import asyncio
import websockets
import json
import base64
from jiwer import cer
from loguru import logger
import jionlp as jio
import ssl
import re

ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

audio_folder = "/mnt/asr_data"
model_server_url = "wss://192.168.100.18:10095"  # WebSocket URL

def get_first_line_of_transcript(transcript_file_path):
    with open(transcript_file_path, 'r') as f:
        first_line = f.readline().strip().replace(" ","")
    return first_line

def calculate_cer(ground_truth, hypothesis):
    return cer(ground_truth, hypothesis)

audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]

cer_list = []

logger.info(f"Processing {len(audio_files)} audio files...")

async def get_asr_result(audio_file_path):
    async with websockets.connect(model_server_url,ssl=ssl_context) as ws:
        wav_name = os.path.basename(audio_file_path)
        init_message = {"mode": "offline", "wav_name": wav_name, "is_speaking": True}
        await ws.send(json.dumps(init_message))

        # 发送wav数据
        with open(audio_file_path, 'rb') as file:
            file_byte = file.read()
        await ws.send(file_byte)

        # 发送结束标志
        end_message = {"is_speaking": False}
        await ws.send(json.dumps(end_message))

        response = await ws.recv()
        return response
    
def keep_only_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fff]+')
    chinese_chars = re.findall(pattern, text)
    return ''.join(chinese_chars)

# 对于每个音频文件
for i, audio_file in enumerate(audio_files, 1):
    logger.info(f"Processing file {i} of {len(audio_files)}: {audio_file}")
    audio_file_path = os.path.join(audio_folder, audio_file)
    transcript_file_path = os.path.join(audio_folder, audio_file + '.trn')

    # 获取ASR结果
    response = asyncio.get_event_loop().run_until_complete(get_asr_result(audio_file_path))
    json_response = keep_only_chinese(json.loads(response)["text"])

    # 读取对应的字幕文件的第一行
    ground_truth = get_first_line_of_transcript(transcript_file_path)
    if not jio.check_any_arabic_num(ground_truth) and not jio.check_any_arabic_num(json_response):     
        # 计算cer
        hypothesis = json_response
        current_cer = calculate_cer(ground_truth, hypothesis)
        logger.info(f"\nground_truth: {ground_truth}\nhypothesis:   {hypothesis}\ncurrent cer: {current_cer}")

        # 将该cer添加到cer列表中
        cer_list.append(current_cer)

# 计算总的cer
total_cer = sum(cer_list) / len(cer_list)

# 输出总的cer
logger.info(f"Total cer: {total_cer}")
