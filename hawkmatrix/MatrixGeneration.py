import numpy as np
import random

def generateMatrix(n, m, level):
    difficulty = level #Easy, Medium, or Hard

    num_rows = n
    num_columns = m
    matrix_weight = False

    if (level == "Easy"):
        
        while not matrix_weight:

            x_sol = list()
            zero_sol = False

            for i in range(num_columns):
                x_sol.append(random.randint(0,9))
            pre_matrix = np.random.normal(loc=3, scale=4, size=(num_rows,num_columns)) 
            matrix = np.abs(pre_matrix).astype(int)

            y_column = np.dot(matrix, x_sol)

            #Sums of matrix and y_column
            matrix_sum = 0
            for i in range(num_rows):
                matrix_sum += sum(matrix[i])
            y_sum = sum(y_column)
            total_sum = matrix_sum + y_sum

            limiter = (num_columns + num_rows)*6

            for i in range(num_columns):
                if (x_sol[i] == 0):
                    zero_sol = True

            if (total_sum < limiter and zero_sol == False):
                matrix_weight = True
    elif(level == "Medium"):
        
        while not matrix_weight:

            x_sol = list()
            zero_sol = False

            for i in range(num_columns):
                x_sol.append(random.randint(0,9))
            pre_matrix = np.random.normal(loc=5, scale=6, size=(num_rows,num_columns)) 
            matrix = np.abs(pre_matrix).astype(int)

            y_column = np.dot(matrix, x_sol)

            #Sums of matrix and y_column
            matrix_sum = 0
            for i in range(num_rows):
                matrix_sum += sum(matrix[i])
            y_sum = sum(y_column)
            total_sum = matrix_sum + y_sum

            lower_limiter = (num_columns + num_rows)*6
            upper_limiter = (num_columns + num_rows)*10

            for i in range(num_columns):
                if (x_sol[i] == 0):
                    zero_sol = True

            if (total_sum < upper_limiter and total_sum > lower_limiter and zero_sol == False):
                matrix_weight = True
    elif(level == "Hard"):
        
        while not matrix_weight:

            x_sol = list()
            zero_sol = False

            for i in range(num_columns):
                x_sol.append(random.randint(0,9))
            pre_matrix = np.random.normal(loc=6, scale=4, size=(num_rows,num_columns)) 
            matrix = np.abs(pre_matrix).astype(int)

            y_column = np.dot(matrix, x_sol)

            #Sums of matrix and y_column
            matrix_sum = 0
            for i in range(num_rows):
                matrix_sum += sum(matrix[i])
            y_sum = sum(y_column)
            total_sum = matrix_sum + y_sum

            limiter = (num_columns + num_rows)*10

            for i in range(num_columns):
                if (x_sol[i] == 0):
                    zero_sol = True

            if (total_sum > limiter and zero_sol == False):
                matrix_weight = True

    augmented_matrix = np.column_stack((matrix, y_column))

    print(augmented_matrix)

    return augmented_matrix, x_sol

if __name__ == "__main__":
    generateMatrix(2,2,"Easy")