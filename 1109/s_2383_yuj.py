import sys
sys.stdin=open('sample_input.txt')
from itertools import combinations
from collections import deque

# 계단 내려가기
def move(exit, idx):
    t = 0
    exit.sort(reverse=True)                   # 늦게 내려가는 사람들이 앞에 오도록 정렬 -> pop쓰기위해
    deq = deque([])                           # 계단에서 이동 중인 사람들
    wait = deque([])                          # 계단에서 대기 중인 사람들

    while True:
        t += 1

        while exit and exit[-1] == t:                           # 계단 입구에 도착한 사람 대기명단에 넣기
            waitperson = exit.pop()
            wait.append(waitperson)

        while deq and deq[0]+stairs[idx] == t:                    # 다 내려간 사람 내보내기
            deq.popleft()

        while wait and wait[0] < t and len(deq) < 3:
            wait.popleft()
            deq.append(t)

        if not deq and not exit and not wait:                     # 아무도 내려갈 사람이 없으면 return
            return t




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people, exit = [], []                               # 사람 위치, 출구 위치
    stairs = []                                         # 계단 수
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                if arr[r][c] == 1:
                    people.append([r, c])
                else:
                    exit.append([r, c])
                    stairs.append(arr[r][c])


    lst = [j for j in range(len(people))]               # 1번 계단에 올라갈 사람 조합으로 뽑기(인덱스)
    nums = []                                           # 나머지는 2번 계단에 올라갈 사람들 (인덱스)
    for i in range(len(people)+1):
        N = combinations(lst, i)                        # 1번 계단에 아무도 안 올라갈 경우. 모두 1번 계단으로 올라갈 경우
        nums += N
    print(nums)

    first_r, first_c = exit[0][0], exit[0][1]           # 계단 위치
    sec_r, sec_c = exit[1][0], exit[1][1]
    min_time = float('inf')

    for num in nums:
        exit1, exit2 = [], []                           # 1번 출구로부터의 사람들 거리, 2번 출구로부터 사람들 거리
        for idx in range(len(people)):
            r, c = people[idx][0], people[idx][1]
            if idx in num:
                exit1.append(abs(first_r-r)+abs(first_c-c))
            else:
                exit2.append(abs(sec_r-r)+abs(sec_c-c))

        max_time = max(move(exit1, 0), move(exit2, 1))
        min_time = min(min_time, max_time)


    print('#{} {}'.format(tc, min_time))

