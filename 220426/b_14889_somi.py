def calGap(arr1, arr2):
    global gap
    team1 = 0
    team2 = 0
    for i in range(size - 1):
        for j in range(i, size):
            team1 += score[arr1[i]][arr1[j]]
            team1 += score[arr1[j]][arr1[i]]

            team2 += score[arr2[i]][arr2[j]]
            team2 += score[arr2[j]][arr2[i]]

    tmp_gap = abs(team1 - team2)
    gap = min(gap, tmp_gap)

def makeTeam(n, r, start):
    if r == n:  # 다 뽑은 경우,
        link = []  # 다른 팀 리스트
        for i in range(N):
            if not visited[i]: # 1팀이 아닌 사람들 모임
                link.append(i)
        calGap(start, link)  # 갭 계산
        return
    for i in range(start, N):
        if not visited[i]:
            start[r] = i
            visited[i] = True
            makeTeam(n, r + 1, i + 1)
            visited[i] = False
            start[r] = 0


N = int(input())
score = list(list(map(int, input().split())) for _ in range(N))

size = N // 2  # 1팀 당 인원수
gap = sum(map(sum, score))  # 최대 gap은 총합

start = [0] * size  # 조합
visited = [False] * N
visited[0] = True  # 0번 사람이 들어간 팀을 1팀

makeTeam(size, 1, 1)  # 필요한 인원, 현재까지 뽑은 인원, 시작 인덱스
print(gap)

