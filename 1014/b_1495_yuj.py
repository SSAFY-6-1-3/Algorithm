import sys
sys.stdin=open('input.txt')

N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
control = [[0] * (M+1) for _ in range(N+1)]

control[0][S] = 1                               # 0행 초기값 설정

for i in range(1, N+1):                         # 행 = 곡, 열 = 볼륨
    v = volume[i-1]                             # 현재 바꿀 볼륨 범위
    for j in range(M+1):                        # 전 곡 볼륨 확인
        if control[i-1][j] == 1:
            minus, plus = j - v, j + v
            if minus in range(M+1):             # 볼륨 바꾸고 범위 안에 있는지 확인(0 < x < M)
                control[i][minus] = 1           # 바뀐 볼륨 1로 표시해주기
            if plus in range(M+1):
                control[i][plus] = 1


for last in range(M, -1, -1):
    if control[N][last] == 1:
        print(last)
        break
else:
    print(-1)

# 재귀 풀이
# def control(cnt, nowV):
#     global maxV, flag
#
#     if nowV > M or nowV < 0:
#         return
#
#     if cnt == N:
#         maxV = max(maxV, nowV)
#         return
#
#     v = volume[cnt]
#     if nowV - v < 0 and nowV + v > M:
#         return
#     control(cnt+1, nowV - v)
#     control(cnt+1, nowV + v)
#
#
# control(0, S)
#
# if maxV == 0:
#     print(-1)
# else:
#     print(maxV)


# 메모리 에러
# for i in range(N):
#     for v in control[i]:
#
#         plus = int(v) + volume[i]
#         minus = int(v) - volume[i]
#
#         if 0 <= plus <= M:
#             control[i+1].append(str(plus))
#         if 0 <= minus <= M:
#             control[i+1].append(str(minus))
#
# if not control[-1] or max(control[-1]) == 0:
#     print(-1)
# else:
#     print(max(control[-1]))
