'''
youtube 설명 참고
https://youtu.be/xCbYmUPvc2Q?t=280
'''

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 물건 개수 / K : 가방 부피
    items = [list(map(int, input().split())) for _ in range(N)]  # [부피, 가치]

    bag_v = list([0] * (K + 1) for _ in range(N + 1))  # 0 ~ K 부피에 대해서 / 가치 최대화 선택(i번째 물건을 선택 or not)

    for i in range(1, N + 1):  # i번째 물건에 대해서
        volume, value = items[i - 1]

        for j in range(1, K + 1):  # 1 ~ K 부피를 채울 때,

            if j >= volume:        # 현재 채울 부피가 i번째 물건의 부피보다 클 때 (즉, 가방에 넣을 수 있을 때)
                bag_v[i][j] = max(bag_v[i - 1][j], bag_v[i - 1][j - volume] + value)   # 안 넣을 때 vs. 넣을 때

            else:  # 못 넣을 때
                bag_v[i][j] = bag_v[i - 1][j]  # 직전 행의 값 가져다 쓰기


    print('#{} {}'.format(tc, bag_v[-1][-1]))


'''
sol2. 부분집합 구하기
역시나 시간초과
'''
#
# def knapsack():
#     value = 0
#     for i in range(1 << N):
#         bag = [0, 0]  # V, C
#         for j in range(N-1, -1, -1):
#             if i & (1 << j):
#                 if bag[0] + objects[j][0] <= K:
#                     bag[0] += objects[j][0]
#                     bag[1] += objects[j][1]
#
#         if bag[1] > value:
#             value = bag[1]
#     return value
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     objects = [list(map(int, input().split())) for _ in range(N)]
#     ans = knapsack()
#     print('#{} {}'.format(tc, ans))
#



