# BOJ 24416
# pypy

import sys
input = sys.stdin.readline


n = int(input())

f = [0 for _ in range(n + 1)]

method1 = 0
method2 = 0
def fib(n):
    global method1
    if n == 1 or n == 2:
        method1 = method1 + 1
        return 1  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    global method2
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        method2 = method2 + 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]


fib(n)
fibonacci(n)

# .format(fib(n), fibonacci(n))

print("{} {}" .format(method1, method2))
