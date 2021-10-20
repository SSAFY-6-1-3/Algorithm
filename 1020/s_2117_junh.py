from collections import deque
import sys

sys.stdin = open('s_2117.txt')

size_dp = [0, 1]

def make_size_dp(k=2):
    size = size_dp[-1] + (k-1)*4
    if k <= N//2+1:
        size_dp.append(size)
        make_size_dp(k+1)


def isOK(size, M, mat):
    for i in range(N):
        for j in range(N):



def check(i, j, M, size):
    q = deque([(i, j, 1)])
    k=1
    while k < size:


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    make_size_dp()
    size = len(size_dp)-1
    check(N//2, N//2, 3, M, 0)
    print(*mat)
    # print(isOK(size, M, mat))