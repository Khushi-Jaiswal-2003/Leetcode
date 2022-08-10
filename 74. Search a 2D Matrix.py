matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
row_low, row_high = 0, len(matrix)
col_low, col_high = 0, len(matrix[0])
found = False
while (row_low<row_high and not found):
    row_mid = (row_low+row_high)//2

    if matrix[row_mid][0]==target:
        found=True

    elif matrix[row_mid][0]<target:
        row_low=row_mid+1

    else:
        row_high=row_mid

row_low-=1
Found = False
while(col_low < col_high and not Found):
    col_mid = (col_low+col_high)//2

    if matrix[row_low][col_mid]==target:
        Found=True

    elif matrix[row_low][col_mid]<target:
        col_low=col_mid+1

    else:
        col_high=col_mid
if Found==True or found==True: print(True)
else: print(False)
