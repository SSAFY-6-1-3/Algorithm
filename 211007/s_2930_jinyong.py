import sys

sys.stdin = open('2930.txt')


def max_heap(lst, x):
    result = [0] + lst

    if x == 1:
        idx = len(lst)

        while result[idx] > result[idx // 2]:

            if idx == 1:
                break

            if result[idx] > result[idx // 2]:
                result[idx], result[idx // 2] = result[idx // 2], result[idx]
            idx //= 2

    else:
        idx = len(lst)

        while result[idx] > result[idx // 2]:

            if idx == 1:
                break

            if idx % 2:
                if result[idx - 1] < result[idx]:
                    result[idx - 1], result[idx] = result[idx], result[idx - 1]
                idx -= 1

            if result[idx] > result[idx // 2]:
                result[idx], result[idx // 2] = result[idx // 2], result[idx]

            idx //= 2

    return result[1:]


def solution(orders):
    heap = []
    result = []

    for order in orders:
        if order[0] == 2 and not heap:
            result.append(-1)

        elif order[0] == 2 and heap:
            result.append(heap.pop(0))
            heap = max_heap(heap, 2)

        else:
            heap.append(order[1])
            heap = max_heap(heap, 1)

    return result


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    orders = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case}', *solution(orders))
