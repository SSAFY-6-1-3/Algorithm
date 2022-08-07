
N = int(input())
alphas = {}
for _ in range(N):
    word = input()
    for i in range(len(word)):
        alp = word[-i -1]
        alphas[alp] = alphas.get(alp, 0) + 10 ** i

li = sorted(alphas.values(), reverse=True)
answer = 0
for i in range(len(li)):
    answer += li[i] * (9-i)

print(answer)