import sys
input = sys.stdin.readline

def make_tree(tree):    # [값, 부모, l, r]
    idx = 0
    while True:
        try :
            n = int(input().strip('\n'))
        except ValueError:
            return tree

        par = tree[idx][1]

        while idx and (((tree[par][0] < n) and par) or tree[idx][2] * tree[idx][3]):
            idx = par
            par = tree[idx][1]

        if tree[idx][0] > n:
            tree.append([n, idx, 0, 0])
            tree[idx][2] = len(tree)-1
            idx = len(tree)-1

        elif not tree[idx][3]:
            tree.append([n, idx, 0, 0])
            tree[idx][3] = len(tree)-1
            idx = len(tree)-1


def huwi(idx, tree):
    l = tree[idx][2]
    r = tree[idx][3]
    if l:
        huwi(l, tree)
    if r:
        huwi(r, tree)
    print(tree[idx][0])

try:
    start = int(input().strip('\n'))
except EOFError:
    exit()
tree = [[start, 0, 0, 0]]
make_tree(tree)
huwi(0, tree)