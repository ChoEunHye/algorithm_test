# BOJ 2579

import sys
input = sys.stdin.readline

n = int(input())

step = list(int(input()) for _ in range(n))
step.insert(0, 0)
step.insert(0, 0)

dp = [[0, 0] for _ in range(n + 2)]

dp[2][0] = step[2]

for i in range(3, n + 2):
    if dp[i-1][1] + i >= 2:
        if step[i] + step[i-1] + dp[i-3][0] > step[i] + dp[i-2][0]:
            dp[i][0], dp[i][1] = step[i] + step[i-1] + dp[i-3][0], 2
        else:
            dp[i][0], dp[i][1] = step[i] + dp[i-2][0], 1
    else:
        if step[i] + dp[i-1][0] > step[i] + dp[i-2][0]:
            dp[i][0], dp[i][1] = step[i] + dp[i-1][0], 2
        else:
            dp[i][0], dp[i][1] = step[i] + dp[i-2][0], 1

print(dp[n + 1][0])
