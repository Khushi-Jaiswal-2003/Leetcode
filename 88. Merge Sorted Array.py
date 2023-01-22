nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for i in range(len(nums2)):
    nums1[len(nums1)-i-1]=nums2[i]
print(sorted(nums1))
print(nums1.sort())