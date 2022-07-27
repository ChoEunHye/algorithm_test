# BOJ 11657
# Bellman-Ford

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = float('inf')

n, m = map(int, input().split())

graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def dijkstra(node):
    distance = [INF] * (n + 1)
    distance[node] = 0
    
    for i in range(n):
        for a, b, c in graph:
            if distance[a] != INF and distance[b] > distance[a] + c:
                if i == n - 1:
                    return -1
                distance[b] = distance[a] + c

    return distance

result = dijkstra(1)
if result == -1:
    print(-1)
else:
    for i in result[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)
