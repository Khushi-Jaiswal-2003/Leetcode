nums= [0,1,0,3,12]
a = 0
for i in range(len(nums)):
    if nums[i]!=0:
        r = nums.pop(i)
        nums.insert(a,r)
        a+=1
print(nums)
