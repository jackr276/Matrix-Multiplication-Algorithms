"""
Author: Jack Robbins
This python file will multiply a matrix with its inverse using the regular method
and Strassen's algorithm to compare the performance of the two methods
"""

import numpy as np
import time


def matrix_mult_classic(a, b):
    result = np.array([[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]])
    start_time = time.time()

    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                result[i][j] = result[i][j] + a[i][k] * b[k][j]

    end_time = time.time()

    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = round(result[i][j], 2)

    return (result, (end_time - start_time) * 1000000)
   

def matrix_mult_strassen(a, b): 
    start_time = time.time()
    result = strassen_helper(a, b)
    end_time = time.time() 

    for i in range(len(a)):
        for j in range(len(a[0])):
           result[i][j] = round(result[i][j], 2)

    return (result, (end_time - start_time) * 1000000)


def strassen_helper(a, b):
    n = len(a)

    if n < 3:
        return np.dot(a, b)

    middle = n // 2

    # Partition matrix A into four submatrices
    Matrix_a_1_1 = a[:middle, :middle]
    Matrix_a_1_2 = a[:middle, middle:]
    Matrix_a_2_1 = a[middle:, :middle]
    Matrix_a_2_2 = a[middle:, middle:]

    # Partition matrix b into four submatrices
    Matrix_b_1_1 = b[:middle, :middle]
    Matrix_b_1_2 = b[:middle, middle:]
    Matrix_b_2_1 = b[middle:, :middle]
    Matrix_b_2_2 = b[middle:, middle:]

    # Recursively multiply all submatrices
    Product_1 = strassen_helper(Matrix_a_1_1, Matrix_b_1_2 - Matrix_b_2_2)
    Product_2 = strassen_helper(Matrix_a_1_1 + Matrix_a_1_2, Matrix_b_2_2)
    Product_3 = strassen_helper(Matrix_a_2_1 + Matrix_a_2_2, Matrix_b_1_1)
    Product_4 = strassen_helper(Matrix_a_2_2, Matrix_b_2_1 - Matrix_b_1_1)
    Product_5 = strassen_helper(Matrix_a_1_1 + Matrix_a_2_2, Matrix_b_1_1 + Matrix_b_2_2)
    Product_6 = strassen_helper(Matrix_a_1_2 - Matrix_a_2_2, Matrix_b_2_1 + Matrix_b_2_2)
    Product_7 = strassen_helper(Matrix_a_1_1 - Matrix_a_2_1, Matrix_b_1_1 + Matrix_b_1_2)
    
    Matrix_c_1_1 = Product_5 + Product_4 - Product_2 + Product_6
    Matrix_c_1_2 = Product_1 + Product_2
    Matrix_c_2_1 = Product_3 + Product_4
    Matrix_c_2_2 = Product_5 + Product_1 - Product_3 - Product_7

    C = np.vstack((np.hstack((Matrix_c_1_1, Matrix_c_1_2)), np.hstack((Matrix_c_2_1, Matrix_c_2_2))))
    return C

"""
Main method for running/printing
"""
def main():
    print("\nTesting matrix multiplication execution time.")
    print("Input Matrix M:") 
    #Matrix given in prompt
    M= np.array([[1, 3, 3, 6], [4, 2, 8, 2],[3, 3, 4, 5],[2, 6, 3, 1]])
    print(M)
    print("\n")

    # Calculate inverse
    N= np.linalg.inv(M)
    print("Inverse of M N:")
    print(N)
    print("\n")

    result_tuple = matrix_mult_classic(M, N)
    print("Result of M X N using classic matrix multiplication algorithm:")
    print(result_tuple[0])
    print("Operation completed in:", round(result_tuple[1], 5), " microseconds")
    print("\n")

    print("Result of N X M using classic matrix multiplication algorithm:")
    result_tuple = matrix_mult_classic(N, M)
    print(result_tuple[0])
    print("Operation completed in:", round(result_tuple[1], 5), " microseconds")
    print("\n")

    result_tuple = matrix_mult_strassen(M, N)
    print("Result of M X N using Strassen's matrix multiplication algorithm:")
    print(result_tuple[0])
    print("Operation completed in:", round(result_tuple[1], 5), " microseconds")
    print("\n")

    result_tuple = matrix_mult_strassen(N, M)
    print("Result of M X N using Strassen's matrix multiplication algorithm:")
    print(result_tuple[0])
    print("Operation completed in:", round(result_tuple[1], 5), " microseconds")
    print("\n")

if __name__ == '__main__':
    main()
