# BOJ 1956
# python3 X, pypy O

import sys
input = sys.stdin.readline

INF = float("inf")

v, e = map(int, input().split())

graph = [[INF]*(v) for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

stupid = INF

for i in range(v):
    ran = min(v, i+1)
    for j in range(ran):
        if i != j:
            stupid = min(stupid, graph[i][j] + graph[j][i])
        else:
            stupid = min(stupid, graph[i][j])

print(stupid if stupid != INF else -1)
