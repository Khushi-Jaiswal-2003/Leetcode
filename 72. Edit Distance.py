word1 = "horse"
word2 = "ros"
dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
print(dp)
for i in range(len(word1)+1):
    dp[i][0]=i
    for j in range(1, len(word2)+1):
        if i==0:
            dp[0][j]=j

        elif word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
print(dp[-1][-1])