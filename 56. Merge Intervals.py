intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key= lambda i: i[0])
print(intervals)
output = [intervals[0]]

for i, j in intervals[1:]:
    lastend = output[-1][1]
    print(lastend)
    if i<= lastend:
        output[-1][1] = max(lastend, j)
    else:
        output.append([i, j])
print(output)