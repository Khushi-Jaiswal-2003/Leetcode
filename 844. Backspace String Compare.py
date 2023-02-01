s = "ab#c"
t = "ad#c"
if len(s)!=len(t):
    print(False)
else:
    count=0
    for i in range(len(s)):
        if s[i] and t[i]=='#':
            count+=1
    if count==s.count('#'):
        print(True)
    else:
        print(False)
