
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()), reverse=True)
    votes = [0] * (N)
    i, j = 0, 0

    while i < N and j < M:
        if A[i] <= B[j]:
            votes[i] += 1
            j += 1
        else:
            i += 1

    print(f'#{t} {votes.index(max(votes)) + 1}')
