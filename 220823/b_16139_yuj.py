# pypy로 통과
import sys
input = sys.stdin.readline
s = str(input().strip())
q = int(input())
alpha = [[0] * 26 for _ in range(len(s))]
alpha[0][ord(s[0])-97] = 1
for idx in range(1, len(s)):
    num = ord(s[idx])-97
    alpha[idx][num] = 1
    for j in range(26):
        alpha[idx][j] += alpha[idx-1][j]

for _ in range(q):
    word, l, r = map(str, input().split())
    askii = ord(word) - 97
    if l == '0':
        print(alpha[int(r)][askii])
    else:
        print(alpha[int(r)][askii] - alpha[int(l)-1][askii])