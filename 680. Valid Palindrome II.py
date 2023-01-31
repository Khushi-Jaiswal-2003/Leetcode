s = "abca"
s = list(s)
if s == s[::-1]:
    print(True)

else:
    for i in range(len(s)//2):
        x = s.pop(i)
        if ''.join(s)==''.join(s)[::-1]:
            print(True, ''.join(s))
            break
        else:
            s.insert(i, x)
    else:
        print(False)
