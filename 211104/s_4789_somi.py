import sys
sys.stdin = open('s_4789.txt')
T = int(input())
for tc in range(1, T + 1):
    clap = list(map(int, input()))
    hire = 0
    now_clap = 0
    for i in range(len(clap)):
        if clap[i] != 0:  # 0명일때는 넘어가기
            if now_clap >= i:
                now_clap += clap[i]
            else:
                hire += (i - now_clap)
                now_clap += (i - now_clap + clap[i])
    print('#{} {}'.format(tc, hire))