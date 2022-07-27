# BOJ 11404
# Floyd

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = float('inf')

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

def floyd():
    distance = graph
    for k in range(n + 1):
        for i in range(n+1):
            for j in range(n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    return distance

result = floyd()

for i in range(1,n+1):
    for j in range(1, n+1):
        print(0 if result[i][j] == INF else result[i][j], end=" ")
    print()
