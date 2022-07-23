n, m = map(int, input().split())
num = min(n-m, m)
first, second = 1, 1
cnt = 0
while cnt != num:
    first *= (n-cnt)
    second *= (cnt+1)
    cnt += 1
print(first//second)