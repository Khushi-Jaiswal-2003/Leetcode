n = 19
ans = 0
while ans!=1 and n!=4:
    ans = 0
    while n>0:
        temp = n%10
        print(temp)
        ans+=(temp*temp)
        print(ans)
        n = n//10
        print(n)
    n = ans
if ans == 1:
    print(True)
else:
    print(False)