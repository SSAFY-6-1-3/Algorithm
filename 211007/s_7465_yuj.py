import sys
sys.stdin=open('input.txt')

def check(p):
    stack = [p]
    while stack:
        i = stack.pop()
        for j in range(1, N+1):
            if country[i][j] == 1:
                stack.append(j)
                people[j] = cnt                         # 그룹으로 묶어주기
                country[i][j] = 0
                country[j][i] = 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    country = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):                                  # 인물 관계도 생성
        x, y = map(int, input().split())
        country[x][y] = 1
        country[y][x] = 1

    people = [0] * (N+1)                                # 사람 = 인덱스에 맞춰서 자신의 그룹(cnt) 만들어주기
    cnt = 0
    for p in range(1, N+1):                             # 그룹지어지지 않은 사람들(값이 0인 사람들)만 그룹 찾아주기
        if not people[p]:
            cnt += 1
            people[p] = cnt                             # 해당 그룹 번호로 people 리스트에 값 넣기
            check(p)                                    # 그룹으로 묶을 연결된 사람들 찾기


    print('#{} {}'.format(tc, cnt))
