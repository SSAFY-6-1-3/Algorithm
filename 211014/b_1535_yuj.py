import sys
sys.stdin=open('input.txt')

def hello(sj_p, sj_j, i):
    global maxj

    if sj_p <= 0:
        return

    if sj_j > maxj:                                         # 기쁨은 계속 증가하므로 제일 크면 바로 최댓값 바꿔주기
            maxj = sj_j

    for idx in range(i, N):                                 # 다음에 확인할 사람 키워드 인자로 넘겨주기(visited 필요 x)
        hello(sj_p - power[idx], sj_j + joy[idx], idx+1)    # i 안 넘겨주면 시간 초과,,


N = int(input())
power = list(map(int, input().split()))
joy = list(map(int, input().split()))
maxj = 0
hello(100, 0, 0)                                            # 현재 파워, 현재 기쁨, 앞으로 인사 시작할 사람
print(maxj)