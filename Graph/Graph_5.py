# BaekJoon 2606

edge = []
computer = 0
virus = []
check = []

def virus(x):
    for i in range(len(edge[x])):
        if check[edge[x][i]]:
            continue
        check[edge[x][i]] = True
        virus(edge[x][i])

def main():
    computer = int(input())
    
    for i in range(computer):
        edge.append(list())
        check.append(False)
    
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        x = int(x)
        y = int(y)
        edge[x-1].append(y - 1)
        edge[y-1].append(x - 1)

    virus(0)
    count = 0
    for i in range(len(check)):
        if check[i]:
            count += 1

if __name__ == '__main__':
    main()
