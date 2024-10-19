import numpy as np

# Параметры
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 1000
grid_size = 5
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Определение наград и действий
rewards = np.zeros((grid_size, grid_size))
rewards[4, 4] = 1  # Целевая клетка с наградой


# Инициализация Q-таблицы
Q = np.zeros((grid_size, grid_size, 4))
# print(Q)



# Функции для выбора действий и обновления Q-таблицы
def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(4)
    else:
        return np.argmax(Q[state])


# Функция для выполнения действия и получения нового состояния и награды
def step(state, action):
    # print(state, action)
    next_state = (state[0] + actions[action][0], state[1] + actions[action][1])
    if next_state[0] < 0 or next_state[0] >= grid_size or next_state[1] < 0 or next_state[1] >= grid_size:
        next_state = state  # оставаться на месте, если выходит за пределы
    reward = 1 if next_state == (grid_size-1, grid_size-1) else -0.1
    done = next_state == (grid_size-1, grid_size-1)

    # print(next_state,done)
    return next_state, reward, done


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
        next_state, reward, done = step(state, action)
        update_q(state, action, reward, next_state)
        state = next_state
        # print(Q[0])

    # break

# Визуализация политики
policy = np.argmax(Q, axis=2)
print("Оптимальная политика:")
print(policy)

# print(Q)