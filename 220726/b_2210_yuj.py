def make(i, j, nums):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    if len(nums) == 6:
        answer.add(nums)
        return

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if ni in range(5) and nj in range(5):
            make(ni, nj, nums+str(board[ni][nj]))

board =[list(map(int, input().split())) for _ in range(5)]
answer = set()
for i in range(5):
    for j in range(5):
        make(i, j, str(board[i][j]))

print(len(answer))