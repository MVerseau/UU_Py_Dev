import numpy as np

# Параметры
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 1000
grid_size = 5
actions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
rewards = np.zeros((grid_size, grid_size))

rewards[4, 4] = 1
# print(rewards)
# Инициализация Q-таблицы
Q = np.zeros((grid_size, grid_size, 4))


# Функции для выбора действий и обновления Q-таблицы
def choose_action(state):
    a = np.random.rand()
    # print(a)
    if a < epsilon:
        # print(f'{np.random.rand() < epsilon=}')
        return np.random.randint(4)
    else:
        return np.argmax(Q[state])


def step(state, action, done):
    row, col = state
    if action == 0 and row > 0:
        row -= 1
    elif action == 1 and row < grid_size - 1:
        row += 1
    elif action == 2 and col > 0:
        col -= 1
    elif action == 3 and col < grid_size - 1:
        col += 1
    new_state = (row, col)
    if new_state == (grid_size - 1, grid_size - 1):
        reward = 1
        done = True
    else:
        reward = -0.1
    return new_state, reward, done


def update_q(state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state])
    td_target = reward + gamma * Q[next_state][best_next_action]
    td_error = td_target - Q[state][action]
    Q[state][action] += alpha * td_error


# Обучение агента
for episode in range(episodes):
    state = (0, 0)
    done = False
    while not done:
        action = choose_action(state)
        next_state, reward, done = step(state, action, done)
        update_q(state, action, reward, next_state)
        state = next_state

# Визуализация политики
policy = np.argmax(Q, axis=2)
print("Оптимальная политика:")
print(policy)

import matplotlib.pyplot as plt


value_function = np.max(Q, axis=2)


def color(item, range):
    return ['white', 'black'][np.round(item) == np.round(range[1])]


plt.figure(figsize=(8, 8))


plt.subplot(1, 2, 1)
plt.title('Политика')
plt.imshow(policy)

for i in range(grid_size):
    for j in range(grid_size):
        plt.text(j, i, policy[i, j], color=color(item=policy[i, j], range=(np.min(policy), np.max(policy))))

plt.subplot(1, 2, 2)
plt.title('Функция ценности')
plt.imshow(value_function)
for i in range(grid_size):
    for j in range(grid_size):
        plt.text(j, i, round(value_function[i, j], 2), ha='center', color=color(item=value_function[i, j], range=(np.min(value_function), np.max(value_function))))

plt.show()
