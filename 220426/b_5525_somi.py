# 50점...

N = int(input())
M = int(input())
S = input()

P = 'IOI'
P += 'OI' * (N - 1)
cnt = 0
i = 0
while i <= M - len(P):
    if S[i : i + len(P)] == P:
        cnt += 1
        i += 2
    else:
        i += 1

print(cnt)