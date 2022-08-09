# BOJ 10844

import sys
from collections import deque
input = sys.stdin.readline

DEV = 1000000000

queue = deque()

n = int(input())

dp = [0] * (n + 1)

dp[1] = 9
digit = [1] * (10)
digit[0] = 0

for i in range(2, n + 1):
    sum = 0
    for j in range(10):
        queue.append(digit[j])
        digit[j] = 0

    num = queue.popleft()
    digit[1] = (digit[1] + num) % DEV

    for j in range(1, 9):
        num = queue.popleft()
        digit[j-1] = (digit[j-1] + num) % DEV
        digit[j+1] = (digit[j+1] + num) % DEV

    num = queue.popleft()
    digit[8] = (digit[8] + num) % DEV

    for j in range(10):
        sum = (sum + digit[j]) % DEV
    
    dp[i] = sum

print(dp[n])
