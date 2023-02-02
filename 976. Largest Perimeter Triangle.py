# nums = [1, 2, 1]
# count = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             if nums[i]+ nums[j]>nums[k] and nums[i]+nums[k]>nums[j] and nums[k]+nums[j]>nums[i]:
#                 # print(nums[i] + nums[j] + nums[k], count)
#                 if count<nums[i]+nums[j]+ nums[k]:
#                     count = nums[i] + nums[j] + nums[k]
#
# print(count)

nums = [1, 2, 1]
nums.sort(reverse=True)
print(nums)
for i, j, k in zip(nums, nums[1:], nums[2:]):
    if j+k>i:
        print(i+j+k)
print(0)