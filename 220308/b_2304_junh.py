import sys
input = sys.stdin.readline

def go_right(idx):
    global ans
    if idx == N-1:
        return

    new_i = max(bars[idx+1:], key= lambda x:x[1][1])[0]
    ans += (bars[new_i][1][0]-bars[idx][1][0]) * bars[new_i][1][1]

    go_right(new_i)

def go_left(idx):
    global ans
    if idx == 0:
        return

    new_i = max(bars[:idx], key=lambda x: x[1][1])[0]
    ans += (bars[idx][1][0] - bars[new_i][1][0]) * bars[new_i][1][1]

    go_left(new_i)



N = int(input())
bars = [list(map(int, input().split())) for _ in range(N)]
bars.sort()
bars = list(enumerate(bars))
start = max(bars, key= lambda x:x[1][1])[0]

ans = bars[start][1][1]

go_right(start)
go_left(start)
print(ans)