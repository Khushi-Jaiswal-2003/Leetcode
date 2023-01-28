nums1 = [1,3,5,2,4]
nums2= [5,4,3,2,1]
# nums2 =  [1,2,3,4]
greater =[]
for i in nums1:
    x = nums2[nums2.index(i):]
    # print(x)
    ans = []
    for j in x:
        if i<j:
            ans.append(j)
    if len(ans)==0:
        greater.append(-1)
    else:
        greater.append(ans[0])
print(greater)