from transformers import pipeline

generator = pipeline(model="openai/whisper-base", device_map="auto")

print(generator("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"))
