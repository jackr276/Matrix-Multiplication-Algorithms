"""
Author: Jack Robbins
This python file will multiply a matrix with its inverse using the regular method
and Strassen's algorithm to compare the performance of the two methods
"""

import numpy as np
import time


def matrix_mult_classic(a, b):
    result = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    start_time = time.time()


    end_time = time.time()
    

def matrix_mult_strassen(a, b):
    result = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    start_time = time.time()


    end_time = time.time() 

"""
Main method for running/printing
"""
def main():
    print("Testing matrix multiplication execution time.")
    print("Input Matrix:")
    #Matrix given in prompt
    matrix = np.array([[1, 3, 3, 6], [4, 2, 8, 2],[3, 3, 4, 5],[2, 6, 3, 1]])
    print(matrix)
    print("\n")

    # Calculate inverse
    inverse = np.linalg.inv(matrix)
    print("Inverse of input:")
    print(inverse)
    print("\n")


if __name__ == '__main__':
    main()
