import sys

input = sys.stdin.readline

N, M = map(int, input().split())

sts = set()
for _ in range(N):
    sts.add(input().strip())
answer = 0

for _ in range(M):
    s = input().strip()
    if s in sts:
        answer += 1

print(answer)
