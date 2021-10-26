import sys

sys.stdin = open('s_5688.txt')

def bin_search(l, r, t):
    if l>r : return -1
    mid = (l+r)//2
    szg = mid**3
    if szg == t:
        return mid
    elif szg > t:
        return bin_search(l, mid-1, t)
    else:
        return bin_search(mid+1, r, t)


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, bin_search(1, N, N)))