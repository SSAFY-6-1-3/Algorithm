def solution(n):
    answer = []
    tri = [[0]*i for i in range(1, n+1)] # 탐색할 전체 삼각형
    drc = [(1, 0), (0, 1), (-1, -1)] # 아래, 오른쪽, 위로 움직이는 델타
    blanks = 0 # for문을 통해 총 칸의 갯수를 셌다.
    for i in range(n+1):
        blanks += i

    tri[0][0] = 1 # 시작 칸을 1로 채워줌
    cnt = 1 # 첫째 칸은 이미 적어놨으니 cnt는 1에서 시작
    y, x = 0, 0 # 시작하는 y, x값
    drc_val = 0 # 처음에는 아래로 움직인다.

    while cnt < blanks: # length(칸 갯수)
        cnt += 1 # 숫자 1올리고
        while True: # 가능한 길을 찾을때까지 반복
            ny = y + drc[drc_val][0] # drc_val을 통해 움직일 다음 좌표 생성
            nx = x + drc[drc_val][1]
            if 0 <= ny < n and 0 <= nx <= ny and not tri[ny][nx]: # 새 좌표가 유효하고, 빈칸(0)이면,
                tri[ny][nx] = cnt # 그 좌표에 cnt를 적고
                y, x = ny, nx # y와 x를 그 좌표로 바꾸고 break
                break
            else: # 새 좌표가 유효하지 않으면 방향값을 바꾼다.
                drc_val = (drc_val+1)%3
                
    for li in tri: # 2차원 배열 tri를 1차원으로 바꾸기 위한 for문
        for n in li:
            answer.append(n)

    return answer

print(solution(5))