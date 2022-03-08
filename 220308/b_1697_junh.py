
N, K = map(int, input().split())
if N >= K:
    print(N-K)
    exit()
sec = 0
used = set()
able = {N}
while True:
    tmp = set()

    for n in able:
        if n ==K:
            print(sec)
            exit()
        if n-1 not in used and n-1>=0:
            tmp.add(n-1)
        if n+1 not in used and n+1<=100000:
            tmp.add(n+1)
        if 2*n not in used and 2<=2*n<=100000:
            tmp.add(2*n)

    sec += 1

    used.update(able)
    able = tmp




