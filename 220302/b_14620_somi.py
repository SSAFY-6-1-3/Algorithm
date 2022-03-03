dr = [0, 0, 1, 0, -1]  # 꽃 위치
dc = [0, 1, 0, -1, 0]

def check(r, c):  # 화단 밖으로 나가거나 겹치는 경우 없는 지 확인
    for i in range(5):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if next_r < 0 or next_r > N or next_c < 0 or next_c > N or visited[next_r][next_c]:
            return False
    return True


def flower(cnt, price):
    global total_price
    if price > total_price:
        return
    if cnt == 3:
        total_price = min(total_price, price)
    else:
        for r in range(1, N - 1):
            for c in range(1, N - 1):
                if check(r, c):
                    p = 0
                    for i in range(5):
                        visited[r + dr[i]][c + dc[i]] = True
                        p += garden[r + dr[i]][c + dc[i]]
                    flower(cnt + 1, price + p)
                    for i in range(5):
                        visited[r + dr[i]][c + dc[i]] = False


N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

total_price = 20000
visited = [[False for _ in range(N)] for _ in range(N)]
flower(0, 0)
print(total_price)