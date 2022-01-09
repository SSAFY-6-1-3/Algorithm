def match(key, lock):
    pass


def solution(key, lock):
    answer = True
    key_90 = list(zip(*key))
    key_180 = list(zip(*key_90))
    key_270 = list(zip(*key_180))

    match(key, lock)
    match(key_90, lock)
    match(key_180, lock)
    match(key_270, lock)

    return answer




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))