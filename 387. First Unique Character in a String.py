s = "aabb"
dict_s = {}
count = 1
for i in range(len(s)):
    if s[i] in dict_s:
        dict_s[s[i]]+=1
    else:
        dict_s[s[i]]=1
print(dict_s)
count = []
for i in range(len(s)):
    if dict_s[s[i]]==1:
        count.append(i)
        break
# print(count)
if len(count)==1:
    print(count[0])
else:
    print(-1)
