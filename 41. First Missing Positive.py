nums =[1,5,6]
# print(len(nums))
for i in range(1,len(nums)+2):
    if i not in nums:
        if i>0:
            print(i)
            break

nums.sort()
print(nums)
res = 1
for i in nums:
    # print(i)
    if i==res:
        res+=1
        print(i, res)
print(res)