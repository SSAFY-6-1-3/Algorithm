import sys
sys.stdin = open('input.txt')


def worm_virus(start):
    que = [start]  # 시작할 컴퓨터 번호 큐에 넣어놓기

    visited = [0] * (N + 1)  # visited 생성
    visited[start] = 1       # 시작점은 방문 표시시

    virus = 0  # 감염된 컴퓨터 개수 세기

    while que:  # 아직 확인할 컴퓨터 번호 남아있는 경우
        worm = que.pop(0)   # 컴퓨터 번호 큐에서 pop해서 꺼내기
        for i in range(len(arr)):
            if arr[worm][i] == 1 and not visited[i]:  # 바이러스 걸린 컴퓨터와 연결되어있고, 방문 아직 안한 컴퓨터
                virus += 1
                que.append(i)   # 큐에 넣어주기
                visited[i] = 1  # 방문 했음 표시
    return virus

N = int(input())
roads = int(input())

arr = [[0] * (N + 1) for _ in range(N + 1)]  # 인접한 컴퓨터는 1로 표시할 예정

for _ in range(roads):
    c1, c2 = map(int, input().split())       # 방향성이 없음!!
    arr[c1][c2] = 1
    arr[c2][c1] = 1

print(worm_virus(1))


