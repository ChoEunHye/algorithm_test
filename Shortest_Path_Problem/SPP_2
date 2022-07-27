# BOJ 1504

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = int(1e8)


v, e = map(int, input().split())

graph = [[] for _ in range(v)]

for i in range(e):
    u, d, w = map(int, input().split())
    graph[u - 1].append((d - 1, w))
    graph[d - 1].append((u - 1, w))

v1, v2 = map(int, input().split())

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

startDis = dijkstra(0)
v1Dis = dijkstra(v1 - 1)
v2Dis = dijkstra(v2 - 1)

result = min((startDis[v1-1] + v1Dis[v2-1] + v2Dis[v - 1]), (startDis[v2-1] + v2Dis[v1-1] + v1Dis[v - 1]))

print("-1" if result >= INF else result)
