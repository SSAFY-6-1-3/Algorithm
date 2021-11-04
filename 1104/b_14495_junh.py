n = int(input())

fibo = [1] * (n+1)

for i in range(4, n+1):
    fibo[i] = fibo[i-1] + fibo[i-3]

print(fibo[n])