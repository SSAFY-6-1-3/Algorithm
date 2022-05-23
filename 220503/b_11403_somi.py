N = int(input())
path = list(list(input().split()) for _ in range(N))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if path[j][i] == '1' and path[i][k] == '1':
                path[j][k] = '1'

for r in path:
    print(' '.join(r))
