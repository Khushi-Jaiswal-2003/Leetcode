a = [2,4,3]
b = [5,6,4]
a = ''.join(map(str, a))
b = ''.join(map(str, b))
a = a[::-1]
b = b[::-1]
c = str(int(a)+int(b))
print(list(c[::-1]))
