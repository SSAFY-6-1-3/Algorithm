import sys

sys.stdin = open('2117.txt')


def service(point, K, answer):  # 범위가 K 로 주어질 때의 영역을 탐색하기 위한 함수

    r, c = point  # 시작 점

    expense = K ** 2 + (K - 1) ** 2  # 영역의 크기 = 서비스 비용
    revenue = 0  # 수입

    if answer // M > expense:  # 지금까지 나온 집의 수가 영역 비용보다 크면 함수 끝....
        return 0

    s_r = r - (K - 1)  # 행의 시작 지점
    b_r = r + (K - 1)  # 행의 끝 지점
    k = -1  # 해당 행의 열 범위
    plus = True  # 열 범위가 증가하는지, 감소하는지 판단할 변수

    for i in range(s_r, b_r + 1):  # 행의 시작부터 끝까지 탐색

        if plus:  # 열 범위를 증가시켜야 하는 경우
            k += 1
        else:
            k -= 1

        for j in range(c-k, c + k + 1):  # 열은 행이 몇 번째냐에 따라 범위가 달라진다
            if i < 0 or i >= N or j < 0 or j >= N:  # 현재 보고 있는 좌표가 범위를 벗어나면 패스
                continue
            if town[i][j] == 1:  # 해당 범위에 집이 있으면 수입을 M 만큼 증가
                revenue += M

        if k == K - 1:  # 만약 열 범위의 증가치가 K와 같아지면 감소해야 한다
            plus = False

    if revenue >= expense:  # 수익이 더 많은 경우
        return revenue  # 수익 반환
    return 0


def solution():

    answer = 0

    for i in range(N):
        for j in range(N):
            point = [i, j]
            for k in range(1, N+2):  # 정중앙의 집을 기준으로 k+1 범위의 영역을 탐색하는게 최대다
                temp = service(point, k, answer)
                if answer < temp:
                    answer = temp

    return answer // M


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {solution()}')
