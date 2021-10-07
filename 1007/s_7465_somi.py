import sys
sys.stdin = open('s_7465.txt')

def find_group(i, friends):  # 그룹 하나 찾기
    stack = []
    stack.extend(friends)  # stack에 i번째 사람이 아는 사람의 인덱스 저장
    visited[i] = 1  # i번째 사람 방문 처리

    while stack:
        friend = stack.pop()  # 지인들에 대해서
        if not visited[friend]: # 아직 방문 안했다면
            visited[friend] = 1  # 방문 처리
            stack.extend(connection[friend])  # stack에 그 사람의 지인을 저장


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]  # 입력값을 리스트에 담아두기
    connection = [[] for _ in range(N + 1)]  # 인덱스 번호가 사람 숫자, 해당 인덱스에 아는 사람 인덱스 저장
    for person in arr:
        connection[person[0]].append(person[1])
        connection[person[1]].append(person[0])
    # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

    visited = [0] * (N + 1)  # 방문 처리를 위함
    group = 0  # 그룹 숫자 세기
    for i in range(1, N+1):  # 1번부터 N번 사람까지
        if not visited[i]:   # 아직 방문 안했다면(아직 그룹으로 묶이지 않았다면)
            if len(connection[i]) == 0: # 아는 사람이 없는 경우
                group += 1              # 그 자체로 그룹

            else:
                find_group(i, connection[i])
                group += 1


    print('#{} {}'.format(tc, group))