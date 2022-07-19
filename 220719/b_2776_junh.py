T = int(input())

for _ in range(T):
    N = int(input())
    n_set = set(map(int, input().split()))
    M = int(input())
    m_li = list(map(int, input().split()))

    for m in m_li:
        if m in n_set:
            print(1)
        else:
            print(0)

