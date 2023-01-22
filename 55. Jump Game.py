nums = [2, 7, 1, 0, 2]
ans = len(nums)-1
for i in range(len(nums)-1, -1, -1):
    if i+nums[i]>= ans:
        ans = i
if ans==0:
    print(True)
else:
    print(False)