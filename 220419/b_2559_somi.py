N, K = map(int, input().split())
temps = list(map(int, input().split()))  # 측정 온도

sum_temp = sum(temps[:K])  # 연속 K일 온도 합
ans = sum_temp
i = 1  # K 시작 일
while i <= N - K:
    sum_temp = sum_temp - temps[i - 1] + temps[i + K - 1]
    ans = max(ans, sum_temp)
    i += 1

print(ans)