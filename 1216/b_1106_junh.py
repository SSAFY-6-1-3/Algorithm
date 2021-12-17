import sys

input = sys.stdin.readline

def adv(C, N, cities):
    cities.sort(key=lambda x: -(x[1]/x[0]))
    dp_size = max(cities, key=lambda x:x[1])[1]

    rest_dp = [999999999] * (C+dp_size+1)
    rest_dp[0] = 0
    for i in range(1, C+dp_size+1):
        for c in cities:
            if i<c[1]: continue
            rest_dp[i] = min(rest_dp[i], rest_dp[i-c[1]]+c[0])
    return min(rest_dp[C:])

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

print(adv(C, N, cities))

# def adv(C, N, cities):
#     cities.sort(key=lambda x: -(x[1] / x[0]))
#
#     pp = C // cities[0][1] * cities[0][1] * cities[0][1]
#     cst = C // cities[0][1] * cities[0][0]
#
#     if pp == C:
#         return cst
#
#     dp_size = max(cities, key=lambda x: x[1])[1]
#     rest_dp = [1000] * (dp_size + 1)
#     rest_dp[0] = 0
#     for i in range(1, dp_size + 1):
#         for c in cities:
#             if i < c[1]: continue
#             rest_dp[i] = min(rest_dp[i], rest_dp[i - c[1]] + c[0])
#     return cst + min(rest_dp[C - pp:])