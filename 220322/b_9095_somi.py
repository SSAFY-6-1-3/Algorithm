number = [0, 1, 2, 4] + [0] * 8

for i in range(4, 12):
    number[i] = number[i-1] + number[i-2] + number[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(number[n])
