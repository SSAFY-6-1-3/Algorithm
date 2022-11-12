

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multi(a, b):
    tmp = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += a[i][k] * b[k][j]
            tmp[i][j] %= 1000

    return tmp


def square(arr, t):
    if t == 1:
        return arr
    tmp = square(arr, t//2)
    result = multi(tmp, tmp)
    if t % 2:
        result = multi(result, arr)
    return result

for i in range(N):
    for j in range(N):
        A[i][j] %= 1000
answer = square(A, B)
for line in answer:
    print(*line)