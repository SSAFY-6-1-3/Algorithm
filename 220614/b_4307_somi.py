# pypy로 통과

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())

    min_ant = 0
    max_ant = 0
    for _ in range(n):
        ant = int(input())
        short = min(ant, l - ant)  # 왼쪽, 오른쪽 중 최소
        long = max(ant, l - ant)   # 최대

        min_ant = max(min_ant, short)
        max_ant = max(max_ant, long)

    print(min_ant, max_ant)
