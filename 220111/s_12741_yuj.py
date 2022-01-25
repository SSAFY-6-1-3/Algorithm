import sys
sys.stdin=open('sample_input.txt')

T = int(input())
result = [0] * (T+1)
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    time = min(b, d) - max(a, c)
    if time > 0:
        result[tc] = time
    else:
        result[tc] = 0

for i in range(1, T+1):
    print('#{} {}'.format(i, result[i]))