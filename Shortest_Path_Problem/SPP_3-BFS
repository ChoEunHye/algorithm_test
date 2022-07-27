# BOJ 13549 - BFS

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

INF = int(1e8)
MAXI = 200001

n, k = map(int, input().split())

graph = [INF for _ in range(MAXI)]
graph[n] = 0
queue = deque()
queue.append(n)

def bfs():

    while queue:
        now = queue.popleft()
        for i in (now + 1, now - 1):
            if i == k:
                if graph[i] > graph[now] + 1:
                    graph[i] = graph[now] + 1

            if i >= 0 and i < MAXI:
                if graph[i] > graph[now] + 1:
                    graph[i] = graph[now] + 1
                    queue.append(i)
        if now * 2 == k:
            if graph[now * 2] > graph[now]:
                graph[now * 2] = graph[now]

        if now * 2 >= 0 and now * 2 < MAXI:
            if graph[now*2] > graph[now]:
                graph[now*2] = graph[now]
                queue.append(now*2)

bfs()

print(graph[k])
