# BOJ 9461

import sys
input = sys.stdin.readline

T = int(input())

dp = [1] * (101)

for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(T):
    print(dp[(int(input()))-1])
