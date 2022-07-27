# BOJ 1012

import sys
sys.setrecursionlimit(6000)

width = 0
height = 0
testCase = 0
earthworm = 0
field = []
fieldCheck = []

def dfs(x, y):
    if not (x >= 0 and x < h and y >= 0 and y < w):
        return
    
    fieldCheck[x][y] = earthworm

    if ((x - 1) >= 0 and (x - 1) < h and y >= 0 and y < w):
        if fieldCheck[x-1][y] == 0 and field[x-1][y] == 1:
            dfs(x-1, y)
    if ((x + 1) >= 0 and (x + 1) < h and y >= 0 and y < w):
        if fieldCheck[x+1][y] == 0 and field[x+1][y] == 1:
            dfs(x+1, y)
    if (x >= 0 and x < h and (y - 1) >= 0 and (y - 1) < w):
        if fieldCheck[x][y-1] == 0 and field[x][y-1] == 1:
            dfs(x, y-1)
    if (x >= 0 and x < h and (y + 1) >= 0 and (y + 1) < w):
        if fieldCheck[x][y+1] == 0 and field[x][y+1] == 1:
            dfs(x, y+1)

def main():
    global w, h, field, fieldCheck, earthworm
    testCase = int(input())
    
    for i in range(testCase):
        field = []
        fieldCheck = []

        x, y, z = map(int, input().split())
        w = int(x)
        h = int(y)
        z = int(z)
        earthworm = 0
        
        for _ in range(h):
            field.append([0 for _ in range(w)])
            fieldCheck.append([0 for _ in range(w)])

        for _ in range(z):
            a, b = map(int, input().split())
            field[b][a] = 1

        for a in range(h):
            for b in range(w):
                if field[a][b] == 1 and fieldCheck[a][b] == 0:
                    earthworm += 1
                    dfs(a, b)

        print(earthworm)

if __name__ == '__main__':
    main()
