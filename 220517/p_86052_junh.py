# 상 좌 하 우
dR = (-1, 0, 1, 0)
dC = (0, -1, 0, 1)
move = {
    'S':0,
    'L':1,
    'R':-1
}
def solution(grid):
    answer = []
    rows, cols = len(grid), len(grid[0])
    checked = [[[False]*4 for _ in range(cols)] for _ in range(rows)]

    def start(r, c, d):
        cnt = 0
        while not checked[r][c][d]:
            checked[r][c][d] = True
            #방향 돌리고 움직이기
            d = (move[grid[r][c]] + d + 4) % 4
            r = (r + dR[d] + rows) % rows
            c = (c + dC[d] + cols) % cols
            cnt += 1

        return cnt

    for i in range(rows):
        for j in range(cols):
            for k in range(4):
                if not checked[i][j][k]:
                    answer.append(start(i, j, k))

    return sorted(answer)

print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))