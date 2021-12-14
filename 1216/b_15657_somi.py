def permutation(n, m, k):
    if k == m:
        print(*p)
    else:
        for i in range(n):
            if k == 0 or p[k - 1] <= numbers[i]:  # 오름차순!!
                p[k] = numbers[i]
                permutation(n, m, k + 1)

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
p = [0] * M
permutation(N, M, 0)

