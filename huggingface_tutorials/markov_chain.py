"""
a simple demo for markov chain in generate chinese sentence
"""
import random
import jieba
from loguru import logger


def build_markov_chain(data):
    markov_chain = {}
    for i in range(len(data) - 1):
        current_state = data[i]
        next_state = data[i + 1]
        if current_state in markov_chain:
            markov_chain[current_state].append(next_state)
        else:
            markov_chain[current_state] = [next_state]
    return markov_chain


def generate_sequence(markov_chain, initial_state, length):
    sequence = [initial_state]
    current_state = initial_state
    for _ in range(length - 1):
        if current_state in markov_chain:
            next_state = random.choice(markov_chain[current_state])
            sequence.append(next_state)
            current_state = next_state
        else:
            break
    return sequence


with open("text", "r", encoding="utf-8") as file:
    text = file.read().replace("\n", "").strip()

words = jieba.lcut(text, cut_all=True)

markov_chain = build_markov_chain(words)
initial_state = random.choice(words)
generated_sequence = generate_sequence(markov_chain, initial_state, 150)

logger.info(f"cut words: {words}")
logger.info(f"markov_chain: {markov_chain}")
logger.info(f"generated_sequence: {''.join(generated_sequence)}")
