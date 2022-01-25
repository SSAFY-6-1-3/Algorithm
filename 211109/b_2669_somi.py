graph = list([False] * 100 for _ in range(100))

count = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 사각형 좌표 visit 처리
    for x in range(x1, x2):
        for y in range(y1, y2):
            if not graph[x][y]:
                count += 1
                graph[x][y] = True

print(count)
