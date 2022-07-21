# 나머지 분배 법칙
# (AxB)%C = ((A%C) *(B%C)) % C

A, B, C = map(int, input().split())
def cal(A, B):
    if B == 1:
        return A % C
    else:
        temp = cal(A, B//2)
        if B % 2:
            return (temp * temp * A) % C
        else:
            return (temp * temp) % C

print(cal(A, B))