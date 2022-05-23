N = int(input())

now = 666
cnt = 1

while cnt < N:
    now += 1
    if '666' in str(now):
        cnt += 1

print(now)