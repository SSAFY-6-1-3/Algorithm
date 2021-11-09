n = int(input())

hanoi = [0]*(n+1)
hanoi[1] = 1

for i in range(2, n+1):
    hanoi[i] = hanoi[i-1]*2 +1

print(hanoi[n])