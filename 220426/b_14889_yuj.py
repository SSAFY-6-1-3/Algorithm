from itertools import combinations

def cal(lst):
    result = 0
    for member in lst:
        for other in lst:
            result += matrix[member-1][other-1]
    return result

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
combs = []
ans = 100
total = [i for i in range(1, N+1)]
for c in combinations(total, N//2):
    combs.append(c)

for idx in range(len(combs)//2+1):
    comb = combs[idx]
    start = cal(list(comb))
    link = cal(list(set(total)-set(comb)))
    ans = min(ans, abs(start-link))
    if ans == 0:
        break

print(ans)
