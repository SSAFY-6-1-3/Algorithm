import sys
input = sys.stdin.readline

N = int(input())

routes = [[] for _ in range(N+1)]
dp = [float('inf')]*(N+1)
dp[0], dp[1] = 0, 0
for _ in range(N-1):
    a, b, c = map(int, input().split())
    routes[a].append([b, c])
    routes[b].append([a, c])

def bfs(routes, dp):
    q = [1]
    idx = 0
    while idx<len(q):
        n = q[idx]
        idx +=1
        for i, c in routes[n]:
            if dp[i]> dp[n]+c:
                dp[i] = dp[n]+c
                q.append(i)
    return max(dp)

print(bfs(routes, dp))