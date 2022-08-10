x = 1534236469
ans = 0
if x<2147483648 :
    if x<0:
        x=-(x)
        while x!=0:
            ans = ans*10+x%10
            x//=10
        print(-ans)
    else:
        while x!=0:
            ans = ans*10+x%10
            x//=10
        print(ans)
else:
    print(0)