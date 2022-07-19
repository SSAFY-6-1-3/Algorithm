from collections import deque


def solution(n, weak, dist):
    dist.sort(reverse=True)

    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))

    for i in range(len(dist)):
        d = dist[i]

        for _ in range(len(q)): # 새로 q에 추가된 것들은 다음 dist로 넘어가서만 사용하기 위해 while을 쓰지 않음
            current = q.popleft()
            for start in current:
                end = (start + d) % n

                if start < end:
                    tmp = tuple(filter(lambda x: x < start or x > end, current))
                else:
                    tmp = tuple(filter(lambda x: x < start and x > end, current))

                if not tmp:
                    return i+1

                if tmp not in visited:
                    visited.add(tmp)
                    q.append(list(tmp))

    return -1



print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))