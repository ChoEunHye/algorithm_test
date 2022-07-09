# BOJ 7576

from collections import deque
import sys
sys.setrecursionlimit(10000000)

n = 0
m = 0
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

tomato = []
queue = deque()

def bfs():
    while len(queue) > 0:
        # array.pop(0)는 O(n), deque.popleft()는 O(1)로 시간적 복잡도에서 엄청난 차이가 있음
        x, y = queue.popleft()
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y

            if dx >= 0 and dx < n and dy >= 0 and dy < m and tomato[dx][dy] == 0:
                tomato[dx][dy] = tomato[x][y] + 1
                queue.append([dx, dy])

def main():
    global n, m
    m, n = map(int, input().split())
    for i in range(n):
        tomato.append(list(map(int, input().split())))
        #tomato.append(list(1 for _ in range(1000)))
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append([i, j])
    
    bfs()

    ans = -2
    check = False
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                check = True
        ans = max(ans, max(tomato[i]))
    
    if check:
        print("-1")
    else:
        print(ans - 1)

    

if __name__ == '__main__':
    main()
