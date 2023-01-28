# todo pending..
s = "cbaebabacd"
p = "abc"
power_set = 2**len(s)
size=len(s)
list = []
for i in range(power_set):
    l =[]
    for j in range(size):
        if (i&(1<<j))!=0:
            l.append(s[j])
    list.append(sorted(l))
print(list)
for i


