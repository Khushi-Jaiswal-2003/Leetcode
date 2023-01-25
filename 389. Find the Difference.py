s = "a"
t = "aa"
s = (sorted(s))
t = (sorted(t))
count = ''
for i in range(len(t)):
    if t[i] in s:
        s.remove(t[i])
    else:
        count+=t[i]
        break

print(count)