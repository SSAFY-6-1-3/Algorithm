N, M = map(int, input().split())
li = list(map(int, input().split()))
min_len = sum(li)

def binary(s, e):
    global min_len
    if s > e: return

    limit = (s + e) // 2
    if check(limit):
        min_len = min(min_len, limit)
        binary(s, limit-1)
    else:
        binary(limit+1, e)


def check(limit):
    num = 1
    tmp = 0

    for i in li:
        if i > limit:
            return False
        elif tmp + i <= limit:
            tmp += i
        elif num < M :
            num += 1
            tmp = i
        else:
            return False
    return True

binary(0, sum(li))
print(min_len)