matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
copy_matrix = matrix.copy()
print(copy_matrix)
matrix.clear()
print(matrix)
for i in range(len(copy_matrix)):
    row = []
    column = len(copy_matrix) - 1
    for j in range(len(copy_matrix[i])):
        row.append(copy_matrix[column][i])
        column-=1
    matrix.append(row)
print(matrix)
