import numpy as np

# Input file from user
filename = input('Enter your file: ')
length = int(input('Length of path to find out: '))
start = int(input('Start point: '))
end = int(input('End point: '))

# Access to file path
path = '/home/kisejin/Documents/Folder Ubuntu/code_file/code_py/'
filename = path + filename

# Read file from user's input
with open(filename, mode='r') as fopen:
    matrix = [[int(num) for num in line.split(' ')] for line in fopen]
    matrix = np.array(matrix)


def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print('\n')


def find_path_with_len(matrix, length):
    i = 1
    matrix_len = matrix.copy()
    while i <= length:
        matrix_len = np.dot(matrix_len, matrix)
        i += 1
    return matrix_len


print_matrix(find_path_with_len(matrix, length))
