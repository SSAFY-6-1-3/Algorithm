# 출력형식이 잘못되었습니다.

N = int(input())
n = 4 * N - 3
stars = list(['*' for _ in range(n)] for _ in range(n + 2))

r, c = 1, n  # 시작점
num = n - 1  # 빈칸으로 만들 개수
cnt = 0  # num 만큼 몇번 지웠는지
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌,하,우,상
d_index = 0

while num > 1:  # 마지막 num 은 항상 2
    if cnt == 2:
        cnt = 0
        num -= 2
    else:
        for _ in range(num):
            r += direction[d_index][0]
            c += direction[d_index][1]
            stars[r][c] = ' '
        cnt += 1
        d_index = (d_index + 1) % 4

if N == 1:
    print('*')
else:
    for i in range(n + 2):
        print(''.join(stars[i]))
'''
두번째에 엔터쳐져야함
'''
