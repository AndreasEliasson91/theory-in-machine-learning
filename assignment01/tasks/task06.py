from assignment01 import print_matrices
from assignment01.data.test_data_generators import matrices_multiply_test_1_1, matrices_multiply_test_1_2,\
    matrices_multiply_test_2_1, matrices_multiply_test_2_2, matrices_multiply_test_3_1, matrices_multiply_test_3_2

A = [
    [1, 2],
    [3, 2],
    [1, 3],
    [1, 1]
]
B = [
    [4, 5, 6],
    [6, 5, 4]
]


def multiply_matrices(a: list, b: list) -> list:
    """
    Takes two matrices, of just any type, and multiply them together.
    :param a: nested list, matrix A
    :param b: nested list, matrix B
    :return: list, matrix AB
    """
    def valid_matrices(*args):
        """Checks whether matrix A can multiply with B"""
        if isinstance(args[0], list) and isinstance(args[0][1], list) and isinstance(args[1], list) and isinstance(args[1][1], list):
            if len(args[0][1]) == len(args[1]):
                return True
            elif len(args[1][1]) == len(args[0]):
                pass

            return isinstance(args[0], list) and isinstance(args[1], list) and len(args[0][1]) == len(args[1])

    if not valid_matrices(a, b):
        print('One of the matrices are in the wrong format!')
        return None
    ab = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i, _ in enumerate(a):
        for j, row in enumerate(b):
            for k, column in enumerate(row):
                ab[i][k] += (a[i][j] * b[j][k])

    return ab




def main():
    # Calculate AB (Task 06 for passing grade)
    print_matrices(multiply_matrices(A, B))

    # Calculate and print the product of two matrices of a random type to further testing
    print_matrices(multiply_matrices(matrices_multiply_test_1_1, matrices_multiply_test_1_2))
    print_matrices(multiply_matrices(matrices_multiply_test_2_1, matrices_multiply_test_2_2))
    print_matrices(multiply_matrices(matrices_multiply_test_3_1, matrices_multiply_test_3_2))


if __name__ == '__main__':
    main()
