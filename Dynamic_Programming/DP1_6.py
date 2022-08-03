# BOJ 1149
# [] * () -> 하나의 주소를 가진 리스트

import sys
input = sys.stdin.readline

MAX = 1000

n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = cost[0]

for i in range(1, n):
    dp[i][0] = min(cost[i][0] + dp[i-1][1], cost[i][0] + dp[i-1][2])
    dp[i][1] = min(cost[i][1] + dp[i-1][0], cost[i][1] + dp[i-1][2])
    dp[i][2] = min(cost[i][2] + dp[i-1][0], cost[i][2] + dp[i-1][1])

print(min(dp[n-1]))
