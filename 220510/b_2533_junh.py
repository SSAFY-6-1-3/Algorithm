from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
lines = [[] for _ in range(N+1)]    # 세트가 리스트보다 메모리 많이 사용

for _ in range(N-1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

def find_start():
    q = deque([1])
    visited = [False]*(N+1)
    visited[1] = True

    while q:
        now = q.popleft()
        for nxt in lines[now]:
            if visited[nxt] : continue
            visited[nxt] = True
            q.append(nxt)

    return now

def dfs(now):
    visited[now] = True
    dp[now][0] = 1

    for nxt in lines[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[now][0] += min(dp[nxt][0], dp[nxt][1])
            dp[now][1] += dp[nxt][0]

start = find_start()

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

dfs(start)
print(min(dp[start][0], dp[start][1]))


# def be_aa(n, aa_li):
#     my = 0
#     theirs = 0
#     ffs = set()
#     for f in lines[n]:
#         if not aa_li[f]:
#             my += 1
#             ffs.update(lines[f])
#
#     for ff in ffs:
#         if not aa_li[ff]:
#             theirs += 1
#
#     print(n, my, theirs)
#     print(aa_li)
#     if my > theirs:
#         return True
#
#     return False
#
# def check(start):
#     aa_li = [None] * (N+1)
#     aa_li[start] = be_aa(start, aa_li)
#     q = deque([start])
#
#     while q:
#         now = q.popleft()
#         is_aa = aa_li[now]
#         for nxt in lines[now]:
#             if aa_li[nxt] != None : continue
#
#
#             if not is_aa or be_aa(nxt, aa_li):
#                 aa_li[nxt] = True
#             else:
#                 aa_li[nxt] = False
#             q.append(nxt)
#
#     aa_li[0] = False
#     aas = sum(aa_li)
#     print(aa_li)
#     return aas
