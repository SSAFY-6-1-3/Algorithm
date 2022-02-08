# 답이 꼭 citations에 있는 값이 아니어도 된다!

def solution(citations):
    citations.sort()
    for num in range(len(citations), -1, -1):
        cnt = 0
        for c in citations:
            if c >= num:
                cnt += 1
        if cnt >= num:
            return num

# 다른 풀이
def solution(citations):
    citations.sort()
    l = len(citations)
    for num in range(l):
        if citations[num] >= l-num:
            return l-num
    return 0

print(solution([3, 0, 6, 1, 5]))