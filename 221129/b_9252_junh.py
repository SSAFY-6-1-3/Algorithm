A = ' ' + input()
B = ' ' + input()
dp = [['' for _ in range(len(B))] for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + A[i]
        else:
            a, b = dp[i-1][j], dp[i][j-1]
            if len(a) >= len(b):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

answer = dp[-1][-1]
print(len(answer))
print(answer)

