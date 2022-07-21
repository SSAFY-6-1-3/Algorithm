N = int(input())
temp = 666
while True:
    if '666' in str(temp):
        N -= 1
        if N == 0:
            break
    temp += 1
print(temp)
