"""
Test file.
This is just for testing different functions etc. before implementing them to the real files
"""

import numpy as np

from assignment02 import *
from matplotlib import pyplot as plt
from sklearn.cluster import kmeans_plusplus
from sklearn.datasets import make_blobs

# X, y_true = make_blobs(
#     n_samples=10000, centers=10, cluster_std=1.00, random_state=0
# )
# print(X)
# X = X[:, ::-1]
# print(X)

# centers_init, indices = kmeans_plusplus(X, n_clusters=10, random_state=0)
#
# plt.figure(1)
# colors = ["#FF00FF", "#FF9C34", "#4E9A06", "m", "#4EACC5", "#808080", "#0000FF", "#FFFF00", "#000000", "#008000"]
#
# for k, col in enumerate(colors):
#     cluster_data = y_true == k
#     plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)
#
# plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
# plt.xticks([])
# plt.yticks([])
# plt.show()


# X = np.array([[1, 2],
#               [1, 4],
#               [1, 0],
#               [10, 2],
#               [10, 4],
#               [10, 0]])
# centers, indices = kmeans_plusplus(X, n_clusters=2, random_state=0)
# print(centers)
# print(indices)


df = get_iris_dataset()
pca = pca_transformation(df)
# print(df.shape)


# df = df[['sepal length (cm)', 'sepal width (cm)']]
# print(df.shape)


# plt.figure(1)
# plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], color='blue')
# plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], color='green')
# plt.scatter(df['sepal length (cm)'], df['petal width (cm)'], color='yellow')
# plt.scatter(df['sepal width (cm)'], df['petal length (cm)'], color='red')
# plt.scatter(df['sepal width (cm)'], df['petal width (cm)'], color='black')
# plt.scatter(df['petal length (cm)'], df['petal width (cm)'], color='grey')

# plt.figure(2)
# plt.xlabel('K')
# plt.plot(*elbow_method(pca))
# plt.show()

# df.hist()

# print(len(df))

# sns.displot(df, x='petal length (cm)')


# Test difference between KMeans and KMeans++
# K-Means++ (KMeans initialization)
kmeans_pp = KMeans(n_clusters=3, max_iter=1000, init='k-means++').fit(df)
centroids = kmeans_pp.cluster_centers_

plt.figure(2)
plt.title('KMeans++')
plt.scatter(pca['principal component 1'], pca['principal component 2'], c=kmeans_pp.labels_.astype(float), s=50, alpha=.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

# K-Means
kmeans = KMeans(n_clusters=3, max_iter=1000, init='random').fit(pca)
center = kmeans.cluster_centers_

plt.figure(3)
plt.title('KMeans')
plt.scatter(pca['principal component 1'], pca['principal component 2'], c=kmeans.labels_.astype(float), s=50, alpha=.5)
plt.scatter(center[:, 0], center[:, 1], c='red', s=50)

plt.show()
