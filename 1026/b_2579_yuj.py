import sys
sys.stdin=open('input.txt')

# 중간에서 최댓값이라고 마지막에서도 최댓값은 x

def score():
    stairs = [[0] * N for _ in range(2)]                        # 계단 위치, 1 연속 횟수 저장

    stairs[0][0], stairs[0][1] = lst[0], lst[1]                 # 시작위치에서 1칸 갈 경우, 2칸 갈 경우 초기값 설정

    for idx in range(N):
        if idx + 1 < N:                                         # 1칸 움직일 수 있는 경우 (전에 1칸 움직였으면 무조건 2칸 움직여야 함)
            stairs[1][idx + 1] = max(stairs[0][idx] + lst[idx + 1], stairs[1][idx + 1])
        if idx + 2 < N:                                         # 2칸 움직일 수 있는 경우 (전에 1칸 또는 2칸 움직인 경우 모두 가능)
            stairs[0][idx + 2] = max(stairs[0][idx] + lst[idx + 2], stairs[0][idx + 2])
            stairs[0][idx + 2] = max(stairs[1][idx] + lst[idx + 2], stairs[0][idx + 2])

    if stairs[0][-1] < stairs[1][-1]:
        return stairs[1][-1]
    else:
        return stairs[0][-1]


N = int(input())
lst = [int(input()) for _ in range(N)]

if N > 1:
    print(score())
else:                                     # 계단이 하나인 경우
    print(lst[-1])



