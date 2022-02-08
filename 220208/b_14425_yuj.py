# N, M = map(int, input().split())
# S = set()
# for _ in range(N+M):
#     S.add(input())
#
# print(N+M-len(S))

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())

ans = 0
for _ in range(M):
    if input() in S:
        ans += 1
print(ans)