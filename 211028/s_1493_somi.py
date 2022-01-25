import sys
sys.stdin = open('s_1493.txt')


def write_number():  # 그래프에 숫자 적기...
    number = 1
    for i in range(1, 301):
        graph[1][i] = number
        number += 1
        r, c = 1, i
        while c > 1:
            r += 1
            c -= 1
            graph[r][c] = number
            number += 1

    for j in range(2, 301):
        graph[j][300] = number
        number += 1
        r, c = j, 300
        while r < 300:
            r += 1
            c -= 1
            graph[r][c] = number
            number += 1


graph = list([0] * 301 for _ in range(301))
write_number()


T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    x, y, z, w = 0, 0, 0, 0  # p와 q 가 적힌 인덱스 값 찾기
    for r in range(1, 301):
        if p in graph[r]:
            x = r
            for c in range(1, 301):
                if graph[r][c] == p:
                    y = c
        if q in graph[r]:
            z = r
            for c in range(1, 301):
                if graph[r][c] == q:
                    w = c

    new_x = x + z
    new_y = y + w
    print('#{} {}'.format(tc, graph[new_x][new_y]))


