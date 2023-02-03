from numpy import *
m = 2
n = 3
c = []
for i in range(m):
    k = []
    for j in range(n):
        k.append(0)
    c.append(k)
print(c)
indices = [[0,1],[1,1]]
for i in range(len(indices)):
    for j in range(n):
        c[indices[i][0]][j]+=1

    for k in range(m):
        c[k][indices[i][1]]+=1
print(c)
count = 0
for i in range(m):
    for j in range(n):
        if c[i][j]%2!=0:
            count+=1
print(count)
