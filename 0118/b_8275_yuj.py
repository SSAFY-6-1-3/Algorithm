import sys, copy
sys.stdin=open('sample_input.txt')

def comb(l, com):                   # 조합 구하기
    global answer

    if len(com) == l:
        answer.append(com)
        return

    for num in range(X, -1, -1):
        comb(l, com+[num])

T = int(input())
for tc in range(T):
    N, X, M = map(int, input().split())
    hamsters = [X] * N
    lst = [list(map(int, input().split())) for _ in range(M)]
    answer = []
    result = []
    maxV = 0
    for idx in range(M):                       # 경근이 기록(조건)에 없는 햄스터 우리는 최대값으로 설정, 있으면 0으로 설정
        hamsters[lst[idx][0]-1] = 0
        hamsters[lst[idx][1]-1] = 0

    comb(hamsters.count(0), [])                # 조건에 있는 우리 갯수로만 조합 구하기

    for ans in answer:
        if maxV > sum(ans) + sum(hamsters):    # 최대 마릿수 구해야하므로 가지치기
            continue

        temp = copy.deepcopy(hamsters)
        i = 0
        for idx in range(N):                   # 구한 조합대로 햄스터 우리에 햄스터 마릿수 설정
            if not temp[idx]:
                temp[idx] = ans[i]
                i += 1

        for ls in lst:                         # 조건에 맞는지 확인
            ham = 0
            for j in range(ls[0]-1, ls[1]):
                ham += temp[j]
            if ham != ls[2]:
                break
        else:
            maxV = sum(temp)
            result.append(temp)

    if result:
        result.sort()                          # 최댓값 중 사전순으로 가장 앞선 것부터 출력해야하므로
        print('#{}'.format(tc), end=' ')
        print(*result[0])
    else:
        print('#{} {}'.format(tc, -1))