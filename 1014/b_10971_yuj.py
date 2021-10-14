import sys
sys.stdin=open('input.txt')

def TSP(idx, expense, visited):
    global result
    if expense > result:
        return

    if len(visited) == N:
        if city[idx][start]:
            expense += city[idx][start]
            if expense < result:
                result = expense
        return

    for j in range(N):
        if j not in visited and city[idx][j] != 0:
            TSP(j, expense+city[idx][j], visited+[j])

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
result = 1000000*N*N

for m in range(N):
    start = m
    TSP(m, 0, [m])

print(result)