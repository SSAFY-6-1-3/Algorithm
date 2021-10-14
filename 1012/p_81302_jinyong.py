def solution(places):
    answer = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for place in places:

        p_index = []  # 응시자가 앉아있는 좌표를 담을 변수
        result = 1

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_index.append([i, j])

        if not p_index:  # 만약 응사자가 한 명도 없는 경우에는 1 반환
            answer.append(1)
            continue

        first_stop = False  # 3중 반복문이라서 stop 관련 변수가 2개....

        for p in p_index:  # 각 응시자의 좌표를 row, col 변수에 저장
            row, col = p

            for i in range(4):  # 해당 응시자 주변 상, 하, 좌, 우 4 방향을 살펴본다
                new_row = row + dr[i]
                new_col = col + dc[i]

                if new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 5:
                    continue

                if place[new_row][new_col] == 'P':  # 만약 4방향 중에 하나라도 다른 응시자가 있으면
                    first_stop = True  # 더 볼 필요 없이 0을 출력하면 된다
                    result = 0
                    break

                if place[new_row][new_col] == 'X':  # 만약 파티션이 있는 방향이라면 넘어간다
                    continue

                second_stop = False  # 현재 보고 있는 방향에 빈 테이블이 있는 경우에는 한 번 더 응시자가 위치했는지 봐야 한다

                for j in range(4):
                    over_row = new_row + dr[j]
                    over_col = new_col + dc[j]

                    if over_row == row and over_col == col:
                        continue

                    if over_row < 0 or over_row >= 5 or over_col < 0 or over_col >= 5:
                        continue

                    if place[over_row][over_col] == 'P':  # 빈 테이블을 기준으로 4 방향에 응시자가 앉아있으면
                        second_stop = True  # 0을 반환하고 반복문을 종료해도 된다
                        result = 0
                        break

                if second_stop:
                    break

            if first_stop:
                break

        answer.append(result)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
