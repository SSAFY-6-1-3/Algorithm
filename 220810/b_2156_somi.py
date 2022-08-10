n = int(input())
wine = list(int(input()) for _ in range(n))
dp = [0] * n

if n < 3:
    print(sum(wine))

else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
                   # O/X  X ,      O/X X  O  O,                       O/X X O
    print(dp[n - 1])

'''
#88%
n = int(input())
glass = list([0] * n for _ in range(4))

if n < 3:
    wine = list(int(input()) for _ in range(n))
    print(sum(wine))

else:
    first = int(input())
    glass[0][0], glass[1][0], glass[2][0], glass[3][0] = first, first, first, first

    second = int(input())
    glass[0][1], glass[1][1], glass[2][1], glass[3][1] = second, first + second, second, first + second

    for i in range(2, n):
        wine = int(input())
        glass[0][i] = wine
        glass[1][i] = glass[2][i - 1] + wine  # 직전 와인 마시는 경우
        glass[2][i] = max(glass[3][i - 2], glass[3][i - 3], glass[3][i - 4]) + wine
        glass[3][i] = max(glass[1][i], glass[2][i])

    print(max(glass[3][n - 1], glass[3][n - 2], glass[3][n - 3]))
'''