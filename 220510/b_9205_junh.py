import sys
input = sys.stdin.readline

def is_able(a, b):
    dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
    if dist <= 1000:
        return True
    return False

def bfs(cnvs,fest):
    q = [0]
    idx = 0

    while idx < len(q):
        now = q[idx]
        idx += 1

        if is_able(cnvs[now], fest):
            return 'happy'

        for i in range(n+1):
            if i not in q and is_able(cnvs[now], cnvs[i]):
                q.append(i)
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    cnvs = [list(map(int, input().split())) for _ in range(n+1)]
    fest = list(map(int, input().split()))

    print(bfs(cnvs, fest))



# def check(n, cnvs, fest):
#     now = 0
#     while not is_able(cnvs[now], fest):
#         for i in range(n, 0, -1):
#             if is_able(cnvs[now], cnvs[i]):
#                 now = i
#                 break
#         else:
#             break
#     else:
#         return 'happy'
#     return 'sad'

# def dfs(now, visited):
#     global status
#     if is_able(cnvs[now], fest):
#         print('happy')
#         exit()
#
#     for i in range(n+1):
#         if i not in visited and is_able(cnvs[now], cnvs[i]):
#             visited.add(i)
#             dfs(i, visited)
#             visited.remove(i)