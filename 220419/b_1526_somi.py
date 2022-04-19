# Sol1. 이게 더 빠름

def minsu(num):
    global ans

    if num > N:
        return

    elif num > ans:
        ans = num

    for n in like:
        num = num * 10 + n
        minsu(num)
        num = (num - n) // 10


N = int(input())
ans = 4            # 답은 최소 4
like = [4, 7]  # 은민이가 좋아하는 숫자

for i in like:
    minsu(i)

print(ans)


# Sol2.
def is_minsu(number):
    while number:
        d, m = divmod(number, 10)

        if m == 4 or m == 7:
            number = d

        else:
            return False
    return True

N = int(input())
for i in range(N, 3, -1):
    if is_minsu(i):
        print(i)
        break
