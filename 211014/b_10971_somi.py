
def cities(n, k, cost):
    global min_cost
    if k == n:  # 다 돌아본 경우,
        if arr[city[-1]][city[0]]:
            cost = cost + arr[city[-1]][city[0]]
            if cost < min_cost:
                min_cost = cost

    for j in range(N): # k 번째 갈 도시 정하기
        if j not in city:  # 아직 가본 도시 아니라면
            city[k] = j
            next_cost = cost + arr[city[k-1]][j]  # 다음 도시까지의 총 예산
            if next_cost != cost and next_cost < min_cost: # 다음 도시를 갈 수 있고(0이 아니고) min보다 작다면
                cities(n, k + 1, next_cost)
            city[k] = -1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

city = [-1] * N
min_cost = 10000000

for i in range(N): # 0번 ~ N-1번 도시 중 첫 번째 도시 정하기
    city[0] = i
    cities(N, 1, 0)
    city[0] = -1

print(min_cost)
