nums = [0,1,1,3,3]
k = 4
max_ans = sum(nums[:k])/k
print(max_ans)
for i in range(len(nums)):
    for j in range(i, len(nums)):
        # print(nums[i:j+1])
        if len(nums[i:j+1])==k:
            print(nums[i:j+1])
            max_ans = max(max_ans, sum(nums[i:j+1])/k)
print(max_ans)


