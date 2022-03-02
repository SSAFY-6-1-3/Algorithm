
dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def cost(r, c):
    ret = mat[r][c]
    for d in range(4):
        y, x = r+dY[d], c+dX[d]
        ret += mat[y][x]
    return ret

def recur(flowers, sum_cost):
    global min_cost
    if sum_cost > min_cost: return
    if len(flowers) == 3:
        min_cost = sum_cost
        return

    for i in range(1, N-1):
        for j in range(1, N-1):

            isOk = True
            for flower in flowers:
                y, x = flower
                if abs(y-i) + abs(x-j) < 3:
                    isOk = False
                    break

            if isOk:
                flowers.append([i, j])
                recur(flowers, sum_cost+cost_mat[i][j])
                flowers.pop()




N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
cost_mat = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N-1):
    for j in range(1, N-1):
        cost_mat[i][j] = cost(i, j)

min_cost = cost(1, 1) + cost(1, 4) + cost(4, 1)
recur([], 0)
print(min_cost)