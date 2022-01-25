import sys
input=sys.stdin.readline
# 전체 그래프 연결 개수 확인
def dfs(city):
    global result

    for i in planes[city]:
        if not visited[i]:
            result += 1
            visited[i] = 1
            dfs(i)

    return


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    planes = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        planes[a].append(b)
        planes[b].append(a)

    visited[1] = 1
    result = 0
    dfs(1)
    print(result)

################################################
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         a, b = map(int, input().split())
#
#     print(N-1)