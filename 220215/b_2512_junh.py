

def solve(N, li, limit):
    li.sort()
    rest = limit
    if limit//N < li[0] : return limit//N

    for i in range(N-1):
        rest -= li[i]
        limit_for_one = rest // (N - i - 1)
        if limit_for_one <= li[i+1]:
            return limit_for_one

    return li[-1]

N = int(input())
li = list(map(int, input().split()))
limit = int(input())
print(solve(N, li, limit))