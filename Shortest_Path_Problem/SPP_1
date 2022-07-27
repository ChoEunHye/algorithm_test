# BOJ 1753

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = int(1e8)


v, e = map(int, input().split())

graph = [[] for _ in range(v)]

k = int(input())

for i in range(e):
    u, d, w = map(int, input().split())
    graph[u - 1].append((d - 1, w))


def dijkstra(node):
    distance = [INF for _ in range(v)]
    distance[node] = 0
    heap = []
    heapq.heappush(heap, (0, node))
    
    while heap:
        d, n = heapq.heappop(heap)

        if distance[n] < d:
            continue

        for i in graph[n]:
            weight = d + i[1]
            if weight < distance[i[0]]:
                distance[i[0]] = weight
                heapq.heappush(heap, (weight, i[0]))


    return distance

result = dijkstra(k - 1)

for i in result:
    if i == INF:
        print("INF")
    else:
        print(i)

    
