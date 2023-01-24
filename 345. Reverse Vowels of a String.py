s = 'leetcode'
s = list(s)
# print(s)
count = []
vowel = 'aeiouAEIOU'
for i in range(len(s)):
    if s[i] in vowel:
        count.append(s[i])
count = count[::-1]
# print(count)
ans = 0
for i in range(len(s)):
    if s[i] in count:
        s[i] =  count[ans]
        ans+=1
print(''.join(s))