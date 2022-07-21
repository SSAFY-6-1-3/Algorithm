N = int(input())
P = sorted(list(map(int, input().split())))
time = P[0]
for i in range(1, N):
    time += P[i]
    P[i] = time

print(sum(P))