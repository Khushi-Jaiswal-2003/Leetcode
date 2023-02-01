s = "ababcbacadefegdehijhklij"
# dict = {}
# for i in range(len(s)):
#     if s[i] in dict:
#         dict[s[i]]= i
#     else:
#         dict[s[i]] = i
# print(dict)
dict = {}
for i, j in enumerate(s):
    dict[j] = i
print(dict)

res = []
size, end = 0, 0
for i, j in enumerate(s):
    size+=1
    # if dict[j] > end:
    #     end = dict[j]
    end = max(end, dict[j])

    if i== end:
        res.append(size)
        size=0
print(res)