def check_color(start_r, start_c, size):  # 모두 같은 색인 지 확인 하는 함수
    flag = False
    count = 0  # 파란 색 세기
    color = paper[start_r][start_c]  # 가장 첫번 째 색을 기준으로 삼기
    for i in range(start_r, start_r + size):
        for j in range(start_c, start_c + size):
            if paper[i][j]:  # 파란색이면
                count += 1   # count

    if count == 0:  # 파란색이 1도 없고 모두 하얀색
        flag = True
    elif count == size ** 2:  # 모든 칸이 파란색이라면
        flag = True

    return flag, color


def make_paper(start_r, start_c, size):
    global white, blue
    flag, color = check_color(start_r, start_c, size)
    
    if flag:  # 만약 칸 안에 있는 색이 모두 같은 색이라면
        if color:  # 1 이면 파란색 추가
            blue += 1
        else:      # 0이면 하얀색 추가
            white += 1

    else:  # 만약 다른색이 있다면, 현재 사이즈에서 반으로 쪼개기
        size = size // 2
        make_paper(start_r, start_c, size)         # 좌상
        make_paper(start_r + size, start_c, size)  # 우상
        make_paper(start_r, start_c + size, size)  # 좌하
        make_paper(start_r + size, start_c + size, size)  # 우하

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
make_paper(0, 0, N)

print(white)
print(blue)