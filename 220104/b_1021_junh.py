N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))

def q_pop(num):
    global q

    idx = q.index(num)

    if idx <= len(q)//2:
        move = idx
    else:
        move = len(q) - idx

    if idx+1 < len(q):
        q = q[idx + 1:] + q[:idx]
    else:
        q.pop()

    return move



q = [i for i in range(1, N+1)]
answer = 0

for num in li:
    answer += q_pop(num)

print(answer)
