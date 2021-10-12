import sys

sys.stdin = open('s_5607.txt')

FACTOS = [0 for _ in range(1000001)]
FACTOS[0] = 1

def facto(num):
    if not FACTOS[num]:
        FACTOS[num] =  facto(num-1) * num %1234567891
    return FACTOS[num]


def comb(n, r):
    return int(facto(n)/facto(n-r)/facto(r)) % 1234567891



T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())
    print('#{} {}'.format(tc, comb(N, R)))