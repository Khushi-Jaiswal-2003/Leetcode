# nums =[0, 2]
# n = len(nums)
# local_max = nums[0]
# global_max = nums[0]
# local_min = nums[0]
#
# for i in range(1, n):
#     temp = nums[i] * local_max
#     local_max = max(local_max * nums[i], nums[i], local_min * nums[i])
#     local_min = min(local_min * nums[i], nums[i], temp)
#
#     if local_max > global_max:
#         global_max = local_max
#
# print(global_max)

# brute force
nums =[1, 3, 4]
list = []

for i in range(len(nums)):
    count = 1
    for j in range(i, len(nums)):
        count = count*nums[j]
        list.append(count)

print(max(list))