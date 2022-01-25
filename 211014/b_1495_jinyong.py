def solution(result, idx):
    global answer

    if result > M or result < 0:
        return

    if idx == N:
        if result > answer:
            answer = result
        return

    if result+V[idx] <= M:
        solution(result+V[idx], idx+1)
    if result-V[idx] >= 0:
        solution(result-V[idx], idx+1)


def solution2():

    temp = [[0] * (M+1) for _ in range(N+1)]

    temp[0][S] = 1  # 시작하는 볼륨 크기에 1로 표시

    for i in range(1, N+1):  # 바꿀 볼륨에 하나씩 접근

        if temp[i-1] == [0] * (M+1):  # 바꾸려고 보니까 바로 전에 연주한 적이 없는 경우
            return -1  # 모든 곡을 연주할 수 없으니 -1 반환

        for j in range(M+1):  # 0 ~ M 범위 안에서 볼륨을 바꿔 연주해야 하니까 범위 설정

            if not temp[i-1][j]:  # 볼륨의 크기가 j 인 적이 없으면 패스
                continue

            if j + V[i] <= M and not temp[i][j + V[i]]:  # j로 연주했던 곡에 현재 볼륨 V[i] 만큼 더해도 M을 넘지 않는 경우
                temp[i][j + V[i]] = 1

            if 0 <= j - V[i] and not temp[i][j - V[i]]:  # j로 연주했던 곡에 현재 볼륨 V[i] 만큼 빼도 0 이상인 경우
                temp[i][j - V[i]] = 1

    ans = -1

    for i in range(M, -1, -1):  # 모든 곡을 연주했을 때 제일 크게 연주했던 볼륨을 찾아준다
        if temp[-1][i]:
            ans = i
            break

    return ans


N, S, M = map(int, input().split())
V = [0] + list(map(int, input().split()))
# solution(S, 0)
print(solution2())
