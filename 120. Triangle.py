triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
dp = [0]*(len(triangle)+1)
print(dp)
for i in triangle[::-1]:
    print(i)
    for j, k in enumerate(i):
        # print(j, k)
        dp[j]= k+min(dp[j], dp[j+1])
print(dp[0])