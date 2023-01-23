# nums =[4,1,2,1,2]
# ans  =0
# for i in range(len(nums)):
#     ans ^=nums[i]
# print(ans)

nums = [2,2,4]
dict = {}
for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]]+=1

    else:
        dict[nums[i]]=1
for i,j in dict.items():
    if j==1:
        print(i)