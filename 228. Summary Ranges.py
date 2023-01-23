nums = [0, 1, 2, 4, 5, 7, 6, 8]
cop = nums.copy()
cop[0]=1
print(nums, cop)
# start = 0
# count = 0
# list_n = []
# for i in range(len(nums)):
#     if nums[count]+1 == nums[i]:
#         count+=1
#         x =str(nums[start])+'->'+ str(nums[count])
#         list_n.append(x)
#     else:
#         start= i
#         count= i
# print(list_n)
# # final_ans = []
# # for i in range(len(list_n)-1):
# #     if list_n[i][0]!=list_n[i+1][0]:
# #         x =list_n[i]
# #         y =list_n[i+1]
# #         final_ans.append(x)
# #         final_ans.append(y)
# # print(final_ans)
# #
