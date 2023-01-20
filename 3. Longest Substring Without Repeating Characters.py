# s = "ABCDEAFBDGCBB"
s = "abcabcbb"
dict_s={}
result = 0
i=0
for j in range(len(s)):
    if s[j] in dict_s:
        i = max(i, dict_s[s[j]]+1)
        pass

    result = max(result, (j-i+1))
    dict_s[s[j]]=j
print(result)

