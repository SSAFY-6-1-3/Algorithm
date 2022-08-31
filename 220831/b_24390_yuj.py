M, S = map(int, input().split(':'))
total = 60 * M + S
ans = 1
if total >= 600:
    ten, ten_d = divmod(total, 600)
    ans += ten
    total = ten_d

if total >= 60:
    minute, minute_d = divmod(total, 60)
    ans += minute
    total = minute_d

if total >= 30:
    ans -= 1
    sec, sec_d = divmod(total, 30)
    ans += sec
    total = sec_d

if total >= 10:
    tensec, tensec_d = divmod(total, 10)
    ans += tensec

print(ans)