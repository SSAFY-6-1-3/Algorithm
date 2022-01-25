d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def group(r, c):
    cnt = 1
    stack = [(r, c)]
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i + d[k][0], j + d[k][1]
            if 0 <= ni < N and 0 <= nj < N and town[ni][nj] == 1:
                stack.append((ni, nj))
                town[ni][nj] = 0
                cnt += 1
    return cnt

N = int(input())
town = [list(map(int, input())) for _ in range(N)]
houses = []

for r in range(N):
    for c in range(N):
        if town[r][c] == 1:
            town[r][c] = 0
            houses.append(group(r, c))

# Print objects to the text stream file, separated by sep and followed by end
# sep = ' '가 default
print(len(houses), *sorted(houses), sep='\n')