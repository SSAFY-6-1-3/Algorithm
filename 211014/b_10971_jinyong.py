def permu(idx, N, last, value):
    global answer

    if idx == N-1:  # N-1 까지 갔다는 건 start 로 돌아오기 직전 마을에 도착했다는 뜻

        if not town[last][start]:  # 만약 돌아오는데 비용이 0 이면 갈 수 없는 경우!!
            return

        result = value + town[last][start]
        if result < answer:
            answer = result
        return

    if value >= answer:  # 중간까지의 비용이 현재 최솟값보다 큰 경우 가지치기
        return

    for i in range(N):  # last: 마지막으로 도착한 마을, i: 가고자 하는 마을

        if used[i]:  # 지나온 곳이면 넘어가기
            continue

        if not town[last][i]:  # 가려는 곳이 0 이면 => 경로가 없으면 패스
            continue

        used[i] = 1
        permu(idx + 1, N, i, value+town[last][i])
        used[i] = 0


N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]
t_lst = []
used = [0] * N
answer = 10000000

for start in range(N):  # start 부터 시작해서 start 까지 돌아오는 경로 탐색
    used[start] = 1
    permu(0, N, start, 0)

print(answer)
