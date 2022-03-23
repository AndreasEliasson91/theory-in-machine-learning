"""
Test file.
This is just for testing functions etc. before implementing them to the real files
"""

import numpy as np
import pandas as pd
import seaborn as sns
import time as t

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans, kmeans_plusplus
from sklearn.datasets import load_iris, make_blobs
from sklearn.decomposition import PCA

# X, y_true = make_blobs(
#     n_samples=10000, centers=10, cluster_std=1.00, random_state=0
# )
# print(X)
# # X = X[:, ::-1]
# # print(X)
#
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
#
#
# X = np.array([[1, 2],
#               [1, 4],
#               [1, 0],
#               [10, 2],
#               [10, 4],
#               [10, 0]])
# centers, indices = kmeans_plusplus(X, n_clusters=2, random_state=0)
# print(centers)
# print(indices)


def get_iris_dataset() -> pd.DataFrame:
    """
    Loads the iris data set and converts it to a Pandas Data Frame
    :return: pandas data frame
    """
    iris_data = load_iris()
    return pd.DataFrame(iris_data.data, columns=iris_data.feature_names)


def pca_transformation(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a data frame and transforms it to a principal component analysis data frame,
    containing to 2 principal components
    :param data: pandas data frame, the data to transform to PCA data frame
    :return: pandas data frame
    """
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    return pd.DataFrame(data=principal_components,
                        columns=['principal component 1', 'principal component 2'])


def elbow_method(data: pd.DataFrame) -> (range, list):
    """
    Takes a data frame and iterates a given number of times to get the most optimized number of
    clusters for the data points in the data frame
    :param data: pandas data frame, the data frame to test the best k-value on
    :return: tuple, the range of k-values tested and a list of the k-means inertia
    """
    sse = []
    k_range = range(1, 10)

    for k in k_range:
        k_means = KMeans(n_clusters=k)
        k_means.fit(data)
        sse.append(k_means.inertia_)

    return k_range, sse


def time_kmeans(data: pd.DataFrame, clusters: int, iterations: int) -> float:
    """
    Timer function.
    Takes a data frame and calculates the time it takes for the KMeans to calculate
    the result
    :param data: pandas data frame, the data frame to time
    :param clusters: int, number of clusters to test the kmeans with
    :param iterations: int, maximal number of iterations to test
    :return: float, the time (in seconds) that the kmeans takes to calculate the data frame
    """
    start = t.perf_counter()
    kmeans = KMeans(n_clusters=clusters, max_iter=iterations, init='random').fit(data)
    stop = t.perf_counter()

    return stop - start


df = get_iris_dataset()
# print(df.shape)

pca = pca_transformation(df)


# df = df[['sepal length (cm)', 'sepal width (cm)']]
# print(df.shape)


# # K-Means++ (KMeans initialization)
# kmeans_pp = KMeans(n_clusters=3, max_iter=1000, init='k-means++').fit(df)
# centroids = kmeans_pp.cluster_centers_
#
# plt.figure(2)
# plt.title('KMeans++')
# plt.scatter(pca['principal component 1'], pca['principal component 2'], c=kmeans_pp.labels_.astype(float), s=50, alpha=.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
#

# K-Means
kmeans = KMeans(n_clusters=3, max_iter=1000, init='random').fit(pca)
center = kmeans.cluster_centers_

plt.figure(3)
plt.title('KMeans')
plt.scatter(pca['principal component 1'], pca['principal component 2'], c=kmeans.labels_.astype(float), s=50, alpha=.5)
plt.scatter(center[:, 0], center[:, 1], c='red', s=50)

plt.show()


# plt.figure(1)
# plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], color='blue')
# plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], color='green')
# plt.scatter(df['sepal length (cm)'], df['petal width (cm)'], color='yellow')
# plt.scatter(df['sepal width (cm)'], df['petal length (cm)'], color='red')
# plt.scatter(df['sepal width (cm)'], df['petal width (cm)'], color='black')
# plt.scatter(df['petal length (cm)'], df['petal width (cm)'], color='grey')
#
# plt.figure(2)
# plt.xlabel('K')
# plt.plot(*elbow_method(pca))
# plt.show()

# df.hist()


# print(len(df))

# sns.displot(df, x='petal length (cm)')
