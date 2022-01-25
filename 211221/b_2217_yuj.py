n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
maxV = 0
for i in range(n-1, -1, -1):
    k = n - i
    maxV = max(maxV, ropes[i]*k)

print(maxV)