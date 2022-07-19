import sys
from itertools import combinations


input = sys.stdin.readline
N, K = map(int, input().split())
words = [set(input().strip()) for _ in range(N)]

if K < 5:
    print(0)
    exit()
K -= 5
all_char = set()

for word in words:
    all_char.update(word)
for c in 'antic':
    all_char.remove(c)

if len(all_char) < K:   # K가 더 크면 밑에서 조합을 못 만드는 경우가 생김
    print(N)
    exit()

combis = list(combinations(all_char, K))
answer = 0
if not combis:  # 이거 없으면 combi가 0이어서 밑에가 안 돌아갈 수 있음
    combis = ['a']

for combi in combis:
    readable = 0
    combi = set(combi)
    for word in words:
        for chr in word:
            if chr not in combi and chr not in 'antic':
                break
        else:
            readable += 1
    answer = max(answer, readable)

print(answer)