from collections import deque

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*',0,'#']
]


def dist_bfs(target, left, right):
    q = deque([target])
    visited = [[999 for _ in range(3)] for _ in range(4)]
    visited[target[0]][target[1]] = 0
    while q:
        y, x = q.popleft()
        dist = visited[y][x]
        for d in range(4):
            ny, nx = y + dY[d], x + dX[d]
            if ny not in range(4) or nx not in range(3): continue
            if visited[ny][nx] <= dist + 1: continue
            q.append((ny, nx))
            visited[ny][nx] = dist + 1
    l_dist = visited[left[0]][left[1]]
    r_dist = visited[right[0]][right[1]]
    return l_dist, r_dist

def num_to_point(num):
    for i in range(4):
        for j in range(3):
            if pad[i][j] == num:
                return (i, j)

def solution(numbers, hand):
    answer = ''
    l_hand = [3, 0]
    r_hand = [3, 2]
    l_only = [1, 4, 7]
    r_only = [3, 6, 9]

    for num in numbers:
        if num in l_only:
            answer +='L'
            l_hand = [l_only.index(num), 0]
        elif num in r_only:
            answer +='R'
            r_hand = [r_only.index(num), 2]
        else:
            target = num_to_point(num)
            l_dist, r_dist = dist_bfs(target, l_hand, r_hand)
            if l_dist == r_dist:
                if hand == 'left':
                    l_hand = target
                    answer +='L'
                else:
                    r_hand = target
                    answer +='R'
            elif l_dist < r_dist:
                l_hand = target
                answer +='L'
            else:
                r_hand = target
                answer +='R'
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))