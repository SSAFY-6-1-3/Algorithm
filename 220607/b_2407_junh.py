n, m = map(int, input().split())

bunja = 1
bunmo = 1
for i in range(m):
    bunja *= n - i
    bunmo *= i+1

print(bunja//bunmo)