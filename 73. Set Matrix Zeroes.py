A = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[0,1]]
index = []
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==0:
            index.append([i, j])
print(index)
for i in range(len(index)):
    for j in range(len(A[0])):
        A[index[i][0]][j] = 0
        for k in range(len(A)):
            A[k][index[i][1]]=0
print(A)

# m, n = len(A[0]), len(A)
# r1 = any(A[0][j] == 0 for j in range(m))
# c1 = any(A[i][0] == 0 for i in range(n))
# for i in range(1, n):
#     for j in range(1, m):
#         if A[i][j] == 0: A[i][0] = A[0][j] = 0
#
# for i in range(1, n):
#     for j in range(1, m):
#         if A[i][0] * A[0][j] == 0: A[i][j] = 0
#
# if r1:
#     for i in range(m): A[0][i] = 0
#
# if c1:
#     for j in range(n): A[j][0] = 0