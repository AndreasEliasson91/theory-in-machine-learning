from assignment02 import *
from matplotlib import pyplot as plt

df = get_iris_dataset()
pca_df = pca_transformation(df)


def timer_elbow_method(data: pd.DataFrame) -> float:
    """
    Timer function.
    Takes a data frame and
    :param data: pandas data frame, the data to run through the elbow method at a data frame
    :return: float, the time (in seconds) that the kmeans takes to calculate the elbow method
    """
    timer_start = t.perf_counter()

    plt.figure()
    plt.xlabel('K')
    plt.plot(*elbow_method(data))
    plt.show()

    timer_stop = t.perf_counter()

    return timer_stop - timer_start


def main():
    plt.figure()
    plt.xlabel('K')
    plt.plot(*elbow_method(pca_df))

    kmeans = KMeans(n_clusters=3, max_iter=1000, init='random').fit(pca_df)
    center = kmeans.cluster_centers_

    plt.figure()
    plt.title('KMeans with all attributes')
    plt.scatter(pca_df['principal component 1'], pca_df['principal component 2'], c=kmeans.labels_.astype(float), s=50, alpha=.5)
    plt.scatter(center[:, 0], center[:, 1], c='red', s=50)

    plt.show()

    csv_df = pd.read_csv('./special_iris.csv')
    print(csv_df.shape)

    print(f'It took {timer_elbow_method(df) : .5f} seconds to calculate the elbow method for the basic data frame\n\n\n')
    print(f'It took {timer_elbow_method(csv_df) : .5f} seconds to calculate the elbow method for the csv-file\n\n\n')
    print(f'Time for k-means with the basic iris data set and 3 clusters: {timer_kmeans(df, 3, 1000) : .5f} seconds\n')
    print(f'Time for k-means with the basic iris data set and 5 clusters: {timer_kmeans(df, 5, 1000) : .5f} seconds\n')
    print(f'Time for k-means with the special iris data set and 3 clusters: {timer_kmeans(csv_df, 3, 1000) : .5f} seconds\n')
    print(f'Time for k-means with the special iris data set and 5 clusters: {timer_kmeans(csv_df, 5, 1000) : .5f} seconds')


if __name__ == '__main__':
    main()
