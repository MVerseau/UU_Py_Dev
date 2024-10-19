import numpy as np

# Функция активации (шаговая функция)
def step_function(x):
    return np.where(x >= 0, 1, 0)

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=10):
        self.W = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, x):

        # print(f'{np.dot(self.W, x)=}')
        return step_function(np.dot(self.W, x))

    def train(self, X, y):
        for i in range(self.epochs):
            print()
            print(f'Epoch {i}')
            for xi, target in zip(X, y):
                print(f'{xi=}, {target=}')
                xi = np.insert(xi, 0, 1)  # Вставка смещения (bias)
                print(f'{xi=}, {target=}')
                print(f'{self.W=}')
                prediction = self.predict(xi)
                print(f'{prediction=}')
                print(f'{self.learning_rate}*({target}-{prediction})*{xi}={self.learning_rate*(target-prediction)}*{xi}')
                self.W += self.learning_rate * (target - prediction) * xi
                print(f'{self.W=}')
                print()
            print()
            # break



# Данные для обучения (И, ИЛИ)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Операция И (AND)

perceptron = Perceptron(input_size=2)
perceptron.train(X, y)

# Тестирование
for xi in X:
    xi_with_bias = np.insert(xi, 0, 1)  # Вставка смещения (bias) для тестирования
    print(f"{xi} -> {perceptron.predict(xi_with_bias)}")