# BOJ 1932

import sys
input = sys.stdin.readline

MAX = 500

n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 * (i) for i in range(j+1)] for j in range(n)]

dp[0] = tri[0]

for i in range(1,n):
    dp[i][0] = tri[i][0] + dp[i-1][0]
    dp[i][i] = tri[i][i] + dp[i-1][i-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1] + tri[i][j], dp[i-1][j] + tri[i][j])


print(max(dp[n-1]))
