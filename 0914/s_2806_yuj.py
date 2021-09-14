import sys
sys.stdin = open('input.txt')

def check(i, j):
        for arr_i, arr_j in arr:
            # 대각선인지 같은 열인지 검사
            if arr_j == j or (abs(arr_i - i) == abs(arr_j - j)):
                return 0
        return 1

def queen(i):
    global cnt
    global arr

    if i == N:
        if len(arr) == N:
            cnt += 1
            return

    for j in range(N):
        if check(i, j):
            # 조건에 맞으면 arr에 넣어주고 다음 행으로
            arr.append([i, j])
            queen(i+1)
            # return 됐을 때 없어지게
            arr.pop()
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = []
    queen(0)
    print('#{} {}'.format(tc, cnt))