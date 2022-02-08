def solution(rows, columns, queries):
    arr = list(list(range(columns * i + 1, (columns * i) + columns + 1)) for i in range(rows))
    answer = []
    for query in queries:
        r1, c1, r2, c2 = map(lambda x: x - 1, query)

        rt = arr[r1][c2]
        rb = arr[r2][c2]
        lb = arr[r2][c1]
        ans = min(rt, rb, lb)

        # 윗줄
        for c in range(c2, c1, -1):
            arr[r1][c] = arr[r1][c - 1]
            ans = min(ans, arr[r1][c])

        # 오른쪽
        for r in range(r2, r1 + 1, - 1):
            arr[r][c2] = arr[r - 1][c2]
            ans = min(ans, arr[r][c2])

        # 아랫줄
        for c in range(c1, c2):
            arr[r2][c] = arr[r2][c + 1]
            ans = min(ans, arr[r2][c])

        # 왼쪽
        for r in range(r1, r2 - 1):
            arr[r][c1] = arr[r + 1][c1]
            ans = min(ans, arr[r][c1])

        arr[r1 + 1][c2] = rt
        arr[r2][c2 - 1] = rb
        arr[r2 - 1][c1] = lb
        answer.append(ans)

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))