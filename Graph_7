# BOJ 2667

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(count):
    global village, n, queue
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt = cnt + 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= 0 and nx < n and ny >= 0 and ny < n and village[nx][ny] == 1:
                village[nx][ny] = count
                queue.append((nx, ny))

    return cnt


def main():
    global village, n, queue
    village = []
    queue = deque()
    save = []

    n = int(input())

    for i in range(n):
        village.append(list(input()))
        village[i] = list(map(int, village[i]))
        
    count = 2
    for i in range(n):
        for j in range(n):
            if village[i][j] == 1:
                queue.append((i, j))
                village[i][j] = count
                x = bfs(count)
                save.append(x)
                count = count + 1

    # 오름차순 출력 필요 !    
    save.sort()

    print(len(save))

    for arr in save:
        print(arr)


if __name__ == '__main__':
    main()
