nums = [0,1,2,2,3,0,4,2]
val = 2
len_nums = len(nums)
i = 0
while (i < len_nums):
    if nums[i] == val:
        del nums[i]
        len_nums -= 1
    else:
        i += 1
print(len_nums)
