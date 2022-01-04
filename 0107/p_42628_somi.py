def solution(operations):
    q = []
    for operation in operations:
        a, b = operation.split()
        if a == 'I':
            q.append(int(b))
        elif a == 'D' and b == '1' and q:
            q.pop()
        elif a == 'D' and b == '-1' and q:
            q.pop(0)
        q.sort()

    if q:
        return [max(q), min(q)]
    else:
        return [0, 0]
