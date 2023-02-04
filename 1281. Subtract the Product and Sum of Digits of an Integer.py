n = 234
n = str(n)
product = 1
sum = 0

for i in range(len(n)):
    # print(n[i])
    product*=int(n[i])
    sum+=int(n[i])
print(product-sum)
