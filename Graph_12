# BOJ 1697

from collections import deque
import sys
sys.setrecursionlimit(10000000)

nx = [-1, 1]

def bfs():
    global n, k, mapp
    minn = 100000000

    while queue:
        x = queue.popleft()
        for i in range(3):
            if i > 1:
                dx = x * 2
            else:
                dx = x + nx[i]
            
            if dx >= 0 and dx < 100001:
                if mapp[dx] == 0:
                    mapp[dx] = mapp[x] + 1
                    queue.append(dx)
                
                if dx == k:
                    if minn < mapp[dx] + 1:
                        print(minn - 1)
                        return
                    minn = min(mapp[x] + 1, minn)


def main():
    global n, k, mapp, queue

    n, k = map(int, input().split())
    mapp = list(0 for _ in range(100001))
    queue = deque()

    if n == k:
        print(0)
        return
        
    mapp[n] = 1
    queue.append(n)

    bfs()    


if __name__ == '__main__':
    main()
