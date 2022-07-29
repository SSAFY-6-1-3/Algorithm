import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = [input() for _ in range(N)]

for i in range(len(S)):
    s = S[i]
    for j in range(1, len(s)):
        S.append(s[:j])
S = set(S)
answer = 0

for _ in range(M):
    if input().strip() in S:
        answer += 1

print(answer)
