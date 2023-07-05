import os
import requests
import json
from jiwer import cer
import base64

audio_folder = "/mnt/asr_data"
model_server_url = "192.168.100.18:7890/asr"


# 函数：发送POST请求并获取JSON响应
def get_json_response(model_server_url, audio_file_path):
    with open(audio_file_path, 'rb') as file:
        file_byte = file.read()
    file_b64 = base64.b64encode(file_byte).decode("utf-8")
    body = {"format":"wav",
            "audio":file_b64,
            "language":"zh"
            }
    response = requests.post(model_server_url, json=body)
    return json.loads(response.text)

# 函数：读取字幕文件的第一行
def get_first_line_of_transcript(transcript_file_path):
    with open(transcript_file_path, 'r') as f:
        first_line = f.readline().strip().replace(" ","")
    return first_line

# 函数：计算cer
def calculate_cer(ground_truth, hypothesis):
    return cer(ground_truth, hypothesis)

# 获取音频文件夹的所有音频文件

audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]

# 初始化cer列表
cer_list = []

# 对于每个音频文件
for audio_file in audio_files:
    audio_file_path = os.path.join(audio_folder, audio_file)
    transcript_file_path = os.path.join(audio_folder, audio_file + '.trn')

    # 发送POST请求并获取JSON响应，已解析为字符串
    json_response = get_json_response(model_server_url, audio_file_path)[0]['text']

    # 读取对应的字幕文件的第一行
    ground_truth = get_first_line_of_transcript(transcript_file_path)

    # 计算cer
    hypothesis = json_response
    current_cer = calculate_cer(ground_truth, hypothesis)

    # 将该cer添加到cer列表中
    cer_list.append(current_cer)

# 计算总的cer
total_cer = sum(cer_list) / len(cer_list)

# 输出总的cer
print(f"Total cer: {total_cer}")
