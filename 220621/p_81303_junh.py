


def solution(n, k, cmd):
    last_del = []
    table = ['O'] * n

    def move(k, d, m):
        while m:
            k += d
            if table[k] == 'O':
                m -= 1
        return k

    def delete(org_k):
        table[org_k] = 'X'
        k = org_k
        last_del.append(k)

        while k < n-1:
            k += 1
            if table[k] == 'O':
                return k
        while True:
            org_k -= 1
            if table[org_k] == 'O':
                return org_k

    for c in cmd:
        if c == 'C':
            k = delete(k)
        elif c == 'Z':
            rest = last_del.pop()
            table[rest] = 'O'
        else:
            d, m = c.split()
            d = 1 if d=='D' else -1
            m = int(m)
            k = move(k, d, m)



    return ''.join(table)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))