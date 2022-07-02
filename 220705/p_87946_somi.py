from itertools import permutations

def go_dungeons(orders, k, dungeons):
    cnt = 0
    now_p = k  # 현재 피로도
    for idx in orders:
        if dungeons[idx][0] > now_p:
            break
        now_p -= dungeons[idx][1]
        cnt += 1
    return cnt


def solution(k, dungeons):
    answer = -1
    p = list(permutations(list(n for n in range(len(dungeons)))))  # 인덱스 순서
    for orders in p:
        cnt = go_dungeons(orders, k, dungeons)
        answer = max(answer, cnt)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))