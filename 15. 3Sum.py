# todo brute force
nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                x =[nums[i], nums[j], nums[k]]
                x.sort()
                # print(x)
                if sorted(x) in ans:
                    continue
                else:
                    ans.append(x)
print(ans)

# N, result = len(nums), []
# for i in range(N):
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
#     target = nums[i] * -1
#     s, e = i + 1, N - 1
#     while s < e:
#         if nums[s] + nums[e] == target:
#             result.append([nums[i], nums[s], nums[e]])
#             s = s + 1
#             while s < e and nums[s] == nums[s - 1]:
#                 s = s + 1
#         elif nums[s] + nums[e] < target:
#             s = s + 1
#         else:
#             e = e - 1
# return result
