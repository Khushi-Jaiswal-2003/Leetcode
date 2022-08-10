nums = [3, 2, 4]
target = 6
left = 0
right = len(nums)-1
# c = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i]+nums[j]==target:
#             c.append(i)
#             c.append(j)
# print(c)
while(nums[left]+nums[right]!=target):
    if nums[left]+nums[right]>target:
        right-=1
    else:
        left+=1
else:
    print([left, right])