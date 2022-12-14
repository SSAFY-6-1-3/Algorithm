# 미완성
N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

def merge_sort(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, r, q)


def merge(A, p, r, q):
    global cnt
    tmp = []
    i, j = p, q + 1
    while i < q+1 and j < r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i < q+1:
        tmp.append(A[i])
        i += 1
    while j < r:
        tmp.append(A[j])
        j += 1

    if cnt + len(tmp) >= K:
        print(tmp, K, cnt)
        print(tmp[K - cnt - 1])
        exit()
    else:
        cnt += len(tmp)
        A = A[:p] + tmp + A[r+1:]


merge_sort(A, 0, N)
print(-1)