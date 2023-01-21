# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["a"]
# final = []
# for i in range(len(strs)):
#     count  = []
#     for j in range(len(strs)):
#         if sorted(strs[i])==sorted(strs[j]):
#             count.append(strs[j])
#     if sorted(count) in final:
#         continue
#     else:
#         final.append(sorted(count))
# print(final)
from collections import Counter

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
h = {}
for i in strs:
    x = ''.join(sorted(i))
    print(x)
    if x not in h:
        h[x]=[i]
        # print(h)
    else:
        h[x].append(i)
print(h)
print(h.values())

d={}
for i in strs:
    key = tuple(sorted(i))
    # print(key)
    d[key]= d.get(key, [])+[i]
    print(d)
print(d.values())