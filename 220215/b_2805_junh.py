
def bin_search(l, r, t):
    global max_h
    if l>r: return
    m = (l+r)//2

    get = 0
    for tree in trees:
       get += max(tree-m, 0)
    # sum_ = sum([tree - m for tree in array if tree > m])
    if get >= t:
        bin_search(m+1, r, t)
        max_h = max(max_h, m)
    else:
        bin_search(l, m-1, t)

N, M = map(int, input().split())
trees = list(map(int, input().split()))
max_h = 0
bin_search(0, max(trees), M)
print(max_h)

