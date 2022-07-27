# BOJ 9370

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = int(1e8)

def dijkstra(node):
    distance = [INF] * (n + 1)
    distance[node] = 0
    heap = []
    heapq.heappush(heap, (0, node))

    while heap:
        w, now = heapq.heappop(heap)

        if distance[now] < w:
            continue
        for i in graph[now]:
            weight = w + i[1]
            if weight < distance[i[0]]:
                distance[i[0]] = weight
                heapq.heappush(heap, (weight, i[0]))

    return distance

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    goal = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        goal.append(int(input()))

    startDis = dijkstra(s)
    gDis = dijkstra(g)
    hDis = dijkstra(h)

    result = []
    for i in goal:
        tmp = min((startDis[g] + gDis[h] + hDis[i]), (startDis[h] + hDis[g] + gDis[i]))
        if tmp <= startDis[i]:
            result.append(i)
    
    heapq.heapify(result)

    for i in range(len(result)):
        print(heapq.heappop(result), end=" ")
    print()
