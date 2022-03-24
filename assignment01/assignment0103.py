from data.test_data_generators import vector_add_test_1, vector_add_test_2, vector_add_test_3

u = [1, 2, 3]
v = [2, 2, 2]
w = [1, 0, 1, 0, 1]
x = [5, 6, 6, 5, 9]


def add_vectors(*vectors: list) -> list:
    """
    Takes just any numbers of vectors and returns their sum, as long as they're in the same dimension
    :param vectors: args, lists of vectors to calculate the sum from
    :return: list
    """
    length = len(vectors[0])
    sum = [0 for _ in range(length)]

    for vector in vectors:
        if len(vector) == length:
            for i in range(len(vector)):
                sum[i] += vector[i]
        else:
            return 'One or more of the vectors are in the wrong format!'

    return sum


def print_vectors(*vectors: list) -> None:
    """
    Print function.
    Prints all vectors and then the sum
    :param vectors: list, vectors to calculate
    :return: None
    """
    for i, vector in enumerate(vectors):
        print(f'Vector {i+1}: {vector}')
    print(f'\nSum: {add_vectors(*vectors)}\n\n')


def main():
    # Calculate u+v and w+x (Task 03 for passing grade)
    print_vectors(u, v)
    print_vectors(w, x)

    # Calculate and print the sum of random number of vectors to further testing
    print_vectors(*vector_add_test_1)
    print_vectors(*vector_add_test_2)
    print_vectors(*vector_add_test_3)


if __name__ == '__main__':
    main()
