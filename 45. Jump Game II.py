nums = [2, 3, 1, 1, 4]
jump = 0
left, right = 0, 0
while (right<len(nums)-1):
    f = 0
    for i in range(left, right+1):
        f = max(f, i+nums[i])
    left =right+1
    right = f
    jump+=1
print(jump)

