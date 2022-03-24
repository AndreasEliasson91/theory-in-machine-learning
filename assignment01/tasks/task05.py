from assignment01 import print_matrices
from assignment01.data.test_data_generators import matrices_add_test_1_1, matrices_add_test_1_2, matrices_add_test_2_1,\
    matrices_add_test_2_2, matrices_add_test_3_1, matrices_add_test_3_2

A = [[1, 2], [3, 2]]
B = [[4, 5], [6, 5]]


def add_matrices(a: list, b: list) -> list:
    """
    Takes two matrices with just any, but the same type, and calculates the sum.
    :param a: nested list, matrix A
    :param b: nested list, matrix B
    :return: list, matrix AB
    """

    def valid_matrix(*args):
        """Checks whether matrix A is the same type as matrix B"""
        return all(len(x) == len(args[0]) for x in args[1:])

    for i in range(len(a)):
        if len(a) != len(b) or not valid_matrix(a[i], b[i]):
            print('One of the matrices are in the wrong format!')
            return None

    return [[a[i][j] + b[i][j] for j, column in enumerate(row)] for i, row in enumerate(a)]


def main():
    # Calculate A+B (Task 05 for passing grade)
    print_matrices(add_matrices(A, B))

    # Calculate and print the sum of two matrices of a random type to further testing
    print_matrices(add_matrices(matrices_add_test_1_1, matrices_add_test_1_2))
    print_matrices(add_matrices(matrices_add_test_2_1, matrices_add_test_2_2))
    print_matrices(add_matrices(matrices_add_test_3_1, matrices_add_test_3_2))


if __name__ == '__main__':
    main()