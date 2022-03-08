import copy
def solution(n, info):
    answers = []
    max_pnt = 0
    need = [info[i]+1 for i in range(11)]

    def check_pnt(get):
        pnt = 0
        for i in range(11):
            if i in get:
                pnt += (10 - i) * (2 if info[i] else 1)
        return pnt



    def dfs(now, get, arw):
        nonlocal answers, max_pnt

        if not arw or now==10:
            pnt = check_pnt(get)
            if pnt > max_pnt:
                answers = [copy.deepcopy(get)]
                max_pnt = pnt
            elif pnt == max_pnt:
                answers.append(copy.deepcopy(get))
            return

        did_win = False
        for i in range(now+1, 11):
            if need[i] <= arw:
                did_win = True
                get.append(i)
                dfs(i, get, arw-need[i])
                get.pop()

        if not did_win:
            dfs(10, get, arw)

    dfs(-1, [], n)

    for a in range(len(answers)):

        answer = [need[i] if i in answers[a] else 0 for i in range(11)]
        answer[10] = n-sum(answer)
        answers[a] = answer

    answers.sort(key = lambda x: (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4],-x[3],-x[2], -x[1]))
    ret = answers[0]

    ry, ap = 0, 0
    for i in range(10):
        if ret[i]:
            ry += 10-i
        elif info[i]:
            ap += 10-i

    if ry > ap:
        return ret
    return [-1]



print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))




# def solution(n, info):
#     answer = [0]*11
#     is_ry_win = [False] * 11
#     # [화살 당 점수, 얻기 위한 화살 수)
#     towin = [[(10-i) * (1+(1 if info[i] else 0)) / (info[i]+1), info[i]+1] for i in range(11)]
#     towin = sorted(enumerate(towin), key=lambda x: (-x[1][0], -x[0]))
#
#     for a in towin:
#         if a[1][1] <= n:
#             is_ry_win[a[0]] = True
#             n -= a[1][1]
#             answer[a[0]] += a[1][1]
#
#     ap = [(10-i)*(0 if is_ry_win[i] or not info[i] else 1) for i in range(11)]
#     ry = [(10-i)*(1 if is_ry_win[i] else 0) for i in range(11)]
#
#     if sum(ap)>=sum(ry):
#         return [-1]
#     answer[10] = n
#     return answer