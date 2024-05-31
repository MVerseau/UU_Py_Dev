team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 20185.7
if score_1 >= score_2 and team1_time == team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 and team1_time <= team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    "Ничья!"
tasks_total = score_2 + score_1
time_avg = (team1_time + team2_time) / tasks_total

# ИСПОЛЬЗОВАНИЕ %
print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

# ИСПОЛЬЗОВАНИЕ format()
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

# ИСПОЛЬЗОВАНИЕ f-строки
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:3.4} секунды на задачу!.')
