n = 13
ans = []
for i in range(1, n+1):
    ans.append(i)
print(sorted(ans, key=str))

count = sorted([i for i in range(1, n+1)], key=str)
print(count)