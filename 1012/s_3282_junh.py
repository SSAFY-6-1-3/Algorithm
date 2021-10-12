import sys

sys.stdin = open('s_3282.txt')

# def bag(idx, val, wgt):
#     if val >= wgt_val[wgt]:
#         wgt_val[wgt]= val
#         if wgt == K : print(idx)
#     else:
#         return
#
#     for i in range(idx+1, N):
#         if wgt + lst[i][0] <= K:
#             bag(i,val + lst[i][1], wgt + lst[i][0])
#         else:
#             break

def bag_dp(N, K):
    for i in range(N):
        w, v = lst[i][0], lst[i][1]
        for j in range(K, w-1, -1):
            wgt_val[j] = max(wgt_val[j], wgt_val[j-w] + v)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().strip().split())
    lst = sorted([list(map(int, input().strip().split())) for _ in range(N)],key=lambda x: (x[0], -x[1]))
    wgt_val = [0] * (K+1) # 무게와 가치
    # bag(-1, 0, 0)
    bag_dp(N, K)
    print('#{} {}'.format(tc, max(wgt_val)))