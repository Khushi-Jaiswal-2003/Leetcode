nums =[4,4,4,1,4]
nums.sort()
power_set = 2 ** len(nums)
size = len(nums)
list_ans = []
for i in range(power_set):
    l1 = []
    for j in range(size):
        if (i & (1 << j)) != 0:
            l1.append(nums[j])

    if l1 in list_ans:
        continue
    else:
        list_ans.append(l1)
print(len(list_ans))