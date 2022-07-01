


def solution(n, k, cmd):
    last_del = []
    table = ['O'] * n
    link = {i: [i-1, i+1] for i in range(n)}
    link[0][0], link[n-1][1] = None, None

    def move(d, m):
        nonlocal k
        for _ in range(int(m)):
            k = link[k][d]

    def delete():
        nonlocal k
        table[k] = 'X'
        l, r = link[k]
        # last_del.append(k)
        last_del.append((k, l, r))
        if r is None:
            k = link[k][0]
        else:
            k = link[k][1]

        if r is None:
            link[l][1] = None
        elif l is None:
            link[r][0] = None
        else:
            link[l][1] = r
            link[r][0] = l


    def Z():
        num, l, r = last_del.pop()
        # num = last_del.pop()
        # l, r = link[num]
        table[num] = 'O'

        if l is None:
            link[r][0] = num
        if r is None:
            link[l][1] = num
        else:
            link[r][0] = num
            link[l][1] = num


    for c in cmd:
        if c == 'C':
            delete()
        elif c == 'Z':
            Z()
        else:
            d, m = c.split()
            d = 1 if d == 'D' else 0
            move(d, m)

    return ''.join(table)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))



# def solution(n, k, cmd):
#     last_del = []
#     table = ['O'] * n
#
#     def move(k, d, m):
#         while m:
#             k += d
#             if table[k] == 'O':
#                 m -= 1
#         return k
#
#     def delete(org_k):
#         table[org_k] = 'X'
#         k = org_k
#         last_del.append(k)
#
#         while k < n-1:
#             k += 1
#             if table[k] == 'O':
#                 return k
#         while True:
#             org_k -= 1
#             if table[org_k] == 'O':
#                 return org_k
#
#     for c in cmd:
#         if c == 'C':
#             k = delete(k)
#         elif c == 'Z':
#             rest = last_del.pop()
#             table[rest] = 'O'
#         else:
#             d, m = c.split()
#             d = 1 if d=='D' else -1
#             m = int(m)
#             k = move(k, d, m)
#
#
#
#     return ''.join(table)