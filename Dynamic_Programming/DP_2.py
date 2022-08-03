# BOJ 9184

import sys
input = sys.stdin.readline

# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if a < b and b < c:
#         return w(a, b, c - 1) + w(a, b-1, c-1) - w(a, b-1, c)
#     else:
#         return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for k in range(1, 21):
    for i in range(1, 21):
        for j in range(1, 21):
            if k < i and i < j:
                dp[k][i][j] = dp[k][i][j-1] + dp[k][i-1][j-1] - dp[k][i-1][j]
            else:
                dp[k][i][j] = dp[k-1][i][j] + dp[k-1][i-1][j] + dp[k-1][i][j-1] - dp[k-1][i-1][j-1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = dp[20][20][20]
    else:
        answer = dp[a][b][c]

    print("w({}, {}, {}) = {}" .format(a, b, c, answer))
