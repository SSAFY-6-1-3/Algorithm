from math import gcd

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    max_year = M * N // gcd(M, N)
    first, second = 0, 0
    year = x
    flag = False

    if M == x and N == y:
        print(year)

    while year <= max_year:
        if y != N and year % N == y:
            print(year)
            break

        elif y == N and year % N == 0:
            print(year)
            break

        year += M

    if year > max_year:
        print(-1)
