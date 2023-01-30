nums = [1,2,2,4]
n = len(nums)

s = list(set(nums))
actual = n * (n + 1) // 2 - sum(s)
rep = actual + sum(nums) - n * (n + 1) // 2

print([rep, actual])