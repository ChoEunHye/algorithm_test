# BOJ 1707
# 이분 그래프 기억하자 !

from collections import deque
import sys
sys.setrecursionlimit(10000000)

def bfs():
    global color, edge, v, e, check, queue, visit

    while queue:
        node = queue.popleft()
        for i in edge[node]:
            if visit[i] == 0:
                if color[node] == 1:
                    color[i] = 2
                else:
                    color[i] = 1
                visit[i] = 1
                queue.append(i)
            elif color[i] == color[node]:
                check = True
                return
            
def main():
    global color, edge, v, e, check, queue, visit

    testCase = int(sys.stdin.readline())
    for _ in range(testCase):
        v, e = map(int, sys.stdin.readline().split())
        color = list(0 for _ in range(v + 1))
        visit = list(0 for _ in range(v + 1))
        edge = [list() for _ in range(v + 1)]
        queue = deque()

        for _ in range(e):
            s, f = map(int, sys.stdin.readline().split())
            edge[s].append(f)
            edge[f].append(s)
        
        check = False
        for i in range(1, v + 1):
            if visit[i] == 0:
                queue.append(i)
                visit[i] = 1
                color[i] = 1
                bfs()
                if check:
                    break
        
        if check:
            print('NO')
        else:
            print('YES')

        del edge, color, queue, visit


if __name__ == '__main__':
    main()
