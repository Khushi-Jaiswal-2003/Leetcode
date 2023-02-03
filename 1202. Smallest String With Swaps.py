s = "cba"
pairs = [[0,1],[1,2]]
s = list(s)
for i in range(len(pairs)):
    s[pairs[i][0]], s[pairs[i][1]]=s[pairs[i][1]], s[pairs[i][0]]
    print(s)