s = "rat"
t = "car"
s= sorted(s)
t = sorted(t)
print(s, t)
count = 0
if len(s)==len(t):
    for i in range(len(s)):
        if s[i]==t[i]:
            count+=1
if count==len(s):
    print(True)
else:
    print(False)

