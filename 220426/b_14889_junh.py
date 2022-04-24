N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
starts = []

def team_start(team):
    if len(team) == N//2:
        starts.append(team)
        return
    for i in range(team[-1]+1, N):
        team_start(team+[i])

team_start([0])

def team_power(team):
    power = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            power += mat[a][b] + mat[b][a]
    return power

min_gap = float('inf')

for start in starts:
    link = [i for i in range(N) if i not in start]
    gap = team_power(start) - team_power(link)
    min_gap = min(min_gap, abs(gap))

print(min_gap)