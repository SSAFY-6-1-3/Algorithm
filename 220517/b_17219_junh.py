import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sites = {}
ans = ''

for _ in range(N):
    a, b = input().split()
    sites[a] = b

for _ in range(M):
    ans += sites[input().strip()] + "\n"

print(ans)