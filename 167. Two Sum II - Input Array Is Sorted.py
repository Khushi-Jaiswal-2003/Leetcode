numbers =   [2,7,11,15]
target = 8
start = 0
end = len(numbers)-1
while(numbers[start]+numbers[end]!=target):
    if numbers[start]+numbers[end]>target:
        end-=1
    else:
        start+=1
else:
    print([start+1, end+1])

# for i in range(len(numbers)):
#     for j in range(i,len(numbers)):
#         if i!=j:
#             if numbers[i] + numbers[j] == target:
#                 index.append(i + 1)
#                 index.append(j + 1)
#         else:
#             pass
#
# print(index)