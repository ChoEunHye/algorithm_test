# BOJ 16928

queue = []
lad = []
sna = []
mapp = [10000 for _ in range(101)]
ans = 10000

def bfs():
    global ans
    while len(queue) > 0:
        now, count = queue.pop(0)
        check = 0
        if now == 100:
            ans = min(ans, count)
            continue

        for i, j in lad:
            if i == now:
                check = j
                break
            if i > now:
                break

        if check != 0:
            queue.append((check, count))
            mapp[check] = min(mapp[check], count)
            continue

        check = 0

        for i, j in sna:
            if i == now:
                check = j
                break
            if i > now:
                break

        if check != 0:
            queue.append((check, count))
            mapp[check] = min(mapp[check], count)
            continue
        

        for i in range(6, 0, -1):
            if now + i <= 100:
                if mapp[now + i] > count + 1:
                    queue.append((now + i, count + 1))
                    mapp[now + i] = min(mapp[now + i], count + 1)

def main():
    n, m = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())
        lad.append((x, y))

    for _ in range(m):
        x, y = map(int, input().split())
        sna.append((x, y))
    
    lad.sort()
    sna.sort()

    queue.append((1, 0))
    bfs()
    print(ans)

if __name__ == '__main__':
    main()
