def infection(com):
    rtn = 0
    queue = [com]
    computers[com] = True
    while queue:
        c = queue.pop(0)
        for i in range(1, T+1):
            if networks[c][i] and not computers[i]:
                queue.append(i)
                computers[i] = True
                rtn += 1
    return rtn



T = int(input())
N = int(input())
computers = [False] * (T+1)
networks = [[False]* (T+1) for _ in range(T+1)]
for _ in range(N):
    a, b = map(int, input().split())
    networks[a][b] = networks[b][a] = True
print(infection(1))