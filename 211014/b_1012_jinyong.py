def solution(locations):

    answer = 0

    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [0] * K  # i 번 배추를 봤는지 보기 위한 방문체크용 리스트

    for i in range(K):  # i 개의 배추들을 한 번씩 탐색
        if visited[i]:
            continue

        queue = [[] for _ in range(K)]  # 인접한 곳에 배추가 있는지 확인할 배추들을 담을 큐
        head = 0
        rear = 1
        queue[0] = locations[i]  # i 번째 배추부터 시작!!
        visited[i] = 1  # i 번째 배추에 방문체크
        answer += 1  # i 번째 배추부터 인접한 곳을 찾으니까 지렁이가 일단 한 마리 더 필요

        while head < rear:

            row, col = queue[head]
            head += 1

            for d in range(4):  # 현재 배추를 기준으로 인접한 4 방향에 다른 배추가 있는지 확인
                new_row = row + dr[d]
                new_col = col + dc[d]

                new_p = [new_row, new_col]

                for j in range(K):  # 다른 배추들을 다 보면서 해당 좌표에 배추가 존재하는지 탐색
                    if locations[j] == new_p and not visited[j]:  # 현재 위치에 배추가 있고, 한 번도 방문한 적 없는 배추인 경우
                        visited[j] = 1  # 인접한 배추이므로 방문체크(지렁이 필요 X)
                        queue[rear] = new_p  # 그 배추 주변도 살펴봐야 하니까 큐에 추가
                        rear += 1
                        break

    return answer


T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    locations = [list(map(int, input().split())) for _ in range(K)]
    print(solution(locations))
