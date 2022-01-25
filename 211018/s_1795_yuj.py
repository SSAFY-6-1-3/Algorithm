import sys
sys.stdin=open('input.txt')
# 최단거리 구하기!!
def dijkstra(s, G):
    D = [0] + [987654321] * N                               # 인덱스 맞추기 위해서 0 추가
    D[s] = 0                                                # 시작 인덱스 0
    visited = [0] * (N+1)

    for _ in range(N):
        minidx = -1
        minV = 987654321

        for k in range(1, N+1):                             # 시작할 위치 찾기
            if not visited[k] and D[k] < minV:              # 아직 방문하기 전인 집 중에 제일 작은 값 -> 이미 최솟값으로 나왔으니까 더 볼 필요 x
                minV = D[k]
                minidx = k

        visited[minidx] = 1

        for i in range(1, N+1):                             # 현위치랑 연결된 집들 중 갱신할 수 있으면 갱신
            if G[minidx][i]:
                if not visited[i] and D[minidx] + G[minidx][i] < D[i]:       # 기존값보다 작으면 새로 저장
                    D[i] = D[minidx] + G[minidx][i]

    return D


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    go = [[0] * (N+1) for _ in range(N+1)]       # 인수집 가는 그래프
    back = [[0] * (N+1) for _ in range(N+1)]     # 다시 집으로 오는 그래프
    for _ in range(M):
        x, y, c = map(int, input().split())
        go[y][x] = c                              # 맨 뒤(인수집)부터 올 거니까 연결관계 거꾸로 설정 - 인수집 갈 떄
        back[x][y] = c                            # 인수집에서 올 때

    result1 = dijkstra(X, go)
    result2 = dijkstra(X, back)
    result = [0] * (N+1)
    for idx in range(N+1):                        # 올 때, 갈 때 더해주기
        result[idx] = result1[idx] + result2[idx]

    print('#{} {}'.format(tc, max(result)))
