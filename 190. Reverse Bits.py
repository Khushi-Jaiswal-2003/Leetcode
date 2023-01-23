n = 11111111111111111111111111111101
# print(n[::-1])
# print(str(int(n,2)))
print(int("{:032b}".format(n)[::-1],2))
