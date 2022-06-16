from itertools import combinations

L, C = map(int, input().split())
alphas = list(input().split())
vowels = [i for i in alphas if i in ['a', 'e', 'i', 'o', 'u']]
consts = list(set(alphas) - set(vowels))
result = []

for i in range(1, L - 1):  # 모음 뽑는 개수 i
    vowel_comb = list(combinations(vowels, i))
    const_comb = list(combinations(consts, L - i))  # 여기서 list 안바꾸고 for문 돌리면 안됨!!
                                                    # 두번째 for문 돌때는 빈 리스트만 남음
    if vowel_comb and const_comb:
        for vowel in vowel_comb:  # [(a,) (i,)] [a]
            for const in const_comb: # [(s, w)] [s, w]
                password = list(vowel) + list(const) #[a, s, w]
                password.sort()
                result.append(''.join(password)) #'asw'

result.sort()
for ans in result:
    print(ans)
