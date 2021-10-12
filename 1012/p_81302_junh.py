dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

def solution(places):
    answer = []

    def case(room):             # 하나의 케이스를 수행하는 함수
        for y in range(5):
            for x in range(5):
                if room[y][x] !='P': continue   #사람인 경우에만 검사하도록
                if not check(y, x, 0, y, x, room):  #   뒤의 y와 x는 시작지점을 검사하지 않도록 사용
                    answer.append(0)            #  false가 나오면 0찍고 리턴
                    return
        answer.append(1)

    def check(y, x, depth, oy, ox, room):
        if depth == 2: return True

        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if ny not in range(5) or nx not in range(5) or (oy == ny and ox == nx) or room[ny][nx]=='X':
                continue
            if room[ny][nx] == 'P' : return False
            if not check(ny, nx, depth+1, oy, ox, room):
                return False

        return True


    for i in range(5):  # 5개의 케이스를 검사
        case(places[i])
    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))