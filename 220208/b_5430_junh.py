def execute(p, n, li):
    cut = [0, 0]
    target = 0
    for a in p:
        if a == 'R':
            target += 1
        else:
            cut[target%2] += 1

    if sum(cut) > n:
        return 'error'

    li = li[cut[0]:n-cut[1]]
    if target%2:
        li = li[::-1]

    rtn = ','.join(map(str, li))
    return '[' + rtn + ']'



T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    st = input().lstrip('[').rstrip(']')
    if st:
        li = list(map(int, st.split(',')))
    else:
        li = []
    print(execute(p, n, li))
