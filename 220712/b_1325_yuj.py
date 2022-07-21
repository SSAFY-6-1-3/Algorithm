# pypy
import sys
from collections import deque

def check(s):
    global checked, computer

    deq = deque([s])
    while deq:
        n = deq.popleft()
        for com in computer[n]:
            if not checked[com]:
                deq.append(com)
                checked[com] = 1

input = sys.stdin.readline
N, M = map(int, input().split())
computer = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    computer[B].append(A)

max_cnt = 0
cnt = [0] * (N+1)
for num in range(1, N+1):
    checked = [0] * (N+1)
    checked[num] = 1
    check(num)
    temp = sum(checked)
    if temp >= max_cnt:
        max_cnt = temp
    cnt[num] = temp

ans = []
for i in range(1, N+1):
    if cnt[i] == max_cnt:
        ans.append(i)
ans.sort()
print(*ans)