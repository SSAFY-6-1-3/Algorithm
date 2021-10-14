import sys
sys.stdin=open('input.txt')

def TSP(idx, expense, visited):
    global result
    if expense > result:                                # 현재 최솟값보다 이미 더 큰 경우 가지치기
        return

    if len(visited) == N:                               # 모든 지역 다 방문했으면
        if city[idx][start]:                            # 최솟값 확인
            expense += city[idx][start]                 # 원래 도시로 돌아오는 비용도 마지막에 더해주기
            if expense < result:
                result = expense
        return

    for j in range(N):                                  # 방문하지않았고 도시 비용이 0이 아니라면 확인
        if j not in visited and city[idx][j] != 0:
            TSP(j, expense+city[idx][j], visited+[j])

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
result = 1000000*N*N

for m in range(N):                                      # 시작위치를 모든 지점으로 해보기
    start = m
    TSP(m, 0, [m])                                      # (시작위치, 비용, 방문확인)

print(result)