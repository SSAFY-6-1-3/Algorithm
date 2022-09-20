# pypy로 통과
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
while K:

    # 봄, 여름
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                temp = []
                die = 0
                for tree in trees[i][j]:
                    if food[i][j] >= tree:
                        food[i][j] -= tree
                        # 나이 증가
                        temp.append(tree+1)
                    else:
                        die += tree // 2
                trees[i][j] = temp
                food[i][j] += die

    dp, dq = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    for p in range(N):
        for q in range(N):
            # 가을
            for tree in trees[p][q]:
                if not tree % 5:
                    for s in range(8):
                        np, nq = p+dp[s], q+dq[s]
                        if np in range(N) and nq in range(N):
                            trees[np][nq].append(1)
            # 겨울
            food[p][q] += A[p][q]
    K -= 1

ans = 0
for r in range(N):
    for c in range(N):
       ans += len(trees[r][c])
print(ans)