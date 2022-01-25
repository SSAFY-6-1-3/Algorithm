def hanoi_tower(n, a, b, c):
    if n == 1:
        print(a, c)

    else:
        hanoi_tower(n-1, a, c, b)
        print(a, c)
        hanoi_tower(n-1, b, a, c)

N = int(input())
print(2**N -1)
hanoi_tower(N, 1, 2, 3)

