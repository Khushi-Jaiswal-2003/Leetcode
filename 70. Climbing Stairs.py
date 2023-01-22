n = 4
way = [0, 1]
for i in range(n):
    s = way[0]+way[1]
    way[0]=way[1]
    way[1]=s
    # print(s)
    print(way)
print(way[1])
