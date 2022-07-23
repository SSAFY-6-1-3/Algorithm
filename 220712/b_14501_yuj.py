N = int(input())
result = [0] * (N+2)
ans = 0
for i in range(N):
    T, P = map(int, input().split())
    ans = max(ans, result[i+1])
    result[i+1] = ans
    if i+1 + T in range(N+2):
        result[i+1 + T] = max(result[i+1 + T], result[i+1]+P)

print(max(result))
