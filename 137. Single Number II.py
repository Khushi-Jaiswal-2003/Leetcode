nums = [2,2,3,2]
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        print(nums[i])