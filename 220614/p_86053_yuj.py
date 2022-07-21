
def solution(a, b, g, s, w, t):
    answer = 0
    start = 0
    # 최댓값
    end = 2 * max(t) * (a + b)
    while start < end:
        mid = (start + end) // 2
        gold, silver = 0, 0

        for idx in range(len(t)):
            cnt = mid // (t[idx] * 2)
            if mid % (t[idx] * 2) >= t[idx]:
                cnt += 1

            if a > gold:
                gold += min(g[idx], w[idx]) * cnt

        if gold < a and silver < b:
            start = mid+1
        else:
            answer = min(mid, answer)
            end = mid-1

    return answer

print(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1])