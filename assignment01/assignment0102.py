from data.test_data_generators import distance_test_1, distance_test_2, distance_test_3

P = [0, 0]
Q = [2, 3]
R = [8, 8]


def valid_points(p: list, q: list) -> bool:
    """
    Check whether coordinates are correct format and contains exactly 2 coordinates
    :param p: list, point P
    :param q: list, point Q
    :return: bool
    """
    return isinstance(p[0], int) and isinstance(q[0], int) and isinstance(p[1], int) and isinstance(q[1], int) \
        and len(p) == 2


def get_length_of_distances(p: list, q: list) -> float:
    """
    Calculates and returns the length of distances
    :param p: list, coordinates for point P
    :param q: list, coordinates for point Q
    :return: float, The length of PQ
    """
    from math import sqrt

    if valid_points(p, q):
        return sqrt(((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2))


def plot_distances(*coordinates: list, sort=False) -> None:
    """
    Takes just any numbers of lists, containing 2 integers, and plots lines between the dots.
    :param coordinates: args, lists that contain exactly 2 integers, x and y coordinates
    :param sort: bool, whether the coordinates should be sorted (by x-coord) or not (False by default)
    :return: None
    """
    import matplotlib.pyplot as plt

    if sort:
        coordinates = sorted(coordinates, key=lambda x: x[0])
    points = []

    for i in range(len(coordinates) - 1):
        if valid_points(coordinates[i], coordinates[i + 1]):
            points.append([coordinates[i + 1][0], coordinates[i][0]])
            points.append([coordinates[i + 1][1], coordinates[i][1]])
            plt.text(int(coordinates[i][0]), int(coordinates[i][1]),
                     f'. {int(coordinates[i][0]), int(coordinates[i][1])}')

            if i == len(coordinates) - 2:
                plt.text(int(coordinates[i + 1][0]), int(coordinates[i + 1][1]),
                         f'. {int(coordinates[i + 1][0]), int(coordinates[i + 1][1])}')
        else:
            points.clear()
            print('One or more of the coordinates are in wrong format!')
            break

    if len(points) > 0:
        plt.plot(*points)
        plt.yscale('linear')
        plt.grid(True)
        plt.show()


def main():
    print(f'Length P -> Q: {get_length_of_distances(P, Q) : .5f}\n'
          f'Length Q -> R: {get_length_of_distances(Q, R) : .5f}')

    # Plot PQ and QR (Task 02 for passing grade)
    plot_distances(P, Q, R)

    # Print and then plots random number of points to further testing
    print('Points for test 1:')
    for point in distance_test_1:
        print(point)

    print('\nPoints for test 2:')
    for point in distance_test_2:
        print(point)

    print('\nPoints for test 3:')
    for point in sorted(distance_test_3):
        print(point)

    plot_distances(*distance_test_1)
    plot_distances(*distance_test_2)
    plot_distances(*distance_test_3, sort=True)


if __name__ == '__main__':
    main()
