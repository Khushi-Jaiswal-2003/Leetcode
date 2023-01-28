nums =[1,1,0,1,1,1,1]
ans = 0
count = 0
for i in nums:
    if i==1:
        count+=1
        ans = max(count, ans)

    else:
        count=0
print(ans)