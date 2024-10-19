#import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Загружаем датасет
wine = load_wine()
for i in set(wine.target):
    print(f'Class {i} elems: {list(wine.target).count(i)}')
    # print(list(wine.target).count(1))
    # print(list(wine.target).count(2))
print(len(wine.target))
# X = wine.data
# y = wine.target
#
# # Разделение не обучающую и тестовую части
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#
# # Обучение логистическая регрессия
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)
#
# # Предсказание на тестовых данных
# y_pred = model.predict(X_test)
#
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)
# print("Classification Report:")
# print(classification_report(y_test, y_pred))
