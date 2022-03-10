# ????????????
import copy
answer = []
maxV = 1

def cal(n, L, A):
    apeach, lion = 0, 0
    for idx in range(n):
        if A[idx] == 0 and L[idx] == 0:         # 둘 다 맞추지 못 했을 때는 점수 없음 !!!
            continue
        elif A[idx] < L[idx]:
            lion += (10 - idx)
        else:
            apeach += (10 - idx)
    return lion - apeach

def compare(res, L):
    global answer, maxV

    if maxV < res:
        answer = [copy.deepcopy(L)]
        maxV = res
    elif maxV == res:
        answer.append(copy.deepcopy(L))


def solution(n, info):
    global answer

    def score(s, L, check, cnt):

        if cnt == 11:
            if sum(L) == n:
                compare(cal(n, L, info), L)

            elif sum(L) < n:
                for k in range(10, -1, -1):
                    if not L[k]:
                        L[k] = n - sum(L)
                        compare(cal(n, L, info), L)
                        L[k] = 0
                        break
            return
        for i in range(s, 11):
            L[i] = info[i] + 1
            score(i + 1, L, check, cnt+1)
            L[i] = 0
            score(i + 1, L, check, cnt + 1)

    score(0, [0] * 11, [0] * 11, 0)
    if not answer:
        return [-1]
    answer.sort(key = lambda x : x[::-1])
    return answer[-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))