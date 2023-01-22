# n = 3
# spiral_matrix = []
# for i in range(n):
#     column = []
#     for j in range(n):
#         column.append(0)
#     spiral_matrix.append(column)
# print(spiral_matrix)
# count = 1
# top_row = 0
# buttom_row = n-1
# left_column = 0
# right_column = n-1
# direction = 0
# while (top_row<=buttom_row and left_column<=right_column):
#
#     if direction==0:
#         for i in range(left_column, right_column+1):
#             spiral_matrix[top_row][i]=count
#             count+=1
#         top_row+=1
#
#     elif direction==1:
#         for i in range(top_row, buttom_row+1):
#             spiral_matrix[i][right_column]=count
#             count+=1
#         right_column-=1
#
#     elif direction==2:
#         for i in range(right_column, left_column-1, -1):
#             spiral_matrix[buttom_row][i]=count
#             count+=1
#         buttom_row-=1
#
#     elif direction==3:
#         for i in range(buttom_row, top_row-1, -1):
#             spiral_matrix[i][left_column]=count
#             count+=1
#         left_column-=1
#
# print(spiral_matrix)

n = 3
# matrix = [[1, 0, 5], [5, 2, 16], [9, 5, 26, 2], [19, 6, 7, 8]]
top_row = 0
left_column = 0
buttom_row = n - 1
right_column = n - 1
direction = 0
spiral_matrix = []
num =1
for i in range(n):
    column = []
    for j in range(n):
        column.append(0)
    spiral_matrix.append(column)
print(spiral_matrix)
while(top_row<=buttom_row and left_column<=right_column):
    if direction==0:
        for i in range(left_column, right_column+1):
            # spiral_matrix.append(spiral_matrix[top_row][i])
            spiral_matrix[top_row][i]=num
            num+=1
        top_row+=1

    elif direction==1:
        for i in range(top_row, buttom_row+1):
            # spiral_matrix.append(spiral_matrix[i][right_column])
            spiral_matrix[i][right_column]=num
            num+=1
        right_column-=1

    elif direction==2:
        for i in range(right_column, left_column-1, -1):
            # spiral_matrix.append(matrix[buttom_row][i])
            spiral_matrix[buttom_row][i]=num
            num+=1
        buttom_row-=1

    elif direction==3:
        for i in range(buttom_row, top_row-1, -1):
            # spiral_matrix.append(matrix[i][left_column])
            spiral_matrix[i][left_column]=num
            num+=1
        left_column+=1

    direction=(direction+1)%4
print(spiral_matrix)
