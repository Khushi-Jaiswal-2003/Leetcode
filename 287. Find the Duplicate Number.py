nums = [1,3,4,2,3]
for i in nums:
    if nums.count(i)>=2:
        print(i)
        break
nums.sort()
for i in range(1, len(nums)):
    if nums[i-1]==nums[i]:
        print(i)
        break