nums = [555,901,482,1771]
count = 0
for i in range(len(nums)):
    nums[i]=len(str(nums[i]))
    if nums[i]%2==0:
        count+=1
print(count)

