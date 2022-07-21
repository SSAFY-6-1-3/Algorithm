N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
answer = 64
for start_x in range(N-7):
    for start_y in range(M-7):
        temp1, temp2 = 0, 0
        for x in range(start_x, start_x+8):
            for y in range(start_y, start_y+8):
                if (x - start_x + y - start_y) % 2:
                    if board[x][y] == 'W':              # temp1은 W로 시작하는 경우
                        temp1 += 1
                    else:                               # temp2는 B로 시작하는 경우
                        temp2 += 1
                else:
                    if board[x][y] == 'B':
                        temp1 += 1
                    else:
                        temp2 += 1
        answer = min(answer, temp1, temp2)

print(answer)