num = [-1,-100,3,99]
k = 2
for i in range(k):
    a = num.pop(len(num)-1)
    num.insert(0,a)
    print(num)