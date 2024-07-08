/**
 * Author: Jack Robbins
 * This file contains a simple C program that compares the execution time of multiplying a 4 x 4 matrix
 * with its inverse using the traditional matrix multiplication algorithm and Strassen's algorithm
 */

#include <stdio.h>
#include <stdlib.h>

void print_matrix(int** matrix, int N){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			printf("%2d ", matrix[i][j]);
		}
	printf("\n");
	}
}



int main(int argc, char** argv){
	//The first command line argument will be the dimension of the matrix
	
	const int N = atoi(argv[1]);

	//If we don't see the right amount of arguments, hard exit
	if(argc != N * N + 2){
		printf("Incorrect number of inputs provided for an %d X %d matrix\n", N, N);
		printf("%d\n", argc);
		exit(1);
	}

	//Declare and allocate our N x N matrix
	int** matrix = (int**)malloc(sizeof(int) * N);

	for(int i = 0; i < N; i++){
		matrix[i] = (int*)malloc(sizeof(int) * N);
	}

	//Advance the pointer by 2
	argv += 2;

	//For running through argv
	int index = 0;

	//Grab all of our inputs
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			matrix[i][j] = atoi(argv[index]);	
		 	index++;
		}
	}
	
	printf("Inputted Matrix:\n");
	print_matrix(matrix, N);
}