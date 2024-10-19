from collections import defaultdict
from Module15_8 import ACTIONS, NUM_EPISODES,MAX_STEPS_PER_EPISODE,EPSILON,epsilon_greedy_action, step,DISCOUNT_FACTOR,LEARNING_RATE
from Module15_8_vis_pol import visualize_policy

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

# Показать последнюю политику
visualize_policy(Q)