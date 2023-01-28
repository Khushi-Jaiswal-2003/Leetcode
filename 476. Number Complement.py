num = 5
bin_num = bin(num)[2:]
print(bin_num)
ans =''
for i in bin_num:
    if i=='1':
        ans+='0'
    else:
        ans+='1'
print(int(ans, 2))
