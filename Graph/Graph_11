# BOJ 7569

from collections import deque
import sys
sys.setrecursionlimit(10000000)

n = 0
m = 0
h = 0
nh = [-1, 1, 0, 0, 0, 0]
nx = [0, 0, -1, 1, 0, 0]
ny = [0, 0, 0, 0, -1, 1]

tomato = []
queue = deque()

def bfs():
    while len(queue) > 0:
        l, x, y = queue.popleft()
        for i in range(6):
            dh = nh[i] + l
            dx = nx[i] + x
            dy = ny[i] + y

            if dh >= 0 and dh < h and dx >= 0 and dx < n and dy >= 0 and dy < m and tomato[dh][dx][dy] == 0:
                tomato[dh][dx][dy] = tomato[l][x][y] + 1
                queue.append([dh, dx, dy])

def main():
    global n, m, h
    m, n, h = map(int, input().split())

    for a in range(h):
        tomato.append(list())
        for i in range(n):
            tomato[a].append(list(map(int, input().split())))
            #tomato.append(list(1 for _ in range(1000)))
            for j in range(m):
                if tomato[a][i][j] == 1:
                    queue.append([a, i, j])
    
    bfs()

    ans = -2
    check = False
    for l in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[l][i][j] == 0:
                    check = True
            ans = max(ans, max(tomato[l][i]))
    
    if check:
        print("-1")
    else:
        print(ans - 1)
    

if __name__ == '__main__':
    main()
