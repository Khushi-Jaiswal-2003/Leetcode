# nums = [1,5,3,6,8]
# lnums = nums*2
# output = []
# print(lnums)
# for i in range(len(nums)):
#     for j in range(i+1, len(lnums)):
#         if nums[i]< lnums[j]:
#             output.append(lnums[j])
#             break
#     else:
#         output.append(-1)
# print(output)

nums = [1,5,3,6,8]
lnums = nums*2
output = []
print(lnums)
for i in range(len(nums)):
    for j in range(i+1, len(lnums)):
        if nums[i]< lnums[j]:
            output.append(lnums[j])
            break
    else:
        output.append(-1)
print(output)
