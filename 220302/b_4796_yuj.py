ans = []
L, P, V = 1, 1, 1
while L > 0:
    L, P, V = map(int, input().split())
    if L:
        days = (V // P) * L
        r = V % P
        if r < L:               # 남아있는 일수가 L보다 작을 경우에는 남아있는 모든 날 이용 가능
            days += r
        else:                   # 아닐 경우, L이 최대 이용 날 수
            days += L
        ans.append(days)

for idx in range(len(ans)):
    print('Case {}: {}'.format(idx+1, ans[idx]))

