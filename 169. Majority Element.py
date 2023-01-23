nums = [3, 3, 4]
dict_set={}
for i in range(len(nums)):
    if nums[i] in dict_set:
        dict_set[nums[i]]+=1
    else:
        dict_set[nums[i]]=1
print(dict_set)
max_count = max(dict_set.values())
for i, j in dict_set.items():
    if max_count==j:
        print(i)
