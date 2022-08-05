# BOJ 2579

import sys
input = sys.stdin.readline

n = int(input())

step = list(int(input()) for _ in range(n))
step.insert(0, 0)
step.insert(0, 0)

dp = [0 for _ in range(n + 2)]

dp[2] = step[2]

for i in range(3, n + 2):
    dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[n + 1])
