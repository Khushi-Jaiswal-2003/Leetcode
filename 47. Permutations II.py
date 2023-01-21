num = [1,1,2]
# if not num:
#     return []
num.sort()
ret = [[]]
for n in num:
    new_ret = []
    l = len(ret[-1])
    for seq in ret:
        for i in range(l, -1, -1):
            if i < l and seq[i] == n:
                break
            new_ret.append(seq[:i] + [n] + seq[i:])
    ret = new_ret
print(ret)