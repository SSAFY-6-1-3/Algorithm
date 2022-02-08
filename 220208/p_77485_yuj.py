def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt
            cnt += 1

    def moveX(r, c, l, prev, k):
        minv = rows * columns
        cnt = 0
        while cnt < l:
            minv = min(minv, prev)
            next = matrix[r][c + k]
            matrix[r][c + k] = prev
            prev = next
            c += k
            cnt += 1
        return (prev, minv)

    def moveY(r, c, l, prev, k):
        minv = rows * columns
        cnt = 0
        while cnt < l:
            minv = min(minv, prev)
            next = matrix[r + k][c]
            matrix[r + k][c] = prev
            prev = next
            r += k
            cnt += 1
        return (prev, minv)

    for query in queries:
        s1, s2 = query[0] - 1, query[1] - 1
        e1, e2 = query[2] - 1, query[3] - 1

        dir, result = 0, rows * columns
        prev, next = matrix[s1][s2], matrix[s1][s2 + 1]
        i, j = s1, s2
        while dir < 4:
            if dir == 0:
                (temp, minv) = moveX(i, j, e2-s2, prev, 1)
                j = e2

            elif dir == 1:
                (temp, minv) = moveY(i, j, e1-s1, prev, 1)
                i = e1
            elif dir == 2:
                (temp, minv) = moveX(i, j, e2-s2, prev, -1)
                j = s2
            else:
                (temp, minv) = moveY(i, j, e1-s1, prev, -1)
                i = s1
            prev = temp
            dir += 1
            result = min(result, minv)
        answer.append(result)
    return answer