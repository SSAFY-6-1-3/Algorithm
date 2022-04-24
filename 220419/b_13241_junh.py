A, B = map(int, input().split())

def ys(a, b):
    n = 2
    yss = [1]
    lim = int(max(a, b)**0.5) +1
    while n < lim:
        used = False
        if not a%n:
            a //= n
            used = True
        if not b%n:
            b //= n
            used = True
        if used:
            yss.append(n)
        else:
            n += 1
    yss.extend([a, b])
    ans = 1
    for i in yss:
        ans *= i
    return ans

print(ys(A, B))