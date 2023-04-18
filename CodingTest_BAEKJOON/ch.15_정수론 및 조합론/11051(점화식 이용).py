n, k = map(int, input().split())

dp = [[0 for i in range(n+1)] for i in range(n+1)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n+1):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = 1
        elif j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k])
