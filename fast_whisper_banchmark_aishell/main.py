import wave
import time
import os
import base64
import io
from fastapi import FastAPI, status, HTTPException
from faster_whisper import WhisperModel
from pydantic import BaseModel
from typing import BinaryIO, Iterable, List, NamedTuple, Optional, Tuple, Union
from loguru import logger
from pydub import AudioSegment


model_size = "./whisper-large-v2-finetune-ct2"
model = WhisperModel(model_size_or_path=model_size,
                     device="cuda", compute_type="float16")
app = FastAPI()
logger.add("serving_{time}.log", level="INFO", rotation="5 MB", retention=2)


class Audio(BaseModel):
    format: str
    audio: str
    language: str = 'zh'
    task: str = 'transcribe'
    beam_size: int = 5
    best_of: int = 5
    patience: float = 1
    length_penalty: float = 1
    temperature: Union[float, List[float], Tuple[float, ...]] = [
        0.0,
        0.2,
        0.4,
        0.6,
        0.8,
        1.0,
    ]
    compression_ratio_threshold: Optional[float] = 2.4
    log_prob_threshold: Optional[float] = -1.0
    no_speech_threshold: Optional[float] = 0.6
    condition_on_previous_text: bool = True

    prefix: Optional[str] = None
    suppress_blank: bool = True
    suppress_tokens: Optional[List[int]] = [-1]
    without_timestamps: bool = False
    max_initial_timestamp: float = 1.0
    word_timestamps: bool = False
    vad_filter: bool = False,
    vad_parameters: Optional[dict] = None,

    prompt: str = None


def preprocess_audio(audio_b64):
    audio_bytes = base64.b64decode(audio_b64)
    return audio_bytes


def convert_audio_to_wav(binary_data):
    byte_stream = io.BytesIO(binary_data)
    formats = ['mp3', 'wav', 'ogg', 'flv', 'mp4', 'aac']
    audio = None
    for format in formats:
        byte_stream.seek(0)  # reset byte stream position
        try:
            audio = AudioSegment.from_file(byte_stream, format=format)
            break
        except:
            pass
    if audio is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if audio.channels > 1:
        audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    buffer = io.BytesIO()
    audio.export(buffer, format='wav')
    binary_data_resampled = buffer.getvalue()

    return binary_data_resampled


@app.post("/asr")
async def asr(items: Audio):
    result = []
    audio = preprocess_audio(items.audio)
    file_name = f"{int(time.time()*1000)}.{items.format}"
    if items.format == 'pcm':
        with wave.open(file_name, 'wb') as f:
            f.setsampwidth(2)
            f.setnchannels(1)
            f.setframerate(16000)
            f.writeframes(audio)
    else:
        audio = convert_audio_to_wav(audio)
        with open(file_name, 'wb') as f:
            f.write(audio)
    condition_on_previous_text = items.condition_on_previous_text
    initial_prompt = items.prompt
    print('-----------')
    print("condition_on_previous_text:", condition_on_previous_text)
    print("initial_prompt:", initial_prompt)
    print('-----------')
    segments, info = model.transcribe(audio=file_name, language=items.language,
                                      task=items.task, beam_size=items.beam_size,
                                      best_of=items.best_of, patience=items.patience,
                                      length_penalty=items.length_penalty, temperature=items.temperature,
                                      compression_ratio_threshold=items.compression_ratio_threshold,
                                      log_prob_threshold=items.log_prob_threshold, no_speech_threshold=items.no_speech_threshold,
                                      condition_on_previous_text=items.condition_on_previous_text,
                                      prefix=items.prefix, suppress_blank=items.suppress_blank,
                                      suppress_tokens=items.suppress_tokens, without_timestamps=items.without_timestamps,
                                      max_initial_timestamp=items.max_initial_timestamp, word_timestamps=items.word_timestamps,
                                      vad_parameters=items.vad_parameters,
                                      initial_prompt=items.prompt, vad_filter=False
                                      )
    for segment in segments:
        result.append(
            {"text": segment.text, "start": round(segment.start,2), "end": round(segment.end,2)})
    logger.info(f"\nfile name: {file_name}\nresult: {result}")
    os.remove(file_name)
    return result


@app.get("/health")
async def health_check():
    try:
        logger.info("health 200")
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/health/inference")
async def health_check():
    try:
        segments, info = model.transcribe(audio='001.wav', language='zh',
                                          task='transcribe', beam_size=5, initial_prompt="", vad_filter=False)
        print(info)
        return status.HTTP_200_OK

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

