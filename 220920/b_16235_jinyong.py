import sys


def base_tuple(number):
    result = [5, int(number)]
    return result


def solution(trees, field, limit, count, n):
    answer = count
    for _ in range(limit):  # K년 후의 경과를 알기 위한 반복문

        for r in range(n):
            for c in range(n):

                # 각 칸마다 봄 여름 가을 겨울은 독립적이므로, 모두 한 번에 구현하고 다음 칸으로 넘긴다
                if not trees[r][c]:  # 현재 칸에 나무가 없으면 겨울에 양분을 추가하고 넘어간다.
                    field[r][c][0] += field[r][c][1]
                    continue

                die_tree = 0
                tree = sorted(trees[r][c])
                new_trees = []
                for tree_age in tree:

                    if tree_age <= field[r][c][0]:  # 땅에 남아 있는 양분이 나무 나이 이하인 경우
                        new_trees.append(tree_age + 1)
                        field[r][c][0] -= tree_age

                        if (tree_age + 1) % 5:  # 증가한 나이가 5의 배수가 아닌 경우
                            continue

                        # 증가한 나이가 5의 배수이기 때문에 인접한 칸에 나무가 늘어난다
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                nr, nc = r + i, c + j

                                if nr == r and nc == c:
                                    continue

                                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                                    continue

                                # 인접한 칸들 중에서 이미 탐색한 칸은 나무의 나이를 1로 해서 늘리고, 그렇지 않은 칸은 0으로 늘린다
                                # 다음에 탐색할 칸에 나무의 나이를 1로 해서 추가하면, 바로 2살이 되버리기 때문!
                                if nr < r or (nr == r and nc < c):
                                    trees[nr][nc].append(1)
                                else:
                                    trees[nr][nc].append(0)

                                answer += 1

                    else:  # 땅에 남아 있는 양분이 적어 나무가 죽는 경우
                        die_tree += tree_age // 2  # 여름에는 나무가 죽어 땅에 양분을 추가한다
                        answer -= 1

                trees[r][c] = new_trees  # 봄, 여름, 가을이 지난 뒤 현재 칸에 남아있는 나무들
                field[r][c][0] += field[r][c][1] + die_tree  # 겨울에 땅에 양분 + 죽은 나무에서 흡수한 양분을 추가하고 다음 칸으로 넘어간다

    return answer


N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(base_tuple, sys.stdin.readline().split())) for _ in range(N)]
numbers = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    numbers[x - 1][y - 1].append(z)

print(solution(numbers, A, K, M, N))
