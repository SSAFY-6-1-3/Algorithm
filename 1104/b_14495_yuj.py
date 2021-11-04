import sys
sys.stdin=open('input.txt')

n = int(input())
if n > 3:
    seq = [0] * (n + 1)

    for i in range(1, 4):
        seq[i] = 1

    for idx in range(1, n):
        num = seq[idx]
        if 2 < idx < n:                # 3 < idx+1 < n+1
            seq[idx+1] += num
        if 0 < idx < n-2:              # 3 < idx+3 < n+2
            seq[idx+3] += num

    print(seq[n])
else:
    print(1)