m = 25
count = 0
if m==0:
    print(0)
if m==1:
    print(1)
if m==2:
    print(1)
else:
    a = 0
    b = 1
    s =1
    for i in range(2, m + 1):
        a = b
        b = s
        # print(b)
        s= a + b
        count+=s
        print(s)
        # print(count)
m=25
a=[0,1,1]
for i in range(m):
    a.append(sum(a))
    a.pop(0)
    print( a[0])