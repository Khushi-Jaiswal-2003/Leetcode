nums = [1, 2, 3]
list = [[]]
for i in nums:
    sub_list = []
    for j in list:
        sub_list.append(j + [i])
        print(j+[i])
    list+=sub_list
print(list)