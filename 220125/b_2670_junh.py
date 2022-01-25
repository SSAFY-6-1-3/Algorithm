import sys

input = sys.stdin.readline

N = int(input())
li = [float(input()) for _ in range(N)]

for i in range(1, N):
    li[i] = max(li[i], li[i-1]*li[i])

print('{0:.3f}'.format(max(li)))

print(round(3.1, 3))        #3.1
print('{0:.3f}'.format(3.1))#3.100
