def cal(n):
    if n == 1:
        return A % C
    else:
        num = cal(n//2)
        if n % 2:
            print(n, num)
            return (num * num * A) % C
        else:
            print(n, num)
            return (num * num) % C

A, B, C = map(int, input().split())

print(cal(B))
