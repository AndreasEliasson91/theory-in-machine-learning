import seaborn as sns

from assignment02 import elbow_method, get_iris_dataset, load_iris
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


df = get_iris_dataset()

combinations = [
    (df['sepal length (cm)'], df['sepal width (cm)']),
    (df['sepal length (cm)'], df['petal length (cm)']),
    (df['sepal length (cm)'], df['petal width (cm)']),
    (df['sepal width (cm)'], df['petal length (cm)']),
    (df['sepal width (cm)'], df['petal width (cm)']),
    (df['petal length (cm)'], df['petal width (cm)'])
]


def plot_clusters() -> None:
    global combinations, df

    for i in range(len(combinations)):
        tmp_df = df[[combinations[i][0].name, combinations[i][1].name]]
        kmeans = KMeans(n_clusters=3, max_iter=1000, init='random').fit(tmp_df)
        center = kmeans.cluster_centers_

        plt.figure(figsize=(6., 4.))
        plt.title(f'{combinations[i][0].name}, {combinations[i][1].name} : 3 clusters')
        plt.scatter(*combinations[i], c=kmeans.labels_.astype(float), s=50, alpha=.5)
        plt.scatter(center[:, 0], center[:, 1], c='red', s=50)

        kmeans = KMeans(n_clusters=5, max_iter=1000, init='random').fit(tmp_df)
        center = kmeans.cluster_centers_

        plt.figure(figsize=(6., 4.))
        plt.title(f'{combinations[i][0].name}, {combinations[i][1].name} : 5 clusters')
        plt.scatter(*combinations[i], c=kmeans.labels_.astype(float), s=50, alpha=.5)
        plt.scatter(center[:, 0], center[:, 1], c='red', s=50)

    plt.show()


def test_attributes() -> None:
    global combinations

    colors = ['blue', 'green', 'yellow', 'red', 'black', 'grey']
    legend = [f'{combinations[i][0].name}, {combinations[i][1].name}' for i in range(len(colors))]

    plt.figure(figsize=(10., 7.))
    plt.title('Test Attributes Combinations')

    for i in range(len(colors)):
        plt.scatter(*combinations[i], color=colors[i])

    plt.legend(legend)
    plt.show()


def main():
    # Seaborn distribution chart of the data set
    df['flower'] = load_iris().target
    sns.displot(df, x='sepal length (cm)', hue='flower')
    sns.displot(df, x='sepal width (cm)', hue='flower')
    sns.displot(df, x='petal length (cm)', hue='flower')
    sns.displot(df, x='petal width (cm)', hue='flower')

    # Elbow Method to get the k value for the algorithm
    plt.figure()
    plt.title('All attributes from the data set')
    plt.xlabel('K')
    plt.plot(*elbow_method(df))

    plt.figure()
    plt.title('Only sepal length and width')
    plt.xlabel('K')
    plt.plot(*elbow_method(df[['sepal length (cm)', 'sepal width (cm)']]))
    plt.show()

    # Print data points and attributes for the data set and run the plot functions
    print(df.shape)
    test_attributes()
    plot_clusters()


if __name__ == '__main__':
    main()
