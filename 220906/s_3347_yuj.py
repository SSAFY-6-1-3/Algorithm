T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    games = [0] + list(map(int, input().split()))
    result = [0] * (N+1)
    people = list(map(int, input().split()))
    for p in people:
        for idx in range(1, N+2):
            if games[idx] <= p:
                result[idx] += 1
                break

    ans = result.index(max(result))
    print(f'#{tc} {ans}')