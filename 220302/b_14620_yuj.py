N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
ans = 200 * N * N
visited = [[0] * N for _ in range(N)]
total_expense = 0
da = [0, -1, 1, 0, 0]
db = [0, 0, 0, -1, 1]

# 가격 계산하기
def seed(i, j):
    expense = 0
    for k in range(5):
        expense += garden[i+da[k]][j+db[k]]
    return expense

# visited 체크하기
def make_one(i, j):
    global visited

    for k in range(5):
        visited[i+da[k]][j+db[k]] = 1

# visited 풀어주기
def make_zero(i, j):
    global visited

    for k in range(5):
        visited[i+da[k]][j+db[k]] = 0

# 방문한 적 없는 지 체크
def check(i, j):
    for k in range(5):
        ni, nj = i + da[k], j + db[k]
        if visited[ni][nj]:
            return False
    return True


def dfs(cnt, total):
    global visited, ans

    if cnt == 3:
        if ans > total:
            ans = total
        return
    else:
        for i in range(1, N - 1):                   # 가장자리에는 씨앗을 심을 수 없으므로
            for j in range(1, N - 1):
                if check(i, j):
                    temp = seed(i, j)
                    make_one(i, j)
                    dfs(cnt+1, total+temp)
                    make_zero(i, j)

dfs(0, 0)
print(ans)