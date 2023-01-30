mat = [[1,2],[3,4]]
reshape = []
r = 1
c = 4
if len(mat)*len(mat[0])==r*c:
    con_mat = []
    for i in mat:
        reshape.extend(i)
    # print(reshape)
    count = 0
    for i in range(r):
        row = []
        for j in range(c):
            row.append(reshape[count])
            count+=1
        con_mat.append(row)
    print(con_mat)
else:
    print(mat)
