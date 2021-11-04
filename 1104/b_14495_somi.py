
n = int(input())
pibo = [0] * 118
pibo[1], pibo[2], pibo[3] = 1, 1, 1
for i in range(4, 117):
    pibo[i] = pibo[i-1] + pibo[i-3]

print(pibo[n])