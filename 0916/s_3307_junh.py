import sys

sys.stdin = open('s_3307_input.txt')


def sooyol(n, li):
    for i in range(n):
        for j in range(i, -1, -1): # i 이전의 모든 수
            if li[j] < li[i]: # j번째 수가 i번째보다 작고
                if length[j] + 1 > length[i]: # 그 j의 증가수열 길이가 i보다 같거나 크면
                    length[i] = length[j]+1 # 거기 1을 더한 값을 i의 길이로 저장
    return max(length)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    length = [1 for _ in range(N)]
    print('#{} {}'.format(tc, sooyol(N, li)))