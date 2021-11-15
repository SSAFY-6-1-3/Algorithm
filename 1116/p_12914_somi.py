def solution(n):
    if n < 3: return n

    jump = [0] * (n + 1)

    jump[1] = 1
    jump[2] = 2
    for i in range(3, n + 1):
        jump[i] = (jump[i - 1] + jump[i - 2]) % 1234567
    return jump[n]


print(solution(1))