def same_area(r, c): # 수평, 수직으로만 이동하며 울타리 없이 연결되어 있으면 => 같은 영역
    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]

    sheep = 0  # 같은 영역 내의 양의 수
    wolf = 0   # 같은 영역 내의 늑대의 수
    if yard[r][c] == 'o': sheep = 1 # 현재 좌표가 양이면 1
    elif yard[r][c] == 'v': wolf = 1 # 현재 좌표가 늑대면 1
    yard[r][c] = '#' # 현재 좌표를 울타리로 바꿔서 다시 방문 하지 않도록 설정


    stack = [[r, c]]


    while stack:
        r_ , c_ = stack.pop()

        for i in range(4): # dr, dc 인덱스를 돌면서 영역을 체크하러 돌아다니기
            nr, nc = r_ + dr[i], c_ + dc[i]

            if 0 <= nr < R and 0 <= nc < C and yard[nr][nc] != '#': # 다음 좌표가 유효한 좌표이고(마당 내) 울타리가 아닌 경우
                stack.append([nr, nc])  # 다음에 방문해야하니까 stack에 넣기
                if yard[nr][nc] == 'o':
                    sheep += 1
                elif yard[nr][nc] == 'v':
                    wolf += 1
                yard[nr][nc] = '#'


    return sheep, wolf


R, C = map(int, input().split())          # 행, 열 수
yard = [list(input()) for _ in range(R)]  # 마당의 구조

sheep_count = 0  # 다음날 아침 살아남은 양의 수
wolf_count = 0   # 살아남은 늑대의 수

for j in range(R): # 행 우선으로 리스트 순회
    for k in range(C):
        if yard[j][k] != '#':  # 울타리가 아닌 경우,
            s, w = same_area(j, k)  # 해당 '영역' 안에 있는 양, 늑대 수 가져오기
            if s > w: # 만약 양의 수가 많다면 양만 살아남음
                sheep_count += s
            else:  # 그렇지 않다면 늑대가 양을 잡아먹음
                wolf_count += w

print(sheep_count, wolf_count)
