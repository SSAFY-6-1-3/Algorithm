import sys

input = sys.stdin.readline
print = sys.stdout.write
S = input()
q = int(input())
li = [[0 for _ in range(26)] for _ in range(len(S)+1)]

for i in range(1, len(S)+1):
    c = ord(S[i-1]) - ord('a')
    for j in range(26):
        li[i][j] = li[i-1][j] + (j==c)

for _ in range(q):
    a, l, r = input().split()
    a = ord(a) - ord('a')
    l, r = map(int, (l, r))

    print(str(li[r+1][a] - li[l][a]) + '\n')


