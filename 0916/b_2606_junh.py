def infection(com):
    rtn = 0 # 감염된 갯수
    queue = [com] # 큐. 시작 컴퓨터 하나 담음
    computers[com] = True # 시작 컴퓨터 감염 True
    while queue:
        c = queue.pop(0) # 큐의 컴퓨터 하나를 빼서
        for i in range(1, T+1):
            if networks[c][i] and not computers[i]: # c와 연결돼있고 감염이 안 된 컴퓨터는
                queue.append(i) # 큐에 담고
                computers[i] = True # 감염 True
                rtn += 1 # 감염수 +1
    return rtn



T = int(input())
N = int(input())
computers = [False] * (T+1)
networks = [[False]* (T+1) for _ in range(T+1)]
for _ in range(N):
    a, b = map(int, input().split())
    networks[a][b] = networks[b][a] = True
print(infection(1))