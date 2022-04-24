N = int(input())
ans = 0
for number in range(N, 3, -1):
    for num in str(number):
        if num == '4' or num == '7':
            pass
        else:
            break
    else:
        ans = number
        break

print(ans)