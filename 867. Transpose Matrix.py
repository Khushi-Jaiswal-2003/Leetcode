from numpy import *
matrix = [[1,2,3],[4,5,6],[7,8,9]]
row = len(matrix)
column = len(matrix[0])
zero_matrix = zeros((row, column), int)
# zero_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        zero_matrix[j][i]=matrix[i][j]
print(zero_matrix)