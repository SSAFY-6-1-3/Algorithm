import math

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N

for s in students:
    tmp = s - B
    if tmp > 0:

        ans += math.ceil(tmp / C)

print(ans)
