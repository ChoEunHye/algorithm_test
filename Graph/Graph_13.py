# BOJ 7562

from collections import deque
import sys
sys.setrecursionlimit(10000000)

nx = [-2, -2, -1, -1, 1, 1, 2, 2]
ny = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    global startX, startY, finX, finY, num, queue, desk, minn
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx >= 0 and dx < num and dy >= 0 and dy < num:
                if desk[dx][dy] == 0:
                    desk[dx][dy] = desk[x][y] + 1
                    queue.append((dx, dy))
                if dx == finX and dy == finY:
                    if minn < desk[dx][dy] + 1:
                        print(minn - 1)
                        return
                    minn = min(desk[dx][dy], minn)


def main():
    global startX, startY, finX, finY, num, queue, desk, minn
    testCase = int(input())
    for _ in range(testCase):
        desk = []
        queue = deque()
        num = int(input())
        startX, startY = map(int, input().split())
        finX, finY = map(int, input().split())
        minn = 10000000
        for _ in range(num):
            desk.append(list(0 for _ in range(num)))
        
        desk[startX][startY] = 1
        if startX == finX and startY == finY:
            print(0)
            continue
        queue.append((startX, startY))

        bfs()


if __name__ == '__main__':
    main()
