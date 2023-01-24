from collections import Counter

nums = [1]
k = 1
freq = Counter(nums)
ans = []
for i, j in freq.items():
    if j>=k:
        ans.append(i)
print(ans)