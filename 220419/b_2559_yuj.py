N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans, temp = sum(lst[:K]), sum(lst[:K])

for i in range(N-K):
    temp -= lst[i]
    temp += lst[i+K]
    ans = max(temp, ans)

print(ans)