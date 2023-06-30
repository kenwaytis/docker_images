import random
import jieba
from loguru import logger

def build_hmm(data):
    hidden_states = set(data)
    observed_states = set(data)
    initial_probabilities = {}
    transition_probabilities = {}
    observation_probabilities = {}

    for i in range(len(data)-1):
        current_hidden_state = data[i]
        current_observed_state = data[i]
        next_hidden_state = data[i+1]

        # 更新初始状态概率分布
        if current_hidden_state not in initial_probabilities:
            initial_probabilities[current_hidden_state] = 0
        initial_probabilities[current_hidden_state] += 1

        # 更新状态转移概率矩阵
        if current_hidden_state not in transition_probabilities:
            transition_probabilities[current_hidden_state] = {}
        if next_hidden_state not in transition_probabilities[current_hidden_state]:
            transition_probabilities[current_hidden_state][next_hidden_state] = 0
        transition_probabilities[current_hidden_state][next_hidden_state] += 1

        # 更新观察概率矩阵
        if current_hidden_state not in observation_probabilities:
            observation_probabilities[current_hidden_state] = {}
        if current_observed_state not in observation_probabilities[current_hidden_state]:
            observation_probabilities[current_hidden_state][current_observed_state] = 0
        observation_probabilities[current_hidden_state][current_observed_state] += 1

    # 归一化概率
    total_samples = len(data) - 1
    for state in initial_probabilities:
        initial_probabilities[state] /= total_samples
    for state in transition_probabilities:
        total_transitions = sum(transition_probabilities[state].values())
        for next_state in transition_probabilities[state]:
            transition_probabilities[state][next_state] /= total_transitions
    for state in observation_probabilities:
        total_observations = sum(observation_probabilities[state].values())
        for observed_state in observation_probabilities[state]:
            observation_probabilities[state][observed_state] /= total_observations

    return {
        'hidden_states': hidden_states,
        'observed_states': observed_states,
        'initial_probabilities': initial_probabilities,
        'transition_probabilities': transition_probabilities,
        'observation_probabilities': observation_probabilities
    }

def generate_sequence(hmm, length):
    hidden_states = hmm['hidden_states']
    initial_probabilities = hmm['initial_probabilities']
    transition_probabilities = hmm['transition_probabilities']
    observation_probabilities = hmm['observation_probabilities']
    observed_states = hmm['observed_states']

    sequence = []
    current_hidden_state = random.choice(list(hidden_states))

    for _ in range(length):
        sequence.append(current_hidden_state)
        next_hidden_state = random.choices(
            list(hidden_states), 
            weights=[transition_probabilities[current_hidden_state].get(state, 0) for state in hidden_states]
        )[0]
        current_hidden_state = next_hidden_state

    return sequence

with open("text", "r", encoding="utf-8") as file:
    text = file.read().replace("\n", "").strip()

words = jieba.lcut(text, cut_all=True)

hmm = build_hmm(words)

generated_sequence = generate_sequence(hmm, 150)

logger.info(f"cut words: {words}")
logger.info(f"hmm: {hmm}")
logger.info(f"generated_sequence: {''.join(generated_sequence)}")
