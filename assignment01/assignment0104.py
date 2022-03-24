from data.test_data_generators import scalar_product_test_1_1, scalar_product_test_1_2, scalar_product_test_2_1,\
    scalar_product_test_2_2, scalar_product_test_3_1, scalar_product_test_3_2
from math import sqrt, cos, pi

u = [0, 2, 3]
v = [0, 4, 6]


def calculate_scalar_product(u: list, v: list, degrees=None, radians=0.) -> float:
    """
    Takes two vectors from just any dimensions, they need to be in the same dimension tho,
    and calculates their scalar product.
    The vectors are considered parallel by default.
    :param u: list, vector u
    :param v: list, vector v
    :param degrees: float, angle in degrees
    :param radians: float, angle in radians
    :return: float
    """
    if len(u) != len(v):
        return 'One of the vectors are in the wrong format!'

    # Calculated with the formula: a·b = |a||b|cos(u,v)
    len_u, len_v = 0, 0

    for i in range(len(u)):
        len_u += u[i] ** 2
        len_v += v[i] ** 2

    # Calculate the angle from radians
    if degrees:
        radians = (degrees / 180) * pi

    return sqrt(len_u) * sqrt(len_v) * cos(radians)


def main():
    # Calculate u·v (Task 04 for passing grade)
    print(calculate_scalar_product(u, v))

    # Calculate scalar products of a random number of vectors to further testing
    print(calculate_scalar_product(scalar_product_test_1_1, scalar_product_test_1_2, radians=(2 * pi) / 3))
    print(calculate_scalar_product(scalar_product_test_2_1, scalar_product_test_2_2, radians=(2 * pi) / 3))
    print(calculate_scalar_product(scalar_product_test_3_1, scalar_product_test_3_2, radians=(2 * pi) / 3))


if __name__ == '__main__':
    main()
