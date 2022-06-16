P = [0 for _ in range(101)]
P[1], P[2], P[3] = 1, 1, 1

for i in range(1, 98):
    P[i + 3] = P[i] + P[i + 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N])
