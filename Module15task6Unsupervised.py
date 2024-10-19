from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Загружаем датасет
wine = load_wine()
# print(wine.data)
print(wine['DESCR'])

X = wine.data

# Обучаем модель K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Предсказываем кластеры
clusters = kmeans.predict(X)

# центры кластеров
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Визуализируем результаты кластеризации
plt.scatter(X[:, -4], X[:, -1], c=clusters, cmap='viridis', marker='o')
plt.scatter(cluster_centers[:, -4], cluster_centers[:, -1], color='red', marker='X', s=200, label='Cluster Centers')
# plt.plot(X[:, -4], X[:, -1], color='red',linestyle='dashed', marker='.')
plt.title('K-means Clustering of Wine Dataset')
plt.xlabel('Colour Intensity')
plt.ylabel('Proline')
plt.show()
