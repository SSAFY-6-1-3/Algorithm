import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def adopter(person):
    visited[person] = True
    dp[person][0] = 0 # 이 사람이 얼리어답터가 아닐때
    dp[person][1] = 1 # 얼리어답터일때

    for friend in tree[person]:
        if not visited[friend]:
            adopter(friend)
            dp[person][0] += dp[friend][1]
            dp[person][1] += min(dp[friend][0], dp[friend][1])


N = int(input())
tree = [list() for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


adopter(1)
print(min(dp[1][0], dp[1][1]))