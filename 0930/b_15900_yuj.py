import sys
sys.stdin=open('input.txt')

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

stack = [1]
checked = []
node =[0] * (N+1)
result = 0
cnt = 0
while stack:

    idx = stack.pop()
    checked.append(idx)

    if idx != 1 and len(tree[idx]) == 1:
        result += node[idx]
        continue

    cnt += 1
    for t in tree[idx]:
        if t not in checked:
            node[t] = cnt
            stack.append(t)


if result % 2:
    print('yes')
else:
    print('No')