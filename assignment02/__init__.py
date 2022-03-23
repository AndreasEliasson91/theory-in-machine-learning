import pandas as pd
import seaborn as sns
import time as t

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


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


def timer_kmeans(data: pd.DataFrame, clusters: int, iterations: int) -> float:
    """
    Timer function.
    Takes a data frame and returns the time it takes for the KMeans to calculate its result
    :param data: pandas data frame, the data frame to time
    :param clusters: int, number of clusters to test the kmeans with
    :param iterations: int, maximal number of iterations to test
    :return: float, the time (in seconds) that the kmeans takes to calculate the data frame
    """
    start = t.perf_counter()
    KMeans(n_clusters=clusters, max_iter=iterations, init='random').fit(data)
    stop = t.perf_counter()

    return stop - start
