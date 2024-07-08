# Jack Robbins
# Basic runner script for the C programs in src

if [[ ! -d ./out ]]; then 
	mkdir out
fi

if [[ ! -f ./src/matrix_multiplication.c ]]; then
	echo "Could not find the required C source file ./src/matrix_multiplication.c" 
	exit 1;
fi

read -p "Enter an N x N matrix, inputting N first, then the matrix in row-major order: " INPUT

gcc -Wall -Wextra ./src/matrix_multiplication.c -o ./out/matrix_multiplication

./out/matrix_multiplication $INPUT
