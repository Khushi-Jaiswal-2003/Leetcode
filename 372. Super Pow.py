a = 1
b = [4,3,3,8,5,2]
c = 0
for i in b:
    c = 10*c+i
    print(c)
print(pow(a, c, 1337))