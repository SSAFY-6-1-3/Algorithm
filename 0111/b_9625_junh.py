def push(N):
    a, b = 1, 0
    for _ in range(N):
        a, b = b, a+b
    return a, b


N = int(input())
print(*push(N))
