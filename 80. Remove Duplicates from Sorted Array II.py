nums = [1,1,1,2,2,3]
for i in nums:
    if nums.count(i)>2:
        n = nums.count(i)
        for k in range(n-2):
            print(k)
            nums.remove(i)
nums.sort()
l= len(nums)
print(nums)
