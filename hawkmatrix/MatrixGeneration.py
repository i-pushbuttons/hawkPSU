import numpy as np
import random

def generateMatrix(n, m, level):
    difficulty = level  # Easy, Medium, or Hard

    num_rows = n
    num_columns = m
    matrix_weight = False

    while not matrix_weight:
        x_sol = list()

        for i in range(num_columns):
            x_sol.append(random.randint(1, 9))  # Ensure no zero solutions

        if level == "Easy":
            pre_matrix = np.random.normal(loc=3, scale=4, size=(num_rows, num_columns))
        elif level == "Medium":
            pre_matrix = np.random.normal(loc=5, scale=6, size=(num_rows, num_columns))
        elif level == "Hard":
            pre_matrix = np.random.normal(loc=6, scale=4, size=(num_rows, num_columns))

        matrix = np.abs(pre_matrix).astype(int)  # Convert to integers

        y_column = np.dot(matrix, x_sol)

        # Calculate the sum of the matrix and y_column
        matrix_sum = np.sum(matrix)
        y_sum = np.sum(y_column)
        total_sum = matrix_sum + y_sum

        # Define limits based on difficulty
        if level == "Easy":
            limiter = (num_columns + num_rows) * 6
        elif level == "Medium":
            lower_limiter = (num_columns + num_rows) * 6
            upper_limiter = (num_columns + num_rows) * 10
        elif level == "Hard":
            limiter = (num_columns + num_rows) * 10

        # Check for zero rows or columns and ensure total_sum is within limits
        if not np.any(matrix == 0, axis=0).all() and not np.any(matrix == 0, axis=1).all():
            if level == "Easy" and total_sum < limiter:
                matrix_weight = True
            elif level == "Medium" and lower_limiter < total_sum < upper_limiter:
                matrix_weight = True
            elif level == "Hard" and total_sum > limiter:
                matrix_weight = True

    augmented_matrix = np.column_stack((matrix, y_column))

    print(augmented_matrix)

    return augmented_matrix, x_sol

if __name__ == "__main__":
    matrix, solution = generateMatrix(2, 2, "Easy")
    print(matrix)
    print(solution)