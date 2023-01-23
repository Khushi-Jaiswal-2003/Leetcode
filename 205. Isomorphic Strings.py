s = "bbbaaaba"
t = "aaabbbba"
dict_s = {}
dict_t = {}
if len(s)!=len(t):
    print(False)
else:
    for i in range(len(s)):
        if s[i] in dict_s:
            dict_s[s[i]]+=1
        else:
            dict_s[s[i]]=1
    print(dict_s)

    for i in range(len(t)):
        if t[i] in dict_t:
            dict_t[t[i]] += 1
        else:
            dict_t[t[i]]=1
    print(dict_t)
    if len(dict_s)==len(dict_t):
        count = 0
        a = sorted(dict_s.values())
        print(a)
        b = sorted(dict_t.values())

        match = []
        for i in range(len(a)):
            if a[i]==b[i]:
                match.append(True)
            else:
                match.append(False)
        print(all(match))
    else:
        print(False)


