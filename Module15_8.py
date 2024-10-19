import numpy as np
import random
from collections import defaultdict

# Параметры среды
GRID_SIZE = 5
NUM_EPISODES = 500
MAX_STEPS_PER_EPISODE = 100

# Параметры Q-Learning
LEARNING_RATE = 0.1  # Скорость обучения alpha
DISCOUNT_FACTOR = 0.99  # Дисконтирующий фактор gamma
EPSILON = 1.0  # Вероятность выбора случайного действия (всегда случайное действие)

# Определение наград и действий
REWARDS = np.zeros((GRID_SIZE, GRID_SIZE))

REWARDS[4, 4] = 1  # Целевая клетка с наградой

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

# Функция для выбора следующего действия на основе epsilon-greedy политики
def epsilon_greedy_action(Q, state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.choice(ACTIONS)
    else:
        return max(ACTIONS, key=lambda action: Q[state][action])

# Функция для выполнения действия и получения нового состояния и награды
def step(state, action):
    row, col = state
    if action == "UP" and row > 0:
        row -= 1
    elif action == "DOWN" and row < GRID_SIZE - 1:
        row += 1
    elif action == "LEFT" and col > 0:
        col -= 1
    elif action == "RIGHT" and col < GRID_SIZE - 1:
        col += 1
    new_state = (row, col)
    reward = REWARDS[row, col]
    return new_state, reward

# Инициализация Q-таблицы
Q = defaultdict(lambda: {action: 0 for action in ACTIONS})


# Обучение агента с использованием Q-Learning
for episode in range(NUM_EPISODES):
    state = (0, 0)
    for step_num in range(MAX_STEPS_PER_EPISODE):
        action = epsilon_greedy_action(Q, state, EPSILON)
        new_state, reward = step(state, action)

        # Обновление Q-значений
        best_next_action = max(ACTIONS, key=lambda action: Q[new_state][action])
        td_target = reward + DISCOUNT_FACTOR * Q[new_state][best_next_action]
        td_error = td_target - Q[state][action]
        Q[state][action] += LEARNING_RATE * td_error

        state = new_state

# Вывод Q-таблицы (для отладки или анализа)
for state in Q:
    print(f"State {state}: {Q[state]}")
