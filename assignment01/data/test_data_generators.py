import random as r


# Generates random distance points for task 02
distance_test_1 = [[r.randint(-10, 10), r.randint(0, 10)] for _ in range(r.randint(3, 10))]
distance_test_2 = [[r.randint(-10, 10), r.randint(0, 10)] for _ in range(r.randint(3, 10))]
distance_test_3 = [[r.randint(-10, 10), r.randint(0, 10)] for _ in range(r.randint(3, 10))]

# Generates random vectors for task 03
vector_length = r.randint(2, 8)
vector_add_test_1 = [[r.randint(-10, 10) for _ in range(vector_length)]for _ in range(r.randint(3, 10))]
vector_length = r.randint(2, 8)
vector_add_test_2 = [[r.randint(-10, 10) for _ in range(vector_length)]for _ in range(r.randint(3, 10))]
vector_length = r.randint(2, 8)
vector_add_test_3 = [[r.randint(-10, 10) for _ in range(vector_length)]for _ in range(r.randint(3, 10))]

# Generates random vectors for task 04
vector_length = r.randint(2, 8)
scalar_product_test_1_1 = [r.randint(-10, 10) for _ in range(vector_length)]
scalar_product_test_1_2 = [r.randint(-10, 10) for _ in range(vector_length)]
vector_length = r.randint(2, 8)
scalar_product_test_2_1 = [r.randint(-10, 10) for _ in range(vector_length)]
scalar_product_test_2_2 = [r.randint(-10, 10) for _ in range(vector_length)]
vector_length = r.randint(2, 8)
scalar_product_test_3_1 = [r.randint(-10, 10) for _ in range(vector_length)]
scalar_product_test_3_2 = [r.randint(-10, 10) for _ in range(vector_length)]

# Generates random matrices for task 05
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_add_test_1_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_add_test_1_2 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_add_test_2_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_add_test_2_2 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_add_test_3_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_add_test_3_2 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]

# Generates random matrices for task 06
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_multiply_test_1_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_multiply_test_1_2 = [[r.randint(-10, 10) for _ in range(row)]for _ in range(col)]
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_multiply_test_2_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_multiply_test_2_2 = [[r.randint(-10, 10) for _ in range(row)]for _ in range(col)]
row, col = r.randint(2, 6), r.randint(2, 6)
matrices_multiply_test_3_1 = [[r.randint(-10, 10) for _ in range(col)]for _ in range(row)]
matrices_multiply_test_3_2 = [[r.randint(-10, 10) for _ in range(row)]for _ in range(col)]
