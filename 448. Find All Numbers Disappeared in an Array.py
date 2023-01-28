nums = [4, 3, 2, 7, 8, 2, 3, 1]
ans = [i for i in range(1, len(nums)+1) if i not in nums]
print(ans)

print(set(range(1, len(nums)+1))-set(nums))