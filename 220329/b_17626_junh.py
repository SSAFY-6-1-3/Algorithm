
n = int(input())
sqrs = []
answer = n

i=0
while i**2<=n:
    sqrs.append(i**2)
    i+=1

def comb(used, n_sum):
    global answer
    if n_sum > n:
        return
    if n_sum == n:
        answer = min(answer, len(used))
    if used:
        start = used[-1]
    else:
        start = len(sqrs)-1

    if len(used)<min(answer-1, 4):
        for i in range(start, -1, -1):
            comb(used+[i], n_sum+sqrs[i])

comb([], 0)
print(answer)