
A, B, C = map(int, input().split())
dp = [A%C]
roop_start = 0
roop_len = 0

for _ in range(B):
    tmp = (dp[-1] * A) % C
    if tmp in dp:
        roop_start = dp.index(tmp)
        roop_len = len(dp) - roop_start
        break

    dp.append(tmp)

if not roop_len:
    roop_len = len(dp)

n = roop_start + ((B - roop_start) % roop_len)
print(dp[n])