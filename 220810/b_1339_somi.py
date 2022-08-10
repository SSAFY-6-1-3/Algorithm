N = int(input())
alphas = dict()
for _ in range(N):
    word = input()
    tmp = len(word)
    for i in range(tmp):
        if word[i] not in alphas:
            alphas[word[i]] = 10 ** (tmp - i - 1)
        else:
            alphas[word[i]] += 10 ** (tmp - i - 1)

alphas_sort = sorted(alphas.values(), reverse=True)
num = 9
ans = 0
for char in alphas_sort:
    ans += char * num
    num -= 1
print(ans)
