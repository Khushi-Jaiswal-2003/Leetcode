# nums = [4,3,2,7,8,2,3,1]
# set_nums = list(set(nums))
# ans = []
# for i in range(len(set_nums)):
#     if nums.count(set_nums[i])==2:
#         print(set_nums[i])
#         if set_nums[i] in ans:
#             pass
#         else:
#             ans.append(set_nums[i])
# print(ans)
from collections import Counter
nums = [4,3,2,7,8,2,3,1]
freq = Counter(nums)
ans = [i for i,j in freq.items() if j==2]
print(ans)