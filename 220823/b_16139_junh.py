import sys

input = sys.stdin.readline
S = input()
q = int(input())
S_set = set(S)
li = [[0 for _ in range(len(S))] for _ in range(26)]

for i in range(26):
    c = chr(ord('a') + i)
    if c not in S_set:
        continue
    li[i][0] = int(c == S[0])
    for j in range(1, len(S)):
        li[i][j] = li[i][j-1] + (c == S[j])

answer = ""
for _ in range(q):
    a, l, r = input().split()
    a = ord(a) - ord('a')
    l, r = map(int, (l, r))

    if not l:
        answer += str(li[a][r]) + '\n'
    else:
        answer += str(li[a][r] - li[a][l-1]) + '\n'

print(answer)

