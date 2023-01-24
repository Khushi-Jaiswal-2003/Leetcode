nums1 = [1,2,2,1]
nums2 = [2,2]
nums = []
for i in nums1:
    if i in nums2:
        nums.append(i)
        nums2.remove(i)
print(nums)