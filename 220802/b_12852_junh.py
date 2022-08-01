
N = int(input())
dp = [[N, 0] for _ in range(N+1)]
dp[1] = [0, 0]
for i in range(1, N+1):
    step = dp[i][0]
    if i * 3 <= N and step + 1 < dp[i*3][0]:
        dp[i*3] = [step + 1, i]
    if i * 2 <= N and step + 1 < dp[i*2][0]:
        dp[i*2] = [step + 1, i]
    if i < N and step + 1 < dp[i+1][0]:
        dp[i+1] = [step + 1, i]


print(dp[N][0])
st = str(N)
while dp[N][1]:
    N = dp[N][1]
    st += ' ' + str(N)
print(st)