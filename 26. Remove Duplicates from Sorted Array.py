# num = [1, 1]
#
# c=0
#
# for i in range(len(num) - 1):
#     if num[i]!=num[i + 1]:
#         num[c]=num[i]
#         num[i]="None"
#         # num_len+=1
#         c+=1
#         if i == len(num)-2:
#             num[c] = num[i]
#             num[c] = num[i + 1]
#             # num_len+=1
#             num[i+1]="None"
#     elif num[i]==num[i+1]:
#         num[i]="None"
# num_len=0
# for i in num:
#     if i=="None":
#         num_len+=1
# print(num_len)
# print(num)

nums = [1, 1, 2]
c=0
# for i in range(len(num)-1):
#     if num[i]==num[i+1]:
#         continue
#     elif num[i]!=num[i+1]:
#         c += 1
#         print(c)
#         num[c] = num[i]
#
# print(c+1)
# print(num)
# if len(nums) == 0:
#         return 0
index = 0
for i in range(1, len(nums)):
    if nums[i] != nums[index]:
        index += 1
        nums[index] = nums[i]
        print(nums)
        print (index+ 1)