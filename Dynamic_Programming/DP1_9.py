# BOJ 1463

import sys
input = sys.stdin.readline

MAX = int(1e8)

n = int(input())

dp = [MAX] * (n + 1)
dp[n] = 0

for i in range(n, 1, -1):
    if dp[i] >= MAX:
        continue
    if i % 3 == 0:
        dp[i//3] = min(dp[i//3], dp[i] + 1)
    if i % 2 == 0:
        dp[i//2] = min(dp[i//2], dp[i] + 1)
    dp[i-1] = min(dp[i-1], dp[i] + 1)

print(dp[1])
