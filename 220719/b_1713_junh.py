N = int(input())
M = int(input())
li = list(map(int, input().split()))
posted = []
recom = {}

def pop_one():
    to_pop = None
    for i in range(N):
        num = posted[i]
        if to_pop is None or recom[num] < recom[posted[to_pop]]:
            to_pop = i

    num = posted.pop(to_pop)
    recom[num] = 0


for n in li:
    recom[n] = recom.get(n, 0) + 1

    if n not in posted :
        if len(posted) >= N:
            pop_one()
        posted.append(n)


print(*sorted(posted))