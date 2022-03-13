import sys
input = sys.stdin.readline


L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()

if n in S :
    print(0)
    exit()

if S[0] < n:
    a = min(S, key=lambda x: abs(n-x) if x<n else 1001)
    b = min(S, key=lambda x: abs(x-n) if x>n else 1001)
else:
    a = 0
    b = S[0]

cnt = 0
for i in range(a+1, n+1):
    for j in range(n, b):
        if i<j :
            cnt +=1

print(cnt)