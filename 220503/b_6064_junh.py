import sys
input = sys.stdin.readline

T = int(input())

def calc(M, N, x, y):
    max_year = M*N
    y %=N
    year = x
    while year <= max_year:
        if year % N == y:
            return year
        year += M
    return -1


for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(calc(M, N, x, y))
