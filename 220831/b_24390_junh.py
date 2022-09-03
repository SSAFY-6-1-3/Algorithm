M, S = map(int, input().split(':'))
time = 0
cnt = 1

if S >= 30:
    S -= 30

S = M * 60 + S
for a in (600, 60, 30, 10):
    tmp = S // a
    S -= tmp * a
    cnt += tmp
print(cnt)

