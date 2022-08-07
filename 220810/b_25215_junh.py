st = input()
dp_up = [6001] * len(st)
dp_down = [6001] * len(st)
dp_up[0] = 2
dp_down[0] = 1 + st[0].isupper()

for i in range(1, len(st)):
    dp_up[i] = min(dp_up[i-1] + (st[i].islower()), dp_down[i-1] + 1) + 1
    dp_down[i] = min(dp_down[i-1] + (st[i].isupper()), dp_up[i-1] + 1) + 1

print(min(dp_up[-1], dp_down[-1]))