intervals = [[1,4],[3,6],[2,8]]
n = len(intervals)
c = n
for i in range(n):
    for j in intervals[:i] + intervals[i + 1:]:
        if intervals[i][0] >= j[0] and intervals[i][1] <= j[1]:
            c -= 1
            break
print(c)