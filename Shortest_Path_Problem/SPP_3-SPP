# BOJ 13549 - SPP

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = int(1e8)
MAXI = 200001

n, k = map(int, input().split())

graph = [[] for _ in range(MAXI)]

for i in range(0, 100001):
    if i + 1 < 100001:
        graph[i].append((i+1, 1))
    if i - 1 >= 0:
        graph[i].append((i-1, 1))
    if i * 2 < MAXI:
        graph[i].append((i*2, 0))

def dijkstra(node):
    distance = [INF] * MAXI
    distance[node] = 0
    heap = []
    heapq.heappush(heap, (0, node))
    
    while heap:
        w, node = heapq.heappop(heap)

        if distance[node] < w:
            continue

        for i in graph[node]:
            weight = w + i[1]
            if weight < distance[i[0]]:
                distance[i[0]] = weight
                heapq.heappush(heap, (weight, i[0]))


    return distance

dis = dijkstra(n)

print(dis[k])
