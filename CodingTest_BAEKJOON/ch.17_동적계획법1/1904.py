n = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])

# result = []
# def dfs(temp):
#     if len(temp) == n:
#         result.append(temp)
#         return
#
#     if len(temp) < n:
#         temp += '1'
#         dfs(temp)
#         temp = temp[:-1]
#     if len(temp) < n-1:
#         temp += '00'
#         dfs(temp)
#         temp = temp[:-2]
#
#
# dfs('')
# print(len(result))
