nums = [2,0,2,1,1,0]
zero_count, one_count, two_count =0, 0, 0
for i in range(len(nums)):
    if nums[i]==0:
        zero_count+=1
    elif nums[i]==1:
        one_count+=1
    else:
        two_count+=1

for i in range(zero_count):
    nums[i]=0
for j in range(zero_count,zero_count+one_count):
    nums[j]=1
for k in range(zero_count+one_count, zero_count+one_count+two_count):
    nums[k]=2
print(nums)