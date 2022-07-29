def permutations(m, k, num):  # m 개 중 / k 번째 선택 / num 현재까지 수
    if k == m:
        print(*num)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            permutations(m, k + 1, num + [numbers[i]])
            visited[i] = False


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
permutations(M, 0, [])

