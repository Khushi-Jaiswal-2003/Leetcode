s ="God Ding"
s = list(s.split())
for i in range(len(s)):
    s[i]=s[i][::-1]
print(" ".join(s))