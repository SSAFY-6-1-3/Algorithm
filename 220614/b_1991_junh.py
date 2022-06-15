import sys

def to_num(st):
    if st == '.': return 0

    return ord(st)-ord('A')+1

def to_chr(n):
    return chr(ord('A') + n - 1)


input = sys.stdin.readline
N = int(input())
tree = [None] * (N + 1)

for _ in range(N):
    p, l, r = map(to_num, input().split())
    tree[p] = (l, r)

def pre(node):
    l, r = tree[node]
    result = to_chr(node)
    if l:
        result += pre(l)
    if r:
        result += pre(r)
    return result

def inor(node):
    l, r = tree[node]
    result = ''

    if l:
        result += inor(l)
    result += to_chr(node)
    if r:
        result += inor(r)

    return result

def post(node):
    l, r = tree[node]
    result = ''

    if l:
        result += post(l)
    if r:
        result += post(r)
    result += to_chr(node)

    return result


print(pre(1))
print(inor(1))
print(post(1))

