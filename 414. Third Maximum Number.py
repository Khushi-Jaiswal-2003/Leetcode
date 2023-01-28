nums =  [1, 1, 1]
set_nums = sorted(list(set(nums)))
# print(set_nums)
# print(set_nums.index(max(nums)))
if len(set_nums)==1:
    print(set_nums[0])
else:
    print(set_nums[set_nums.index(max(nums))-2])