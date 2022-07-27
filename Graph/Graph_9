# BOJ 2178

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global n, m, maze, queue

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                if nx == (n-1) and ny == (m-1):
                    return
                queue.append((nx, ny))


def main():
    global n, m, maze, queue
    maze = []
    queue = deque()

    n, m = map(int, input().split())
    
    for i in range(n):
        maze.append(list(input()))
        maze[i] = list(map(int, maze[i]))

    queue.append((0, 0))

    # 시작 위치는 다시 queue에 들어가지 않도록 0으로
    maze[0][0] = 0

    bfs()

    print(maze[n-1][m-1] + 1)
    

if __name__ == '__main__':
    main()
