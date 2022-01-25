import sys
input = sys.stdin.readline

def solution(short_cut, D):
    start, end, dist = short_cut
    if end not in range(D+1): return
    new_end = dp[start]+dist
    if new_end >= dp[end]: return
    dp[end] = new_end
    for i in range(D+1-end):
        dp[end+i] = dp[end]+i


N, D = map(int, input().split())
short_cuts = []
dp = [i for i in range(D+1)]

for _ in range(N):
    short_cut = list(map(int, input().split()))
    short_cuts.append(short_cut)


short_cuts.sort(key= lambda x: x[1])

for short_cut in short_cuts:
    solution(short_cut, D)


print(dp[D])