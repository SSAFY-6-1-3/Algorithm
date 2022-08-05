
st = input()
dp = [1] * len(st)
print(dp)

for i in range(1, len(st)):
    dp[i] = dp[i-1] + 1
    if st[i].isupper() != st[i-1].isupper():
        if st[i-1].isupper() == st[i-2].isupper():
