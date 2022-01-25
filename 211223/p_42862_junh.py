def solution(n, lost, reserve):
    answer = 0
    lost, reserve = set(lost), set(reserve)
    lost, reserve = lost - reserve, reserve - lost  # 순서에 유의
    lost, reserve = sorted(lost), sorted(reserve)

    for i in range(len(reserve)-1, -1, -1):
        r = reserve[i]
        if lost.count(r) > 0: continue
        if r<n and lost.count(r+1):
            r_p = lost.index(r+1)
            if r_p > -1:
                lost.pop(r_p)
                continue
        if r>0 and lost.count(r-1):
            r_m = lost.index(r-1)
            if r_m > -1:
                lost.pop(r_m)

    return n - len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution( 9, [5,6,8,1,2], [2,3,1,4,8,9 ] ))