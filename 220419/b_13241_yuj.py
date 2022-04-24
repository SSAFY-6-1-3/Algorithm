A, B = map(int, input().split())

maxv = max(A, B)
minv = min(A, B)
k = 1
ans = 1
while True:
    ans = maxv * k
    if not ans % minv:
        break
    k += 1

print(ans)