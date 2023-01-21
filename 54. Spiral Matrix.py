matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 0, 5], [5, 2, 16], [9, 5, 26, 2], [19, 6, 7, 8]]
top_row = 0
left_column = 0
buttom_row = len(matrix)-1
right_column = len(matrix[0])-1
direction = 0
spiral_matrix = []
while(top_row<=buttom_row and left_column<=right_column):
    if direction==0:
        for i in range(left_column, right_column+1):
            spiral_matrix.append(matrix[top_row][i])
            print(matrix[top_row][i])
        top_row+=1

    elif direction==1:
        for i in range(top_row, buttom_row+1):
            spiral_matrix.append(matrix[i][right_column])
            print(matrix[i][right_column])
        right_column-=1

    elif direction==2:
        for i in range(right_column, left_column-1, -1):
            spiral_matrix.append(matrix[buttom_row][i])
            print(matrix[buttom_row][i])
        buttom_row-=1

    elif direction==3:
        for i in range(buttom_row, top_row-1, -1):
            spiral_matrix.append(matrix[i][left_column])
            print(matrix[i][left_column])
        left_column+=1

    direction=(direction+1)%4
print(spiral_matrix)
