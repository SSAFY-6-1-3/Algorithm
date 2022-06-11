def solution(n, computers):
    answer = 0

    p = [i for i in range(n)]

    def find(c):
        while p[c] != c:
            c = p[c]
        return c

    def union(a, b):
        if find(a) <= find(b):
            p[b] = find(a)
        else:
            p[a] = find(b)

    for _ in range(2):
        for a in range(n):
            for b in range(n):
                if computers[a][b]:
                    union(a, b)

    return len(set(p))



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))