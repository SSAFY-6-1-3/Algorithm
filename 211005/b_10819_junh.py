import sys
from collections import deque

input = sys.stdin.readline


def calc(N, li):
    li = deque(sorted(li))
    new_li = [0] * N

    for i in range(N//2):
        l, r = li.popleft(), li.pop()
        if i%2:
            l,r = r, l
        new_li[N//2-1-i] = l
        new_li[N//2+i] = r


    if N%2:
        mid = li.pop()
        new_li.pop()
        if abs(new_li[0]-mid) < abs(new_li[-1]-mid):
            new_li = new_li + [mid]
        else:
            new_li = [mid] + new_li

    n_sum = 0
    for i in range(1, N):
        n_sum += abs(new_li[i-1] - new_li[i])
    return n_sum

N = int(input())
li = list(map(int, input().split()))
print(calc(N, li))