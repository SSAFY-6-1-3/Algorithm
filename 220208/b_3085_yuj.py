def check(arr):
    maxl = 0
    for x in range(N):
        cnt, col_cnt = 1, 1
        color = arr[x][0]
        color_col = arr[0][x]
        for y in range(1, N):
            if color == arr[x][y]:
                cnt += 1
            else:
                maxl = max(cnt, maxl)
                cnt = 1
                color = arr[x][y]
            if color_col == arr[y][x]:
                col_cnt += 1
            else:
                maxl = max(col_cnt, maxl)
                col_cnt = 1
                color_col = arr[y][x]
        maxl = max(cnt, maxl)
        maxl = max(col_cnt, maxl)
    return maxl

N = int(input())
candies = []
for _ in range(N):
    candies.append(list(input()))

di = [1, 0]
dj = [0, 1]
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(N) and nj in range(N):
                if candies[i][j] != candies[ni][nj]:
                    candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]
                    ans = max(ans, check(candies))
                    candies[i][j], candies[ni][nj] = candies[ni][nj], candies[i][j]
print(ans)