import sys
sys.stdin=open('sample_input.txt')
def find(x, y, K):
    cnt = 0
    for i, j in home:                   # 집과 마름모의 중심사이의 거리가 K 이하면 마름모 안에 포함된다고 볼 수 있다
        if abs(i-x) + abs(j-y) < K:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    service = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):                  # 집 위치 모두 저장
        for j in range(N):
            if service[i][j] == 1:
                home.append([i, j])

    cnt_lst = []
    for K in range(N+1, 0, -1):         # 가장 큰 마름모부터 확인(N*N이 마름모 안에 들어올 수 있는 크기)
        cost = (K*K) + (K-1)*(K-1)      # 운영비용
        if cost > len(home) * M:        # 모든 집을 통해 얻는 수익이 운영비용보다 작다면 가지치기
            continue

        for x in range(N):              # 모든 위치를 돌면서 마름모 중심으로 생각
           for y in range(N):
                cnt = find(x, y, K)     # 마름모 안에 포함되는 집 개수
                if cnt*M >= cost:
                    cnt_lst.append(cnt)

    print('#{} {}'.format(tc, max(cnt_lst)))


