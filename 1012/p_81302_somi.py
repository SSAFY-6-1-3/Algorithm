
dr = [0, 1, 0, -1, -1, 1, -1, 1] # 우, 하, 좌, 상, 대각선
dc = [1, 0, -1, 0, 1, -1, -1, 1]

def is_distancing(place, r, c):
    for i in range(4):  # 우, 하, 좌, 상 -> 2개 더 가보고, P 있으면, 사이에 파티션 있는 지 확인
        for dist in range(1, 3):  # 2칸 더 가보기 위함
            nr, nc = r + dr[i] * dist, c + dc[i] * dist

            if 0 <= nr < 5 and 0 <= nc < 5:
                if place[nr][nc] == 'P' and place[r + dr[i]][c + dc[i]] != 'X':  # 사이에 X 없으면 False
                        return False


    for j in range(4, 8):  # 대각선 방향 -> 사이에 파티션 있는 지 확인
        nr, nc = r + dr[j], c + dc[j]
        if 0 <= nr < 5 and 0 <= nc < 5:
            if place[nr][nc] == 'P': # 대각선 방향에 사람 있으면
                if place[r][nc] != 'X' or place[nr][c] != 'X':  # 사이에 파티션 없으면 False
                    return False

    return True

def place_check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not is_distancing(place, i, j):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        if place_check(place):
            answer.append(1)
        else: answer.append(0)
    return answer

