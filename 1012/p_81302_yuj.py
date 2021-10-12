from collections import deque
def solution(places):
    answer = []

    for place in places:
        P_lst = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':              # 사람들 위치 찾기
                    P_lst.append([i, j])

        if P_lst:
            for P in P_lst:
                i, j = P
                if check(place, i, j) == 0:
                    answer.append(0)
                    break
            else:
                answer.append(1)
        else:
            answer.append(1)
    return answer

def check(place, x, y):
    que = deque([(x, y)])

    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1
    while que:
        i, j = que.popleft()
        if visited[i][j] < 3:                   # visited에 P에서부터의 거리 기록, 거리가 3이상일 때는 확인할 필요 x
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    if place[ni][nj] == 'O':
                        que.append((ni, nj))
                    elif place[ni][nj] == 'P':      # 거리 2 안에 사람 있는 순간 0 return하고 끝내기
                            return 0

    return 1