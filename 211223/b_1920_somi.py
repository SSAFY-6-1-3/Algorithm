import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))


for i in range(M):
    if X[i] in A:
        print(1)
    else:
        print(0)