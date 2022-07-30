
N, M = map(int, input().split())
cnt, left = 0, 0
days = [int(input()) for _ in range(N)]
min_k = float('inf')

def check(K):
    pass

def bin(s, e):
    global min_k
    if e > s:
        return
    mid = (s+e) // 2

    if check(mid):
        min_k = mid
        bin(s, mid-1)
    else:
        bin(mid+1, e)