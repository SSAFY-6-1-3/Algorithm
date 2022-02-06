


def solution(citations):
    answer = 0

    def bin_search(l, r):
        nonlocal answer
        if l > r : return
        mid = (l + r) // 2

        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                cnt += 1

        if cnt >= mid:
            answer = mid
            bin_search(mid+1, r)
        else:
            bin_search(l, mid-1)

    bin_search(0, 10001)

    return answer


print(solution([3, 0, 6, 1, 5]))