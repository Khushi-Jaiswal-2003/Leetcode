n = 1
if n==0:
    print(0)

if n==1:
    print(1)
else:
    a = 0
    b = 1
    for i in range(2, n+1):
        cur = a+b
        # print(cur)
        a = b
        b = cur
    print(b)