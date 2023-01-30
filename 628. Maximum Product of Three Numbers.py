nums = [1000, 1000, 1000]
nums.sort()
print(max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1]))