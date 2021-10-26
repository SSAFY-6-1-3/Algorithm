
N = int(input())
stairs = [0] + list(int(input()) for _ in range(N))

# 이 부분없으니까 런타임 에러...
if N == 1:
    print(stairs[-1])


else:
    dp = [0, stairs[1], max(stairs[1] + stairs[2], stairs[2])] + [0] * (N - 2)

    for i in range(3,  N + 1):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[-1])



'''
# 아...........????ㅎㅎ
def up(now, sum_now):
    global ans
    if now == N - 2 and ans < sum_now:
        ans = sum_now

        return

    if now + 1 < N - 1:
        visited[now + 1] = True
        up(now + 1, sum_now + stairs[now + 1])
        visited[now + 1] = False

    if now + 2 < N - 1:
        visited[now + 2] = True
        up(now + 2, sum_now + stairs[now + 2])
        visited[now + 2] = False



N = int(input())
stairs = list(int(input()) for _ in range(N))
visited = [False] * N
ans = 0
up(-1, stairs[-1])
print(ans)

'''

