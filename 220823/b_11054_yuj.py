# 기존 리스트 증가하는 부분 수열 + 역 리스트 증가하는 부분 수열
N = int(input())
A = list(map(int, input().split()))
rev = A[::-1]
dp1 = [1] * N
dp2 = [1] * N
for i in range(1, N):
    maxv1, maxv2 = 0, 0
    for j in range(i):
        if A[j] < A[i] and maxv1 < dp1[j]:
            maxv1 = dp1[j]
    for j in range(i):
        if rev[j] < rev[i] and maxv2 < dp2[j]:
            maxv2 = dp2[j]
    dp1[i] = maxv1 + 1
    dp2[i] = maxv2 + 1

ans = 0
for k in range(N):
    ans = max(ans, dp1[k]+dp2[N-k-1]-1)

print(ans)