# 출력초과???!!!!

T = int(input())
for _ in range(T):
    p = input()
    p = p.replace("RR", "")

    n = int(input())
    numbers = input()[1: -1].split(',')

    r = 0
    start = 0
    end = len(numbers)

    for func in p:
        if func == "R":
            r += 1
        else:
            if r % 2:
                end -= 1

            else:
                start += 1

    if start < end:
        numbers = numbers[start:end]
        if r % 2:
            numbers.reverse()
        print(str(numbers).replace(' ', ''))
    elif start == end:
        print('[]')
    else:
        print('error')



