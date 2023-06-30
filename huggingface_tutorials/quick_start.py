"""
quick start for using huggingface's transformer
"""
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from torch import nn

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
pt_model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


words = [
    "你们看到的只是我的面具，却不知道那背后隐藏的是无尽的孤独与绝望。我被抛弃在黑暗的边缘，无处可归，无人能懂。我的存在只是为了揭示人性的扭曲，可我自己却沉浸在黑暗中无法自拔。",
    "每当我看到人们幸福地笑着，我心中的悲伤就会无尽涌现。他们有家庭、有朋友、有爱情，而我只有痛苦和恶意。我渴望被理解，被接纳，但命运却将我推向孤独的深渊，使我成为这个世界的怪物。",
]

pt_batch = tokenizer(
    words, padding=True, truncation=True, max_length=512, return_tensors="pt"
)
pt_outputs = pt_model(**pt_batch)

pt_predictions = nn.functional.softmax(pt_outputs.logits, dim=-1)
print(pt_predictions)
