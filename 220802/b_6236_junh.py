
N, M = map(int, input().split())
days = [int(input()) for _ in range(N)]
min_k = float('inf')

def check(K):
    cnt, left = 0, 0
    for i in range(N):
        need = days[i]
        if left >= need:
            continue
        elif need > K:
            return False
        else:
            left = K - need
            cnt += 1
            if cnt > M:
                return False
    return True

def bin(s, e):
    global min_k
    if e < s:
        return
    mid = (s+e) // 2

    if check(mid):
        min_k = mid
        bin(s, mid-1)
    else:
        bin(mid+1, e)

bin(0, max(days))
print(min_k)