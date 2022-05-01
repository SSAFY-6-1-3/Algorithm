
N = int(input())
x = 64
cnt = 0

while N:
    if N-x >=0:
        cnt += 1
        N -= x
    else:
        x//=2

print(cnt)

