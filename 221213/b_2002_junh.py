
N = int(input())
dg = [input() for _ in range(N)]
ys = [input() for _ in range(N)]

dic = {dg[i]:i for i in range(N)}

answer = 0
for i in range(N):
    prv = dic[ys[i]]
    for j in range(i+1, N):
        if dic[ys[j]] < prv:
            answer += 1
            break

print(answer)
