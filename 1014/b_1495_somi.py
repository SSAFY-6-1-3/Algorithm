N, S, M = map(int, input().split())
V_list = [0] + list(map(int, input().split()))

ans = -1

play = list([0] * (M + 1) for _ in range(N + 1))  # play[i][j] = i번째 행의 곡은 j 볼륨으로 연주 가능
play[0][S] = 1  # S 는 시작 볼륨

for next in range(1, N + 1):   # 1번 ~ N 까지 다음 곡에 대해서
    for v in range(M + 1):
        if play[next - 1][v]:  # 직전 곡의 볼륨

            if v + V_list[next] <= M:  # 직전 +
                play[next][v + V_list[next]] = 1

            if v - V_list[next] >= 0:   # 직전 -
                play[next][v - V_list[next]] = 1

for i in range(M, -1, -1):
    if play[N][i]:
        ans = i
        break

print(ans)