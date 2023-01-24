n = 5
list_n = []
for i in range(n+1):
    x = str(bin(i))[2:]
    if '0' in x:
        x = x.split('0')
        x = ''.join(x)
        list_n.append(len(x))
    else:
        list_n.append(len(x))
print(list_n)

