nums = [1,2,3,4]
ans =[1]*len(nums)
# print(ans)
prefix = 1
postfix = 1
for i in range(len(nums)):
    ans[i]=prefix
    prefix*=nums[i]
# print(prefix)
# print(ans)

for i in range(len(nums)-1, -1, -1):
    ans[i]*=postfix
    postfix*=nums[i]
    # print(nums[i], postfix)
    # print(ans)
print(ans)