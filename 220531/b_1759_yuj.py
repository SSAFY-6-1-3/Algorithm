from itertools import combinations

L, C = map(int, input().split())
alphas = list(map(str, input().split()))
vowels = []
consonant = []
answers = []
for alpha in alphas:
    if alpha in ['a','e','i','o','u']:
        vowels.append(alpha)
    else:
        consonant.append(alpha)

for i in range(1, L-1):
    perms_v = list(combinations(vowels, i))
    perms_c = list(combinations(consonant, L-i))
    for v in perms_v:
        for c in perms_c:
            lst = list(v + c)
            answers.append(''.join(sorted(lst)))
for answer in sorted(answers):
    print(answer)